from collections import Counter
from pathlib import Path

CIPHERTEXT = "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"

ENGLISH_FREQ = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
ENGLISH_BIGRAMS = ["TH", "HE", "IN", "ER", "AN", "RE", "ON", "ES", "EL", "FO", "PL"]
ENGLISH_TRIGRAMS = ["THE", "AND"]


def get_ngrams(text: str, n: int) -> Counter:
    return Counter(text[i:i+n] for i in range(len(text) - n + 1))


def decode(text: str, key_mapping: dict[str, str]) -> str:
    return "".join(key_mapping.get(ch, ch) for ch in text)


def matches_pattern(cipher_bigram: str, english_bigram: str, key_mapping: dict[str, str]) -> bool:
    """Check if cipher bigram could map to english bigram given existing mappings."""
    for cipher_ch, english_ch in zip(cipher_bigram, english_bigram):
        known_mapping = key_mapping.get(cipher_ch)
        if known_mapping is not None and known_mapping != english_ch:
            return False
    return True


def apply_bigram_mappings(key_mapping: dict[str, str], cipher_bigrams: list[str]) -> None:
    """Try to map cipher bigrams to common English bigrams."""
    used_english = set(key_mapping.values())

    for cipher_bigram in cipher_bigrams:
        for english_bigram in ENGLISH_BIGRAMS:
            if not matches_pattern(cipher_bigram, english_bigram, key_mapping):
                continue

            for cipher_ch, english_ch in zip(cipher_bigram, english_bigram):
                if cipher_ch in key_mapping or english_ch in used_english:
                    continue
                key_mapping[cipher_ch] = english_ch
                used_english.add(english_ch)


def main() -> None:
    corpus = "".join(
        Path(f"level03/cipher_texts/found{i}.txt").read_text().replace("\n", "").replace(" ", "")
        for i in range(1, 4)
    )

    cipher_freq_order = "".join(ch for ch, _ in get_ngrams(corpus, 1).most_common())
    cipher_trigrams = [tg for tg, _ in get_ngrams(corpus, 3).most_common(2)]
    cipher_bigrams = [bg for bg, _ in get_ngrams(corpus, 2).most_common(20)]

    key_mapping = {} # Map each cipher letter to an English letter

    # Trigrams
    for cipher_tg, english_tg in zip(cipher_trigrams, ENGLISH_TRIGRAMS):
        key_mapping.update(zip(cipher_tg, english_tg))

    # Bigrams
    apply_bigram_mappings(key_mapping, cipher_bigrams)

    # Most frequent letters
    used = set(key_mapping.values())
    for c, e in zip(cipher_freq_order, ENGLISH_FREQ):
        if c not in key_mapping and e not in used:
            key_mapping[c] = e
            used.add(e)

    # Manual fixes for remaining ambiguous letters
    key_mapping.update({
        'K': 'W',
        'Y': 'P',
        'A': 'B',
        'I': 'V',
    })

    print(decode(CIPHERTEXT, key_mapping))


if __name__ == "__main__":
    main()
