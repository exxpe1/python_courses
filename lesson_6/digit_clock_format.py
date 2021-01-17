b_char = '  '
char = '\u2588\u2588'
color = ''
color_a = '\033[37m'
color_b = '\033[31m'

digit_chars = {
    0:  [[char, char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, char, char]],

    1:  [[b_char, b_char, char],
        [b_char, char, char],
        [char, b_char, char],
        [b_char, b_char, char],
        [b_char, b_char, char],
        [b_char, b_char, char]],

    2:  [[char, char, char],
        [b_char, b_char, char],
        [b_char, char, char],
        [char, char, b_char],
        [char, b_char, b_char],
        [char, char, char]],

    3:  [[char, char, char],
        [b_char, b_char, char],
        [char, char, char],
        [char, char, char],
        [b_char, b_char, char],
        [char, char, char]],

    4:  [[char, b_char, char],
        [char, b_char, char],
        [char, char, char],
        [char, char, char],
        [b_char, b_char, char],
        [b_char, b_char, char]],

    5:  [[char, char, char],
        [char, b_char, b_char],
        [char, char, char],
        [char, char, char],
        [b_char, b_char, char],
        [char, char, char]],

    6:  [[char, char, char],
        [char, b_char, b_char],
        [char, b_char, b_char],
        [char, char, char],
        [char, b_char, char],
        [char, char, char]],

    7:  [[char, char, char],
        [b_char, b_char, char],
        [b_char, char, char],
        [char, char, b_char],
        [char, b_char, b_char],
        [char, b_char, b_char]],

    8:  [[char, char, char],
        [char, b_char, char],
        [char, char, char],
        [char, char, char],
        [char, b_char, char],
        [char, char, char]],

    9:  [[char, char, char],
        [char, b_char, char],
        [char, char, char],
        [b_char, b_char, char],
        [b_char, b_char, char],
        [char, char, char]],

    ':':[[b_char, b_char, b_char],
        [b_char, char, b_char],
        [b_char, b_char, b_char],
        [b_char, b_char, b_char],
        [b_char, char, b_char],
        [b_char, b_char, b_char]],

    '-': [[b_char, b_char, b_char],
        [b_char, b_char, b_char],
        [b_char, char, b_char],
        [b_char, char, b_char],
        [b_char, b_char, b_char],
        [b_char, b_char, b_char]]
}



def char_in_str(digit, scale):
    output = []

    for symbol in digit_chars[digit]:
        line = ''

        for item in symbol:
            line += item * scale
        for item in range(scale):
            output.append(line)

    return output


if __name__ == "__main__":
    pass