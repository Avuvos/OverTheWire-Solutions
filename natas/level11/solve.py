import base64
import json
import re

from natas.lib import natas_session


def xor(left: bytes, right: bytes) -> bytes:
    """XOR two byte sequences together."""
    return bytes(x ^ y for x, y in zip(left, right, strict=False))


def find_repeating_key(full_key: bytes) -> bytes:
    """Find the smallest repeating pattern in a byte sequence."""
    for key_size in range(1, len(full_key)):
        repeated = (full_key[:key_size] * (len(full_key) // key_size + 1))[: len(full_key)]
        if full_key == repeated:
            return full_key[:key_size]
    return full_key


def php_json_encode(data: dict) -> bytes:
    """Mimic the behavior of the PHP json_encode function."""
    return json.dumps(data, separators=(",", ":")).encode()


session, url = natas_session(11)
response = session.get(url)

# Extract the original cookie (base64 encoded ciphertext) and decode it
cookie_b64 = response.cookies.get("data").replace("%3D", "=")
original_cookie_ciphertext = base64.b64decode(cookie_b64)

# Determine the known plaintext (default data that was encrypted)
default_data = {"showpassword": "no", "bgcolor": "#ffffff"}
default_plaintext = php_json_encode(default_data)

# Extract the XOR key by XORing known plaintext with ciphertext
extracted_key = xor(default_plaintext, original_cookie_ciphertext)
key = find_repeating_key(extracted_key)

# Create the desired plaintext payload
wanted_data = {"showpassword": "yes", "bgcolor": "#ffffff"}
wanted_plaintext = php_json_encode(wanted_data)

# Encrypt the desired plaintext using the recovered key
key_length = (len(wanted_plaintext) + len(key) - 1) // len(key)
key_repeated = (key * key_length)[: len(wanted_plaintext)]
cookie_ciphertext = xor(wanted_plaintext, key_repeated)

# Base64 encode the ciphertext for the cookie
cookie_ciphertext_b64 = base64.b64encode(cookie_ciphertext).decode()

session.cookies.clear()
response = session.get(url, cookies={"data": cookie_ciphertext_b64})

print(re.findall(r"The password for natas12 is (\w+)", response.text)[0])
