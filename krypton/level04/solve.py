from pathlib import Path
from itertools import product
import string
import sys

from krypton.lib.ngrams import get_ngrams

CIPHERTEXT = "HCIKVRJOX"
KEY_LENGTH = 6

MOST_COMMON_ENGLISH_LETTER = "E"

def load_ciphertexts() -> list[str]:
    """Load all `found*.txt` ciphertext samples with whitespace removed."""
    cipher_files = sorted(Path("level04/cipher_texts").glob("found*.txt"))
    return [p.read_text().replace("\n", "").replace(" ", "") for p in cipher_files]


def build_position_streams(ciphertexts: list[str]) -> list[str]:
    """Build one stream per key position by slicing each ciphertext with stride KEY_LENGTH."""
    return ["".join(ct[i::KEY_LENGTH] for ct in ciphertexts) for i in range(KEY_LENGTH)]


def candidate_key_letters(position_corpus: str, top_n: int = 2) -> list[str]:
    """Return candidate key letters for a position by assuming top cipher letters map to 'E'."""
    most_common_cipher_letters = "".join(ch for ch, _ in get_ngrams(position_corpus, 1).most_common())[:top_n]
    return [
        chr(ord("A") + ((ord(ch) - ord(MOST_COMMON_ENGLISH_LETTER)) % 26))
        for ch in most_common_cipher_letters
    ]


def build_key_mappings(key: tuple[str, ...]) -> list[dict[str, str]]:
    """Build KEY_LENGTH Caesar decode tables (cipher A–Z -> plain A–Z), one per key position."""
    mappings: list[dict[str, str]] = [{} for _ in range(KEY_LENGTH)]
    for i, key_ch in enumerate(key):
        offset = ord(key_ch) - ord("A")
        for ch in string.ascii_uppercase:
            mappings[i][ch] = chr(ord("A") + ((ord(ch) - ord("A") - offset) % 26))
    return mappings


def decode_repeated_key(ciphertext: str, mappings: list[dict[str, str]]) -> str:
    """Decode `ciphertext` with repeated-key mappings."""
    result = ""
    for i, ch in enumerate(ciphertext):
        result += mappings[i % KEY_LENGTH].get(ch, ch)
    return result

def main() -> None:
    ciphertexts = load_ciphertexts()
    position_streams = build_position_streams(ciphertexts)

    candidates_per_pos = [candidate_key_letters(stream) for stream in position_streams]

    show_all = "--all" in sys.argv

    for key in product(*candidates_per_pos):
        mappings = build_key_mappings(key)
        decoded = decode_repeated_key(CIPHERTEXT, mappings)

        if show_all:
            print(key)
            print(decoded)
        else:
            print(decoded)
            break

    

if __name__ == "__main__":
    main()