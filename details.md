# Solar System Realistic — Project Details

## Overview

This repository is a browser-based Three.js solar-system visualization. The main renderer is in `index.html`; `jpl_proxy.py` serves the project and proxies NASA/JPL Horizons requests.

## Technology

- Three.js `0.161.0` loaded from a CDN.
- Three.js `OrbitControls`.
- GSAP `3.13.0` for smooth camera transitions.
- Vanilla HTML and JavaScript; no `package.json` or build system.
- Python server/proxy on port `8001`.
- NASA/JPL texture assets in `textures/`.

## Features

- Sun, planets, dwarf planets, the Moon, and selected planetary moons.
- Textures, axial rotation, orbital motion, trails, rings, stars, nebulae, asteroid belts, Trojan populations, Centaurs, Kuiper particles, dust bands, comet effects, and stylized spacecraft.
- Camera focus, double-click close-ups, inner/full/Kuiper views, keyboard flight, JPL data buttons, and GSAP camera transitions.
- Keyboard flight uses `W/A/S/D` and `Q/E`; short presses move slightly and held keys accelerate.

## Orbital and gravity model

The scene uses Euclidean 3D coordinates. The active animation primarily uses simplified Keplerian angular motion. The source also contains Newtonian inverse-square routines in `simulateLegacy()` and `simulateNBody()`.

The project uses AU, years, and solar masses with `G = 4 * Math.PI * Math.PI`. It is not a general-relativistic or high-precision ephemeris simulator.

## Moon landing mode

The Moon has higher-resolution geometry, procedural crater bump/displacement, a surface collision boundary, and a `Land on Moon` button. Landing mode creates a local procedural lunar terrain scene with texture, elevation, crater detail, lighting, surface exploration, and a distant visual sky containing the Sun and planets.

The lunar terrain is an approximation. It is not a NASA digital elevation model and does not yet provide exact lunar coordinates, real-time ephemeris projection, or a physically accurate lunar day/night system.

## Earth landing mode

`Land on Earth` provides a first-pass Earth-like local scene with blue sky, green procedural terrain, sunlight, hemisphere lighting, and keyboard exploration. It currently does not use real Earth elevation, coastlines, clouds, cities, or a detailed atmosphere.

## Important limitations

- Landing scenes are local visual environments rather than physically connected to the full-scale orbital coordinate system.
- Celestial bodies in landing skies are visual representations and are not yet correctly projected from live ephemeris data.
- Planet sizes and distances are intentionally exaggerated for visibility.
- Asteroid fields are statistical visualizations, not complete catalogues.
- Spacecraft are stylized primitives.
- The JPL proxy uses hardcoded dates and port `8001`.
- Much of `index.html` is compressed into long JavaScript lines, making maintenance difficult.

## Run locally

Run `python3 jpl_proxy.py` from the repository directory and open `http://localhost:8001`. Use `Ctrl+Shift+R` after deployment changes.

## Git workflow

Use `git add index.html details.md`, then `git commit -m "Update project details"`, followed by `git push origin main`.

If GitHub reports `Internal Server Error` or `Could not resolve host`, inspect `git status --short --branch`, `git log --oneline -8`, `git fsck --full --no-progress`, and `git rev-list --left-right --count origin/main...HEAD`. Do not force-push unless overwriting remote history is intentional.

## Suggested next improvements

1. Replace procedural lunar terrain with NASA elevation tiles or a selected DEM.
2. Add a proper local tangent-frame controller and terrain collision.
3. Calculate Sun, Earth, Moon, and planet visibility from the landing location.
4. Add real day/night systems for Moon and Earth.
5. Add atmospheric scattering and Earth clouds.
6. Replace hardcoded JPL dates with current or user-selected dates.
7. Split the compressed renderer into maintainable modules.

