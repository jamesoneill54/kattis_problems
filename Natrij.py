def time_to_seconds(time):
   hrs, mins, secs = [int(e) for e in time.strip().split(':')]
   return (hrs * 60 * 60) + (mins * 60) + secs

def seconds_to_24hr(seconds):
   mins, secs = divmod(seconds, 60)
   hrs, mins = divmod(mins, 60)
   return '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)

def time_to_explosion(time_a, time_b):
   cur_time = time_to_seconds(time_a)
   exp_time = time_to_seconds(time_b)

   if exp_time - cur_time < 0:
      # calculate time to midnight + from midnight to explosion
      # 86,400 seconds in a day
      return seconds_to_24hr((86400 - cur_time) + exp_time)

   else:
      return seconds_to_24hr(exp_time - cur_time)

import sys

times = sys.stdin.readlines()

print(time_to_explosion(times[0], times[1]))