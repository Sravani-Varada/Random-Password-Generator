import random
import string

def generate_password(length, upper, lower, digits, symbols):
    character_pool = ""
    password_chars = []

    if upper:
        character_pool += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    if lower:
        character_pool += string.ascii_lowercase
        password_chars.append(random.choice(string.ascii_lowercase))
    if digits:
        character_pool += string.digits
        password_chars.append(random.choice(string.digits))
    if symbols:
        character_pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    if not character_pool:
        return "⚠️ Please select at least one character type."

    if length < len(password_chars):
        return "⚠️ Length too short for selected options."

    while len(password_chars) < length:
        password_chars.append(random.choice(character_pool))

    random.shuffle(password_chars)
    return ''.join(password_chars)
