class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        hh = f"{f'0{self.hours}' if self.hours < 10 else self.hours}"
        mm = f"{f'0{self.minutes}' if self.minutes < 10 else self.minutes}"
        ss = f"{f'0{self.seconds}' if self.seconds < 10 else self.seconds}"

        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()


time = Time(13, 4, 56)
print(time.next_second())


