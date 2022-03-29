class ClockTime:
    hours = ""
    minutes = ""
    seconds = ""

    def set_hours(self, hours):
        if int(hours) < 10:
            self.hours += "0"

        self.hours += hours

    def set_minutes(self, minutes):
        if int(minutes) < 10:
            self.minutes += "0"

        self.minutes += minutes

    def set_second(self, seconds):
        if int(seconds) < 10:
            self.seconds += "0"

        self.seconds += seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def show_time(self):
        print(f'Time now is {self.hours}:{self.minutes}:{self.seconds}')


def main():
    clock_time = ClockTime()

    clock_time.set_hours(input("Enter hours: "))
    clock_time.set_minutes(input("Enter minutes: "))
    clock_time.set_second(input("Enter seconds: "))
    print()

    clock_time.show_time()


if __name__ == "__main__":
    main()
