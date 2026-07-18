import numpy as np

from atmosphere import ISAEnviroment
from physics_engine import PhysicsEngine
from aerodynamics import AeroModel
from sensor_bmp280 import BMP280
from state_machine import FlightStateMachine
from telementry_logger import TelemetryLogger
from post_flight import generate_report

MASS_KG = 5.0
GRAVITY = 9.81
THRUST_N = 200.0
BURN_TIME_S = 2.0
MAX_SIM_TIME_S = 60.0
LOG_PATH = "flight_data.csv"


def make_derivatives(env, aero):
    def derivatives(state, t):
        altitude, velocity = state
        rho = env.get_density(max(altitude, 0.0))
        drag = aero.get_drag(rho, velocity)
        drag_force = -drag if velocity > 0 else drag
        thrust = THRUST_N if t <= BURN_TIME_S else 0.0
        acceleration = (thrust + drag_force - MASS_KG * GRAVITY) / MASS_KG
        return np.array([velocity, acceleration])
    return derivatives


def main():
    env = ISAEnviroment()
    phys = PhysicsEngine()
    aero = AeroModel(cd_base=0.5, area=0.02)
    sensor = BMP280()
    fsm = FlightStateMachine()
    logger = TelemetryLogger(LOG_PATH)
    derivatives = make_derivatives(env, aero)

    state = np.array([0.0, 0.0])
    t = 0.0

    print("Simulation starting...")

    while t < MAX_SIM_TIME_S:
        state = phys.rk4_step(state, derivatives, t)
        altitude, velocity = state
        if altitude < 0:
            altitude, velocity = 0.0, 0.0
            state = np.array([altitude, velocity])

        fsm.update(altitude, velocity)
        pressure = sensor.read_data(altitude)

        logger.log({
            "time": round(t, 3),
            "altitude": round(altitude, 3),
            "velocity": round(velocity, 3),
            "pressure": round(pressure, 2),
            "state": fsm.state,
        })

        t += phys.dt
        if fsm.state == "LANDED":
            break

    print(f"Simulation ended at t={t:.2f}s, final state={fsm.state}")
    print(f"Telemetry written to {LOG_PATH}")
    print("\nPost-flight report:")
    print(generate_report(LOG_PATH))


if __name__ == "__main__":
    main()
