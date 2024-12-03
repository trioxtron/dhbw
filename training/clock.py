class Clock:
    def __init__(self, hours, minutes, color, material):
        if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
            raise ValueError("Invalid time")
        self.hours = hours
        self.minutes = minutes
        self.color = color
        self.material = material
    
    def increase(self, amount = 1):
        self.minutes += amount
        if self.minutes >= 60:
            hoursteps = self.minutes//60
            self.minutes = self.minutes%60
            self.hours += hoursteps
            if self.hours >= 24:
                self.hours = self.hours%24

    def decrease(self, amount = 1):
        self.minutes -= amount
        if self.minutes < 0:
            hoursteps = self.minutes//60
            self.minutes = 60 - abs(self.minutes)%60
            self.hours += hoursteps
            if self.hours < 0:
                self.hours = 24 - abs(self.hours)%24

    def timeChange(self, direction):
        if direction == "increase":
            self.increase(60)
        elif direction == "decrease":
            self.decrease(60)
        else:
            raise ValueError("Invalid direction")

    def getTime(self):
        return f"{self.hours}:{self.minutes:02d}"


if __name__ == '__main__':
    clock = Clock(12, 30, "red", "plastic")
    print(clock.getTime())
    clock.timeChange("increase")
    print(clock.getTime())
    clock.timeChange("decrease")
    print(clock.getTime())
