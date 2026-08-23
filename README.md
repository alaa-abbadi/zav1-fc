# ZAV-1 Flight Simulation

A small Python simulation of a rocket's vertical flight: powered ascent, coast, descent, and landing.

## ⚡ Try it Now

**[🚀 Live Demo](https://alaa-abbadi.github.io/zav1-fc/)** — Run the simulation in your browser with no installation required!

#### What it does

- Integrates the flight state (altitude, velocity) with an RK4 physics engine
- Models drag using an ISA (International Standard Atmosphere) density model and a simple aerodynamics module
- Emulates a BMP280 barometric pressure sensor reading altitude, with noise
- Tracks flight phase through a state machine (`GROUND_IDLE` -> `ASCENT` -> `COAST` -> `LANDED`)
- Logs every simulation step to `flight_data.csv`
- Generates a post-flight summary report from the logged telemetry

#### Running from source

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python src/zavmain.py
```

##### Running the compiled binary

A standalone binary can be built with PyInstaller:

```bash
.venv/bin/pip install pyinstaller
.venv/bin/pyinstaller --onefile --name zav1-sim src/zavmain.py
./dist/zav1-sim
```

VERY IMPORTANT!!!!!
Limitation: PyInstaller does not cross-compile. A binary built on Linux only runs on Linux; macOS and Windows binaries must be built on those respective OSes. The binary included with this submission was compiled on a 64-bit Ubuntu Linux system and is compatible with similar systems.
