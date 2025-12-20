import sys
from pathlib import Path

from krypton.lib.vigenere import decrypt_vigenere

CIPHERTEXT = "HCIKVRJOX"
KEY_LENGTH = 6


def load_ciphertexts() -> list[str]:
    """Load all `found*.txt` ciphertext samples with whitespace removed."""
    cipher_files = sorted(Path("level04/cipher_texts").glob("found*.txt"))
    return [p.read_text().replace("\n", "").replace(" ", "") for p in cipher_files]


def main() -> None:
    corpus = load_ciphertexts()
    show_all = "--all" in sys.argv

    for key, decoded in decrypt_vigenere(CIPHERTEXT, corpus, KEY_LENGTH, top_n=2, show_all=show_all):
        if show_all:
            print(key)
        print(decoded)


if __name__ == "__main__":
    main()
