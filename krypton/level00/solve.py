import base64


def main() -> None:
    encoded = "S1JZUFRPTklTR1JFQVQ="
    decoded = base64.b64decode(encoded).decode("utf-8")
    print(decoded)


if __name__ == "__main__":
    main()


