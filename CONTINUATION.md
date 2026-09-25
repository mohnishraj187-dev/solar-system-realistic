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

## Important honesty/limitations

- The asteroid belt and Kuiper belt are statistical visualisations, not a complete live catalogue of every known object.
- Small-body models are procedural irregular meshes, not individually imported NASA shape models.
- Spacecraft are stylised geometry, not engineering-accurate imported CAD/glTF models.
- Solar-system distances and body sizes cannot both be shown physically to scale on one screen, so body sizes and spacecraft distances are visually exaggerated.
- The realistic branch currently has the JPL proxy hardcoded to port 8001.

## Git status

Latest local commit:

```text
20209ab Add axial rotation to celestial bodies
```

The local repository remote is configured for the GitHub URL above. GitHub authentication was not available from the original session, so push with:

```bash
git push origin main
```

## Most recent user request

The user asked to save the whole conversation for continuation from another account. This file is the project handoff. Read it together with `index.html` before changing anything.

## Suggested next work

1. Replace spacecraft primitives with actual ISS/Hubble/JWST glTF models.
2. Replace statistical small-body meshes with selected NASA/JPL/MPC orbital catalogues.
3. Improve solar prominence geometry so both ends visibly anchor to the Sun surface.
4. Add labels/toggles for asteroid belt, Trojan clouds, Centaurs, nebulae, and spacecraft.
5. Add a proper data-source/about panel and loading/error states.
