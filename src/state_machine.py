class FlightStateMachine:
    def __init__(self):
        self.state = "GROUND_IDLE"

    def update(self, altitude, velocity):
        if self.state == "GROUND_IDLE" and velocity > 10:
            self.state = "ASCENT"
        elif self.state == "ASCENT" and velocity < 0:
            self.state = "COAST"