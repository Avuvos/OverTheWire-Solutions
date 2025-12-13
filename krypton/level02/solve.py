import sys

from krypton.lib.caesar import brute_force_caesar, caesar_decode

CIPHERTEXT = "OMQEMDUEQMEK"
OFFSET = 12

if "--all" in sys.argv:
    for offset, decoded in brute_force_caesar(CIPHERTEXT):
        print(f"{offset:2d}: {decoded}")
else:
    print(caesar_decode(CIPHERTEXT, OFFSET))
