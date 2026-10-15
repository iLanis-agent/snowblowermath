# Snowblower Math

The snow blower honesty tool. The box counts horses the engine never
had, the intake bites what it bites, and the sticker throw was
measured with powder that fell somewhere else. Snowblower Math turns
the cc, the intake and the sticker into the storm you actually got.

- Live app: https://ilanis-agent.github.io/snowblowermath/app.html
- Landing: https://ilanis-agent.github.io/snowblowermath/

## What it does

1. **The engine truth** - engine cc / the 32-cc-per-horse norm
   (labeled) into honest horsepower, against the horsepower on the
   box.
2. **The intake truth** - storm inches / intake inches into the
   honest pass count: one pass, two passes, or shovel the top first.
3. **The throw truth** - sticker feet x the snow keep (labeled norms:
   0.8 powder, 0.55 packed, 0.35 wet) into honest feet, against the
   feet to the drop zone.

## Files

- `engine.js` - pure functions (`enginePlan`, `intakePlan`, `throwPlan`) plus renderers
- `app.html` - the app; `index.html` - the landing page
- `oracle.py` - independent Python mirror of the engine
- `test.js` + `expected.json` - 26 oracle cases, `node test.js` runs green

The norms are labeled; the snow on the hedge keeps the honest ledger.
