import json, math

def num(x): return isinstance(x,(int,float)) and not isinstance(x,bool) and math.isfinite(x)
def pos(x): return num(x) and x>0
def jround(x): return math.floor(x+0.5)
def r1(x): return jround(x*10)/10
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)

CC_PER_HP=32

def engine_plan(cc,claimed_hp):
    if not pos(cc): return {"error":"the engine cc must be above zero"}
    if not pos(claimed_hp): return {"error":"the claimed horsepower must be above zero"}
    honest_hp=cc/CC_PER_HP
    ratio=claimed_hp/honest_hp
    if ratio<=1.05: verdict="honestly rated"
    elif ratio<=1.35: verdict="optimistic horses"
    else: verdict="marketing horses"
    return {"honestHp":r1(honest_hp),"pct":r1(ratio*100),"verdict":verdict}

def render_engine(r,cc,claimed_hp):
    return ("The "+jsnum(cc)+"-cc engine honestly makes about "+jsnum(r["honestHp"])
            +" horsepower at the 32-cc-per-horse norm; the box says "+jsnum(claimed_hp)+" - "
            +jsnum(r["pct"])+"% of honest, "+r["verdict"]+".")

def intake_plan(intake_in,storm_in):
    if not pos(intake_in): return {"error":"the intake inches must be above zero"}
    if not pos(storm_in): return {"error":"the storm inches must be above zero"}
    passes=math.ceil(storm_in/intake_in)
    if passes<=1: verdict="one honest pass"
    elif passes<=2: verdict="two passes, no shame"
    else: verdict="shovel the top first"
    return {"passes":passes,"verdict":verdict}

def render_intake(r,intake_in,storm_in):
    word=" pass - " if r["passes"]==1 else " passes - "
    return ("The "+jsnum(intake_in)+"-inch intake against the "+jsnum(storm_in)+"-inch storm takes "
            +jsnum(r["passes"])+word+r["verdict"]+".")

def throw_plan(sticker_ft,keep,need_ft):
    if not pos(sticker_ft): return {"error":"the sticker throw must be above zero"}
    if not pos(keep) or keep>1: return {"error":"the snow keep must sit between zero and 1"}
    if not pos(need_ft): return {"error":"the drop-zone feet must be above zero"}
    honest_ft=sticker_ft*keep
    ratio=honest_ft/need_ft
    if ratio>=1: verdict="reaches the drop zone"
    elif ratio>=0.6: verdict="lands short, aim again"
    else: verdict="feeds the hedge"
    return {"honestFt":r1(honest_ft),"pct":r1(ratio*100),"verdict":verdict}

def render_throw(r,sticker_ft,keep,need_ft):
    return ("The "+jsnum(sticker_ft)+"-foot sticker throw at the "+jsnum(keep)+" keep honestly throws about "
            +jsnum(r["honestFt"])+" feet against the "+jsnum(need_ft)+" needed - "
            +jsnum(r["pct"])+"% of the gap: "+r["verdict"]+".")

cases=[]
def add(tool,args):
    if tool=="engine": r=engine_plan(*args); fn=render_engine
    elif tool=="intake": r=intake_plan(*args); fn=render_intake
    else: r=throw_plan(*args); fn=render_throw
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(208,8),(254,10),(179,6),(420,15),(212,6.5),(208,12)]:
    add("engine",a)
for a in [(21,14),(12,30),(21,8),(18,18),(24,36),(12,12)]:
    add("intake",a)
for a in [(40,0.55,15),(40,0.35,15),(30,0.8,20),(45,0.55,25),(35,0.35,30),(50,0.8,30)]:
    add("throw",a)
add("engine",[0,8]); add("engine",[208,0])
add("intake",[0,14]); add("intake",[21,0])
add("throw",[0,0.55,15]); add("throw",[40,0,15]); add("throw",[40,1.2,15]); add("throw",[40,0.55,0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
