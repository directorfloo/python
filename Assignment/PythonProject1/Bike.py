class AutoBike:
    def __init__(self):
        self.bike_on = False
        self.gear = 1
        self.speed = 0
        self.acceleration = 0
        self.deceleration = 0

    # ------------------- Power -------------------
    def get_turn_on(self):
        return self.bike_on

    def set_turn_on(self):
        self.bike_on = True

    def get_turn_off(self):
        return self.bike_on

    def set_turn_off(self):
        self.bike_on = False
        self.gear = 1
        self.speed = 0

    # ------------------- Gear -------------------
    def get_gear(self):
        return self.gear

    def set_gear(self):
        if self.speed <= 20:
            self.gear = 1
        elif 21 <= self.speed <= 30:
            self.gear = 2
        elif 31 <= self.speed <= 40:
            self.gear = 3
        elif 41 <= self.speed <= 50:
            self.gear = 4
        else:
            self.gear = 5

    # ------------------- Acceleration -------------------
    def get_acceleration(self):
        return self.acceleration

    def set_acceleration(self):
        if self.bike_on:
            self.speed += 5   # increase speed
            self.set_gear()   # adjust gear based on new speed
            self.acceleration += 1
        return self.speed

    # ------------------- Deceleration -------------------
    def get_deceleration(self):
        return self.deceleration

    def set_deceleration(self):
        if self.bike_on and self.speed > 0:
            self.speed -= 5   # decrease speed
            self.set_gear()   # adjust gear based on new speed
            self.deceleration += 1
        return self.speed
