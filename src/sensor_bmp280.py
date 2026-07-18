import random

class BMP280:
    def read_data(self, altitude):
        # Emulate sensor noise and barometric reading
        pressure = 101325 * (1 - 2.25577e-5 * altitude)**5.25588
        return pressure + random.uniform(-10, 10)