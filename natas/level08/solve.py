import base64
import re

from bs4 import BeautifulSoup

from natas.lib import natas_session

session, url = natas_session(8)

response = session.get(url + "/index-source.html")

text = response.text.replace("<br />", "\n").replace("&nbsp;", " ")
soup = BeautifulSoup(text, "html.parser")

secret = re.findall(r'\$encodedSecret *= *"([^"]+)" *;', soup.get_text())[0]

# Reverse: bin2hex(strrev(base64_encode($secret)))
decoded_secret = base64.b64decode(bytes.fromhex(secret)[::-1]).decode()

# Submit the secret to get the password
response = session.post(url, data={"secret": decoded_secret, "submit": "submit"})

regex = r"Access granted. The password for natas9 is (.*)"
print(re.findall(regex, response.text)[0])
