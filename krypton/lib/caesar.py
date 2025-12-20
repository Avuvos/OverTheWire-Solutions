import string

ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_LOWER = string.ascii_lowercase


def caesar_decode(text: str, offset: int) -> str:
    """Decode a Caesar cipher by shifting letters backward by `offset`."""
    result: list[str] = []
    for ch in text:
        if ch in ALPHABET_UPPER:
            idx = (ord(ch) - ord("A") - offset) % 26
            result.append(chr(ord("A") + idx))
        elif ch in ALPHABET_LOWER:
            idx = (ord(ch) - ord("a") - offset) % 26
            result.append(chr(ord("a") + idx))
        else:
            result.append(ch)
    return "".join(result)


def brute_force_caesar(ciphertext: str) -> list[tuple[int, str]]:
    """Return all 26 Caesar decode candidates (offset 0..25)."""
    return [(offset, caesar_decode(ciphertext, offset)) for offset in range(26)]
