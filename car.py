class Car:
    """
    Class for defining a car and calculating its performance under various conditions.
    """
    typical_dry_deceleration = -7.5  # m/s^2
    typical_wet_deceleration = -3  # m/s^2
    typical_frozen_deceleration = -1.5  # m/s^2

    def __init__(self, brand, model, acceleration_0_100_km_h, max_speed_km_h, mass=0):
        """
        Initializes an instance of the Car class.

        :param brand: The brand of the car.
        :param model: The model of the car.
        :param acceleration_0_100_km_h: Acceleration time from 0 to 100 km/h (in seconds).
        :param max_speed_km_h: The car's maximum speed in km/h.
        :param mass: The mass of the car in kilograms (default 0).
        """
        def convert_km_h_to_m_s2(value) -> float:
            """
            :param value: The value to be converted.
            :return: Converts speed from km/h to m/s^2.
            """
            return value * 1000 / 3600

        # Unique variables for each car
        self.brand = brand
        self.model = model
        self.full_name = f"{self.brand} {self.model}"
        self.max_speed_km_h = max_speed_km_h
        self.mass = mass
        self.acceleration_0_100_km_h = acceleration_0_100_km_h

        # Converted variables
        self.max_speed_m_s2 = convert_km_h_to_m_s2(max_speed_km_h)
        self.speed_100 = convert_km_h_to_m_s2(100)

    def car_acceleration(self) -> float:
        """
        Calculates the car's acceleration in m/s^2.

        :return: The car's acceleration in m/s^2.
        """
        return self.speed_100 / self.acceleration_0_100_km_h

    def time_to_max_speed(self) -> float:
        """
        Calculates the time to reach the maximum speed.

        :return: The time to reach maximum speed in seconds.
        """
        return self.max_speed_m_s2 / self.car_acceleration()

    def braking_time_max_speed(self, surface_type: str) -> float:
        """
        Calculates the braking time from maximum speed.

        :param surface_type: The type of road surface (Dry/Wet/Frozen).
        :return: The braking time in seconds.
        """

        match surface_type:

            case "Dry":
                return self.max_speed_m_s2 / abs(Car.typical_dry_deceleration)

            case "Wet":
                return self.max_speed_m_s2 / abs(Car.typical_wet_deceleration)

            case "Frozen":
                return self.max_speed_m_s2 / abs(Car.typical_frozen_deceleration)

            case _:
                print(Exception("Surface type is unknown. Try 'Dry'/'Wet'/'Frozen'"))

    def traction_force(self) -> float:
        """
        Calculates the traction force required for the car.

        :return: The traction force in newtons (N).
        """
        return self.mass * self.car_acceleration()

    def braking_distance(self, surface_type: str) -> float:
        """
        Calculates the braking distance from maximum speed.

        :param surface_type: The type of road surface (Dry/Wet/Frozen).
        :return: The braking distance in meters (m).
        """

        deceleration = 0
        match surface_type:

            case "Dry":
                deceleration = Car.typical_dry_deceleration

            case "Wet":
                deceleration = Car.typical_wet_deceleration

            case "Frozen":
                deceleration = Car.typical_frozen_deceleration

            case _:
                print(Exception("Surface type is unknown. Try 'Dry'/'Wet'/'Frozen'"))

        return (self.max_speed_m_s2 * self.braking_time_max_speed(surface_type)
                + 0.5 * deceleration * (self.braking_time_max_speed(surface_type)
                                        * self.braking_time_max_speed(surface_type)))

    # Functions returning a string
    def get_string_car_acceleration(self) -> str:
        return f"{self.car_acceleration():.2f} m/s^2"

    def get_string_time_to_max_speed(self) -> str:
        return f"{self.time_to_max_speed():.2f} seconds."

    def get_string_braking_time_max_speed(self, surface_type) -> str:
        return f" {self.braking_time_max_speed(surface_type):.2f} seconds. "

    def get_string_traction_force(self) -> str:
        return f"{self.traction_force():.2f} N"

    def get_string_braking_distance(self, braking_type: str) -> str:
        return f" {self.braking_distance(braking_type):.2f} m"

