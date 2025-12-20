import sys
from pathlib import Path

from krypton.lib.vigenere import decrypt_vigenere

CIPHERTEXT = "BELOSZ"
KEY_LENGTH = 9  # discovered through brute-force


def load_ciphertexts() -> list[str]:
    """Load all `found*.txt` ciphertext samples with whitespace removed."""
    cipher_files = sorted(Path("level05/cipher_texts").glob("found*.txt"))
    return [p.read_text().replace("\n", "").replace(" ", "") for p in cipher_files]


def main() -> None:
    corpus = load_ciphertexts()
    show_all = "--all" in sys.argv

    for key_length in range(1, 12):
        for key, decoded in decrypt_vigenere(CIPHERTEXT, corpus, key_length, top_n=1, show_all=True):
            if show_all:
                print(f"len={key_length} key={key} -> {decoded}")
            elif key_length == KEY_LENGTH:
                print(decoded)


if __name__ == "__main__":
    main()
