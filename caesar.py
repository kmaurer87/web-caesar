def alphabet_position(letter):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    cap_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter.islower():
        pos = alpha.index(letter)
    else:
        pos = cap_alpha.index(letter)
    return pos

def rotate_character(char, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    pos = alphabet_position(char)
    new_pos = pos + rot
    if new_pos <= 25:
        new_char = alpha[new_pos]
    else:
        new_char = alpha[new_pos % 26]
    return new_char

def encrypt(text, rot):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                lower_char = i.lower()
                char = rotate_character(lower_char, rot)
                cap_char = char.upper()
                encrypted_string = encrypted_string + cap_char
            else:
                char = rotate_character(i, rot)
                encrypted_string = encrypted_string + char
        else:
            encrypted_string = encrypted_string + i
    return encrypted_string
