# Solar System Realistic Lab — Continuation Handoff

## Project locations

- Realistic branch: `/home/mohnish/solar-system-realistic`
- Original prototype: `/home/mohnish/solar-system-3d` — leave untouched
- GitHub repository: `https://github.com/mohnishraj187-dev/solar-system-realistic`
- Local server port: `8001`

## Run

```bash
cd /home/mohnish/solar-system-realistic
python3 jpl_proxy.py
```

Open `http://localhost:8001`.

Port `8000` belongs to the older prototype.

## Current implementation

The app is a Three.js browser solar-system visualisation with:

- NASA/JPL planetary textures for Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Sun, Moon, Ceres, and Vesta.
- NASA/JPL Dawn surface maps for Ceres and Vesta.
- NASA lunar texture for the Moon.
- NASA/JPL surface maps for Jupiter's Io, Europa, Ganymede, and Callisto.
- NASA/JPL surface maps for Saturn's Titan, Rhea, Enceladus, and Iapetus.
- NASA Solar Dynamics Observatory image for the Sun.
- Animated but intermittent solar plasma prominences.
- Analytic orbital motion with a Moon orbit around Earth.
- Axial spin for the Sun and planets using approximate rotation periods; Venus and Uranus rotate retrograde.
- Realistic visual asteroid belt between Mars and Jupiter with irregular instanced rocks and approximate Kirkwood gaps.
- Jupiter Trojan populations around L4 and L5 using irregular asteroid meshes.
- Sparse Centaur objects between the giant planets.
- Kuiper belt particles.
- Irregular dark comet nucleus, coma, and tail.
- Saturn rings with concentric band mapping and gaps.
- Faint multiple nebula backgrounds and varied star colors.
- Visually exaggerated ISS, Hubble, and James Webb spacecraft near Earth/L2 so they are visible.
- Pause/reset, speed, camera focus, orbit trails, full-system/inner-system/Kuiper views, JPL buttons, free camera movement.
- Double-click close-up framing for planets and moons, with near-surface camera limits.
- Camera flight-speed HUD below the JPL status panel, shown as a fraction of light speed (`c`) with km/s reference.
- NASA-informed interplanetary dust: zodiacal dust concentrated inside about 2 AU and faint asteroid-associated bands near 2.30, 2.60, and 3.10 AU.

## Important honesty/limitations

- The asteroid belt and Kuiper belt are statistical visualisations, not a complete live catalogue of every known object.
- Small-body models are procedural irregular meshes, not individually imported NASA shape models.
- Spacecraft are stylised geometry, not engineering-accurate imported CAD/glTF models.
- Solar-system distances and body sizes cannot both be shown physically to scale on one screen, so body sizes and spacecraft distances are visually exaggerated.
- The realistic branch currently has the JPL proxy hardcoded to port 8001.

## Git status

Latest local commit:

```text
f36cf90 Remove stale real reference from satellite setup
```

The local repository remote is configured for the GitHub URL above. GitHub authentication was not available from the original session, so push with:

```bash
git push origin main
```

## Most recent user request

The user asked to save the whole conversation for continuation from another account. This file is the project handoff. Read it together with `index.html` before changing anything.

## 2026-09-27 session notes

- Added and committed NASA/JPL maps for the eight major Jupiter/Saturn moons (`0c11309`).
- Replaced broad invented outer dust clouds with a NASA-informed zodiacal-dust and asteroid-dust-band model (`f616c96`). NASA describes zodiacal dust as concentrated near the ecliptic and reports dust bands associated with asteroid-belt collisions.
- Added close-up camera controls and lower camera distance (`d9a48df`). Double-click a body to frame it closely.
- Added camera speed display as a fraction of light speed plus km/s (`5863a8a`).
- Changed the simulation to start running automatically (`caecd33`).
- Fixed a startup error caused by a stale satellite setup reference to `real`; latest cleanup commit is `f36cf90`.
- If the deployed Vercel page still reports `real is not defined`, push the latest commits and hard-refresh the deployment (`Ctrl+Shift+R`).

## Suggested next work

1. Replace spacecraft primitives with actual ISS/Hubble/JWST glTF models.
2. Replace statistical small-body meshes with selected NASA/JPL/MPC orbital catalogues.
3. Improve solar prominence geometry so both ends visibly anchor to the Sun surface.
4. Add labels/toggles for asteroid belt, Trojan clouds, Centaurs, nebulae, and spacecraft.
5. Add a proper data-source/about panel and loading/error states.
