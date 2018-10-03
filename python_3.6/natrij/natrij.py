# Kattis problem link: https://open.kattis.com/problems/natrij
import sys


class Time:

    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, given_time):
        self.hours = int(given_time.split(":")[0])
        self.minutes = int(given_time.split(":")[1])
        self.seconds = int(given_time.split(":")[2])

    def convert_to_seconds(self):
        return self.seconds + self.minutes * 60 + self.hours * 60 ** 2

    def time_between(self, later_time):
        time_between = later_time.convert_to_seconds() - self.convert_to_seconds()
        if time_between < 0:
            seconds_between = 86400 + time_between
            minutes, seconds = divmod(seconds_between, 60)
            hours, minutes = divmod(minutes, 60)
        elif time_between == 0:
            hours, minutes, seconds = 24, 0, 0
        else:
            minutes, seconds = divmod(time_between, 60)
            hours, minutes = divmod(minutes, 60)
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)


def main():
    current_time, time_of_explosion = [Time(time.strip()) for time in sys.stdin.readlines()]
    print(current_time.time_between(time_of_explosion))


if __name__ == "__main__":
    main()
