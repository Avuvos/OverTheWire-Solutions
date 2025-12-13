import string
from dataclasses import dataclass


ALPHABET_UPPER = string.ascii_uppercase
ALPHABET_LOWER = string.ascii_lowercase


def caesar_decode(text: str, offset: int) -> str:
    """Decode a Caesar cipher by shifting letters backward by `offset`.

    Non-letters are preserved. Case is preserved.
    """
    offset %= 26
    out: list[str] = []
    for ch in text:
        if ch in ALPHABET_UPPER:
            idx = (ord(ch) - ord("A") - offset) % 26
            out.append(chr(ord("A") + idx))
        elif ch in ALPHABET_LOWER:
            idx = (ord(ch) - ord("a") - offset) % 26
            out.append(chr(ord("a") + idx))
        else:
            out.append(ch)
    return "".join(out)


@dataclass(frozen=True)
class CaesarCandidate:
    offset: int
    decoded: str


def brute_force_caesar(ciphertext: str) -> list[CaesarCandidate]:
    """Return all 26 Caesar decode candidates (offset 0..25)."""
    return [CaesarCandidate(offset=o, decoded=caesar_decode(ciphertext, o)) for o in range(26)]


