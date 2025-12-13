import sys

from krypton.lib.caesar import brute_force_caesar, caesar_decode

CIPHERTEXT = "YRIRY GJB CNFFJBEQ EBGGRA"
OFFSET = 13


def main() -> None:
    if "--all" in sys.argv:
        for offset, decoded in brute_force_caesar(CIPHERTEXT):
            print(f"{offset:2d}: {decoded}")
    else:
        print(caesar_decode(CIPHERTEXT, OFFSET))


if __name__ == "__main__":
    main()
