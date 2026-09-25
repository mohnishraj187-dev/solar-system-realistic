# Solar System — Realistic Data Lab

This is the separate realism branch. The original `/home/mohnish/solar-system-3d` project is unchanged.

Run it from this directory:

```bash
python3 jpl_proxy.py
```

Then open `http://localhost:8000`.

Data provenance:

- Planetary state vectors: NASA/JPL Horizons through the local proxy.
- Planet texture reference: NASA/JPL Solar System Simulator map collection.
- Small-body fields: deliberately statistical visualisation, because rendering every asteroid as a real mesh would be misleading and too expensive. The next data pass can replace these with a selected MPC/JPL catalogue.

Important visual note: astronomical distances and physical diameters cannot both be visible in one screen. The renderer therefore uses correct orbital distances and an explicitly labelled visual radius multiplier for visibility.
