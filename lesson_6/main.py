import os
import time
import digit_clock
import digit_clock_format

toogle = False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if toogle == False:
        sep = '-'
        digit_clock_format.color = digit_clock_format.color_a
    else:
        sep = ':'
        digit_clock_format.color = digit_clock_format.color_b
    digit_clock.print_clock(1, sep)
    time.sleep(1)
    toogle = not toogle
