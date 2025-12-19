"""N-gram utilities shared across Krypton solvers."""

from collections import Counter


def get_ngrams(text: str, n: int) -> Counter:
    """Return a Counter of all contiguous n-grams in `text`."""
    return Counter(text[i : i + n] for i in range(len(text) - n + 1))


