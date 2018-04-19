def user_input_is_valid(cl_args):
    if len(cl_args) != 2:
        return False
    elif cl_args[1].isdigit() == False:
        return False
    else:
        return True

def alphabet_position(letter):
    if letter.isupper():
        position = ord(letter) - 65
        return position
    else:
        position = ord(letter) - 97
        return position


def rotate_character(char, rot):
    if char.isupper():
        rot_char = chr( ( ( alphabet_position(char) + rot ) % 26 ) + 65 )
        return rot_char
    else:
        rot_char = chr( ( ( alphabet_position(char) + rot ) % 26 ) + 97 )
        return rot_char


def encrypt(text, rot):
    encrypted = ""
    for char in text:
        if char.isalpha():
            encrypted = encrypted + rotate_character(char, rot)
        else:
            encrypted = encrypted + char
    return encrypted
