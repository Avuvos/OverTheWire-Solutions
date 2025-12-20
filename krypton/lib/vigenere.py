"""Vigenère / repeated-key cipher utilities shared across Krypton solvers."""

import string
from collections.abc import Generator
from itertools import product

from krypton.lib.ngrams import get_ngrams

MOST_COMMON_ENGLISH_LETTER = "E"


def build_position_streams(corpus: list[str], key_length: int) -> list[str]:
    """Build one stream per key position by slicing each corpus text with stride key_length."""
    return ["".join(text[i::key_length] for text in corpus) for i in range(key_length)]


def candidate_key_letters(position_corpus: str, top_n: int) -> list[str]:
    """Return candidate key letters for a position by assuming top cipher letters map to 'E'."""
    most_common_cipher_letters = "".join(ch for ch, _ in get_ngrams(position_corpus, 1).most_common())[:top_n]
    return [chr(ord("A") + ((ord(ch) - ord(MOST_COMMON_ENGLISH_LETTER)) % 26)) for ch in most_common_cipher_letters]


def build_key_mappings(key: tuple[str, ...]) -> list[dict[str, str]]:
    """Build Caesar decode tables (cipher A-Z -> plain A-Z), one per key position."""
    mappings: list[dict[str, str]] = [{} for _ in range(len(key))]
    for i, key_ch in enumerate(key):
        offset = ord(key_ch) - ord("A")
        for ch in string.ascii_uppercase:
            mappings[i][ch] = chr(ord("A") + ((ord(ch) - ord("A") - offset) % 26))
    return mappings


def decode_with_key(ciphertext: str, mappings: list[dict[str, str]]) -> str:
    """Decode `ciphertext` with repeated-key mappings."""
    key_length = len(mappings)
    result = ""
    for i, ch in enumerate(ciphertext):
        result += mappings[i % key_length].get(ch, ch)
    return result


def decrypt_vigenere(
    ciphertext: str,
    corpus: list[str],
    key_length: int,
    top_n: int,
    show_all: bool = False,
) -> Generator[tuple[tuple[str, ...], str], None, None]:
    """Decrypt a Vigenère cipher by frequency analysis.

    Args:
        ciphertext: The ciphertext to decrypt.
        corpus: Additional ciphertexts for frequency analysis (encrypted with the same key).
        key_length: The known/guessed key length.
        top_n: Number of top candidates per position to try.
        show_all: If False, yield only the first result; if True, yield all combinations.

    Yields:
        Tuples of (key, decoded_text) for each candidate.
    """
    position_streams = build_position_streams(corpus, key_length)
    candidates_per_pos = [candidate_key_letters(stream, top_n) for stream in position_streams]

    for key in product(*candidates_per_pos):
        mappings = build_key_mappings(key)
        decoded = decode_with_key(ciphertext, mappings)
        yield key, decoded
        if not show_all:
            return
