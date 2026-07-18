class AeroModel:
        def __init__(self, cd_base, area):
                        self.cd = cd_base        self.area = area
                            def get_drag(self, rho, velocity):
                                        return 0.5 * rho * (velocity**2) * self.cd * self.area