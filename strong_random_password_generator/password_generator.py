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
    """
    Generate a strong random password based on the provided options.

    Args:
        length (int): Desired password length.
        use_upper (bool): Include uppercase letters.
        use_lower (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_symbols (bool): Include symbols.
        symbols (str): String of allowed symbols.
        no_similar (bool): Exclude similar-looking characters.
        no_duplicate (bool): Exclude duplicate characters.
        add_word (str or None): Word to include in the password.
        begins_with (str or None): Prefix for the password.

    Returns:
        str: Generated password.

    Raises:
        ValueError: If no character set is selected.
    """
    base_chars = ""
    required_chars = []

    # Build the character set and ensure at least one character from each selected type
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

    # Optionally remove similar-looking characters
    if no_similar:
        for c in 'il1Lo0O':
            base_chars = base_chars.replace(c, '')
        required_chars = [c for c in required_chars if c not in 'il1Lo0O']

    if not base_chars:
        raise ValueError("Seleziona almeno un tipo di carattere.")

    password = ""
    used_chars = set()

    # Add prefix if specified
    if begins_with:
        password += begins_with
        used_chars.update(begins_with)

    # Add custom word if specified
    if add_word:
        password += add_word
        used_chars.update(add_word)

    # Ensure at least one character from each required type is present
    for c in required_chars:
        if no_duplicate and c in used_chars:
            continue
        password += c
        used_chars.add(c)

    # Fill the rest of the password
    while len(password) < length:
        c = secrets.choice(base_chars)
        if no_duplicate and c in used_chars:
            continue
        password += c
        used_chars.add(c)

    # Truncate to desired length if necessary
    password = password[:length]

    # Shuffle the part of the password that is not prefix/word to avoid predictability
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