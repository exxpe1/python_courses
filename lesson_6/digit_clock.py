import time
import os
import digit_clock_format



def print_clock(scale = 1, sep = ':'):
    
    cur_time = time.localtime()
    hour_a = digit_clock_format.char_in_str(cur_time.tm_hour // 10, scale)
    hour_b = digit_clock_format.char_in_str(cur_time.tm_hour % 10, scale)
    minute_a = digit_clock_format.char_in_str(cur_time.tm_min // 10, scale)
    minute_b = digit_clock_format.char_in_str(cur_time.tm_min % 10, scale)
    second_a = digit_clock_format.char_in_str(cur_time.tm_sec // 10, scale)
    second_b = digit_clock_format.char_in_str(cur_time.tm_sec % 10, scale)
    
    if sep not in digit_clock_format.digit_chars:
        sep = ':'
    separator = digit_clock_format.char_in_str(sep, scale)

    for item in range(len(hour_a)):
        print(digit_clock_format.color + hour_a[item] + '  ' +  hour_b[item] + separator[item] +
        minute_a[item] + '  ' + minute_b[item] + separator[item] +
        second_a[item] + '  ' + second_b[item])

if __name__ == "__main__":
    pass