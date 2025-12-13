import base64

ENCODED = "S1JZUFRPTklTR1JFQVQ="


def main() -> None:
    print(base64.b64decode(ENCODED).decode())


if __name__ == "__main__":
    main()
