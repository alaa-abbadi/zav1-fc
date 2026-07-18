class PhysicsEngine:
    def __init__(self):
        self.dt = 0.01

    def rk4_step(self, state, derivatives, t):
        k1 = derivatives(state, t)
        k2 = derivatives(state + k1 * self.dt / 2, t + self.dt / 2)
        k3 = derivatives(state + k2 * self.dt / 2, t + self.dt / 2)
        k4 = derivatives(state + k3 * self.dt, t + self.dt)
        return state + (self.dt / 6) * (k1 + 2*k2 + 2*k3 + k4)