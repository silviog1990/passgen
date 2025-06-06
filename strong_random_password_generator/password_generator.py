import secrets
import string
import random

def generate_password(
    length=16,
    use_upper=True,
    use_lower=True,
    use_digits=True,
    use_symbols=True,
    symbols="!#$%&*+-?@',./:;=^_~`|<>[](){}",
    no_similar=False,
    no_duplicate=False,
    add_word=None,
    begins_with=None
):
    base_chars = ""
    required_chars = []

    if use_upper:
        base_chars += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        base_chars += string.ascii_lowercase
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        base_chars += string.digits
        required_chars.append(secrets.choice(string.digits))
    if use_symbols and symbols:
        base_chars += symbols
        required_chars.append(secrets.choice(symbols))

    if no_similar:
        for c in 'il1Lo0O':
            base_chars = base_chars.replace(c, '')
        required_chars = [c for c in required_chars if c not in 'il1Lo0O']

    if not base_chars:
        raise ValueError("Seleziona almeno un tipo di carattere.")

    password = ""
    used_chars = set()

    if begins_with:
        password += begins_with
        used_chars.update(begins_with)

    if add_word:
        password += add_word
        used_chars.update(add_word)

    for c in required_chars:
        if no_duplicate and c in used_chars:
            continue
        password += c
        used_chars.add(c)

    while len(password) < length:
        c = secrets.choice(base_chars)
        if no_duplicate and c in used_chars:
            continue
        password += c
        used_chars.add(c)

    password = password[:length]

    start_len = 0
    if begins_with:
        start_len += len(begins_with)
    if add_word:
        start_len += len(add_word)
    if len(password) > start_len:
        middle = list(password[start_len:])
        random.SystemRandom().shuffle(middle)
        password = password[:start_len] + ''.join(middle)

    return password