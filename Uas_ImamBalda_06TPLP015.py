import matplotlib.pyplot as plt

class BaseFuzzy:
    def __init__(self):
        self.minimum = 0
        self.maximum = 0

    def up(self):
        pass

    def down(self):
        pass


class Pressure(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 10
        self.p1 = 5
        self.p2 = 8
        self.p3 = 15
        self.p4 = 20
        self.p5 = 28
        self.p6 = 10
        self.p7 = 37
        self.p8 = 40
        self.p9 = 47

    def very_low(self, pressure):
        if pressure <= self.p1:
            return 1
        elif pressure <= self.p3:
            return (self.p3 - pressure) / (self.p3 - self.p1)
        else:
            return 0

    def low(self, pressure):
        if pressure <= self.p2:
            return 0
        elif pressure <= self.p4:
            return (pressure - self.p2) / (self.p4 - self.p2)
        else:
            return 0

    def medium(self, pressure):
        if pressure <= self.p5 or pressure > self.p7:
            return 0
        elif pressure <= self.p6:
            return (pressure - self.p5) / (self.p6 - self.p5)
        elif pressure <= self.p7:
            return 1
        else:
            return 0

    def high(self, pressure):
        if pressure <= self.p6 or pressure > self.p9:
            return 0
        elif pressure <= self.p8:
            return (pressure - self.p6) / (self.p8 - self.p6)
        elif pressure <= self.p9:
            return 1
        else:
            return 0

    def very_high(self, pressure):
        if pressure <= self.p8:
            return 0
        elif pressure <= self.p9:
            return (pressure - self.p8) / (self.p9 - self.p8)
        else:
            return 0

class Temperature(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 50

    def very_cold(self, temperature):
        if temperature <= 10:
            return 1
        elif temperature <= 20:
            return (20 - temperature) / (20 - 10)
        else:
            return 0

    def cold(self, temperature):
        if temperature <= 10 or temperature >= 30:
            return 0
        elif temperature <= 20:
            return (temperature - 10) / (20 - 10)
        elif temperature < 30:
            return (30 - temperature) / (30 - 20)

    def warm(self, temperature):
        if temperature <= 20 or temperature >= 40:
            return 0
        elif temperature <= 30:
            return (temperature - 20) / (30 - 20)
        elif temperature < 40:
            return (40 - temperature) / (40 - 30)

    def hot(self, temperature):
        if temperature <= 30 or temperature >= 50:
            return 0
        elif temperature <= 40:
            return (temperature - 30) / (40 - 30)
        elif temperature < 50:
            return (50 - temperature) / (50 - 40)

    def very_hot(self, temperature):
        if temperature <= 40:
            return 0
        elif temperature <= 50:
            return (temperature - 40) / (50 - 40)
        else:
            return 1


class Speed(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.minimum = 0
        self.maximum = 110

    def slow(self, speed):
        if speed <= 40:
            return 1
        elif speed <= 60:
            return (60 - speed) / (60 - 40)
        else:
            return 0

    def medium(self, speed):
        if speed <= 40 or speed >= 100:
            return 0
        elif speed <= 60:
            return (speed - 40) / (60 - 40)
        elif speed <= 80:
            return 1
        elif speed <= 100:
            return (100 - speed) / (100 - 80)

    def fast(self, speed):
        if speed <= 80:
            return 0
        elif speed <= 100:
            return (speed - 80) / (100 - 80)
        else:
            return 1


if __name__ == "__main__":
    temperature_value = float(input("Enter the temperature value: "))
    pressure_value = float(input("Enter the pressure value: "))

    pressure_obj = Pressure()
    temperature_obj = Temperature()
    speed_obj = Speed()

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    x_pressure = list(range(pressure_obj.minimum, pressure_obj.maximum + 1))
    y_pressure_very_low = [pressure_obj.very_low(p) for p in x_pressure]
    y_pressure_low = [pressure_obj.low(p) for p in x_pressure]
    y_pressure_medium = [pressure_obj.medium(p) for p in x_pressure]
    y_pressure_high = [pressure_obj.high(p) for p in x_pressure]
    y_pressure_very_high = [pressure_obj.very_high(p) for p in x_pressure]

    axs[0].plot(x_pressure, y_pressure_very_low, label='Very Low')
    axs[0].plot(x_pressure, y_pressure_low, label='Low')
    axs[0].plot(x_pressure, y_pressure_medium, label='Medium')
    axs[0].plot(x_pressure, y_pressure_high, label='High')
    axs[0].plot(x_pressure, y_pressure_very_high, label='Very High')

    axs[0].set_xlabel('Pressure')
    axs[0].set_ylabel('Membership')
    axs[0].set_title('Pressure Membership Functions')
    axs[0].legend()

    x_temperature = list(range(temperature_obj.minimum, temperature_obj.maximum + 1))
    y_temperature_very_cold = [temperature_obj.very_cold(t) for t in x_temperature]
    y_temperature_cold = [temperature_obj.cold(t) for t in x_temperature]
    y_temperature_warm = [temperature_obj.warm(t) for t in x_temperature]
    y_temperature_hot = [temperature_obj.hot(t) for t in x_temperature]
    y_temperature_very_hot = [temperature_obj.very_hot(t) for t in x_temperature]

    axs[1].plot(x_temperature, y_temperature_very_cold, label='Very Cold')
    axs[1].plot(x_temperature, y_temperature_cold, label='Cold')
    axs[1].plot(x_temperature, y_temperature_warm, label='Warm')
    axs[1].plot(x_temperature, y_temperature_hot, label='Hot')
    axs[1].plot(x_temperature, y_temperature_very_hot, label='Very Hot')

    axs[1].set_xlabel('Temperature')
    axs[1].set_ylabel('Membership')
    axs[1].set_title('Temperature Membership Functions')
    axs[1].legend()

    x_speed = list(range(speed_obj.minimum, speed_obj.maximum + 1))
    y_speed_slow = [speed_obj.slow(s) for s in x_speed]
    y_speed_medium = [speed_obj.medium(s) for s in x_speed]
    y_speed_fast = [speed_obj.fast(s) for s in x_speed]

    axs[2].plot(x_speed, y_speed_slow, label='Slow')
    axs[2].plot(x_speed, y_speed_medium, label='Medium')
    axs[2].plot(x_speed, y_speed_fast, label='Fast')

    axs[2].set_xlabel('Speed')
    axs[2].set_ylabel('Membership')
    axs[2].set_title('Speed Membership Functions')
    axs[2].legend()
    axs[2].set_xticks([0, 40, 60, 80, 100])

    plt.tight_layout()
    plt.show()
