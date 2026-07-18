class ISAEnviroment:
    """International Standard Atmosphere model (troposphere, 0-11km)."""

    SEA_LEVEL_PRESSURE = 101325.0
    SEA_LEVEL_TEMP = 288.15
    LAPSE_RATE = 0.0065
    GAS_CONSTANT_AIR = 287.05

    def get_temperature(self, altitude):
        return self.SEA_LEVEL_TEMP - self.LAPSE_RATE * altitude

    def get_pressure(self, altitude):
        return self.SEA_LEVEL_PRESSURE * (1 - 2.25577e-5 * altitude) ** 5.25588

    def get_density(self, altitude):
        pressure = self.get_pressure(altitude)
        temperature = self.get_temperature(altitude)
        return pressure / (self.GAS_CONSTANT_AIR * temperature)
