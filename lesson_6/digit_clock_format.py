b_char = ' '
char = '\u2588\u2588'

digit_chars = {
    '0':[[char, char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, b_char, char],
        [char, char, char]],
    '1':[[b_char, b_char, b_char],
        [b_char, b_char, b_char],
        [char, char, b_char],
        [char, char, b_char],
        [char, char, b_char],
        [char, char, b_char]],
    '2':[[b_char, b_char, b_char],
        [b_char, b_char, b_char],
        [char, char, b_char],
        [char, char, b_char],
        [char, char, b_char],
        [char, char, b_char]],
}





print(digit_chars.values())