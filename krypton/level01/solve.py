import sys

from krypton.lib.caesar import brute_force_caesar, caesar_decode

CIPHERTEXT = "YRIRY GJB CNFFJBEQ EBGGRA"
OFFSET = 13

if "--all" in sys.argv:
    for c in brute_force_caesar(CIPHERTEXT):
        print(f"{c.offset:2d}: {c.decoded}")
else:
    print(caesar_decode(CIPHERTEXT, OFFSET))
