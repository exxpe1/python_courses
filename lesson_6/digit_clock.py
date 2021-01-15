import time
import os

def print_clock():
    os.system('cls' if os.name == 'nt' else 'clear')
    separator = ':'
    cur_time = time.localtime()
    hour_a = cur_time.tm_hour // 10
    hour_b = cur_time.tm_hour % 10
    minute_a = cur_time.tm_min // 10
    minute_b = cur_time.tm_min % 10
    second_a = cur_time.tm_sec // 10
    second_b = cur_time.tm_sec % 10
    print(hour_a, hour_b, separator, minute_a, minute_b, separator, second_a, second_b, sep='')
    time.sleep(1)

while True:
    print_clock()

if __name__ == "__main__":
    pass