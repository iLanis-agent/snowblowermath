var SnowblowerMath = (function () {
  function num(x) { return typeof x === "number" && isFinite(x); }
  function pos(x) { return num(x) && x > 0; }
  function r1(x) { return Math.round(x * 10) / 10; }
  function jsnum(x) { if (typeof x === "number" && isFinite(x) && x === Math.trunc(x)) return String(Math.trunc(x)); return String(x); }
  var CC_PER_HP = 32;
  function enginePlan(cc, claimedHp) {
    if (!pos(cc)) return { error: "the engine cc must be above zero" };
    if (!pos(claimedHp)) return { error: "the claimed horsepower must be above zero" };
    var honestHp = cc / CC_PER_HP;
    var ratio = claimedHp / honestHp;
    var verdict = ratio <= 1.05 ? "honestly rated"
      : ratio <= 1.35 ? "optimistic horses"
      : "marketing horses";
    return { honestHp: r1(honestHp), pct: r1(ratio * 100), verdict: verdict };
  }
  function renderEngine(r, cc, claimedHp) {
    return "The " + jsnum(cc) + "-cc engine honestly makes about " + jsnum(r.honestHp)
      + " horsepower at the 32-cc-per-horse norm; the box says " + jsnum(claimedHp) + " - "
      + jsnum(r.pct) + "% of honest, " + r.verdict + ".";
  }
  function intakePlan(intakeIn, stormIn) {
    if (!pos(intakeIn)) return { error: "the intake inches must be above zero" };
    if (!pos(stormIn)) return { error: "the storm inches must be above zero" };
    var passes = Math.ceil(stormIn / intakeIn);
    var verdict = passes <= 1 ? "one honest pass"
      : passes <= 2 ? "two passes, no shame"
      : "shovel the top first";
    return { passes: passes, verdict: verdict };
  }
  function renderIntake(r, intakeIn, stormIn) {
    var word = r.passes === 1 ? " pass - " : " passes - ";
    return "The " + jsnum(intakeIn) + "-inch intake against the " + jsnum(stormIn) + "-inch storm takes "
      + jsnum(r.passes) + word + r.verdict + ".";
  }
  function throwPlan(stickerFt, keep, needFt) {
    if (!pos(stickerFt)) return { error: "the sticker throw must be above zero" };
    if (!pos(keep) || keep > 1) return { error: "the snow keep must sit between zero and 1" };
    if (!pos(needFt)) return { error: "the drop-zone feet must be above zero" };
    var honestFt = stickerFt * keep;
    var ratio = honestFt / needFt;
    var verdict = ratio >= 1 ? "reaches the drop zone"
      : ratio >= 0.6 ? "lands short, aim again"
      : "feeds the hedge";
    return { honestFt: r1(honestFt), pct: r1(ratio * 100), verdict: verdict };
  }
  function renderThrow(r, stickerFt, keep, needFt) {
    return "The " + jsnum(stickerFt) + "-foot sticker throw at the " + jsnum(keep) + " keep honestly throws about "
      + jsnum(r.honestFt) + " feet against the " + jsnum(needFt) + " needed - "
      + jsnum(r.pct) + "% of the gap: " + r.verdict + ".";
  }
  return { enginePlan: enginePlan, renderEngine: renderEngine, intakePlan: intakePlan, renderIntake: renderIntake, throwPlan: throwPlan, renderThrow: renderThrow };
})();
if (typeof module !== "undefined" && module.exports) module.exports = SnowblowerMath;
