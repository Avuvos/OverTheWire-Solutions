import base64
import re

from natas.lib import get_source_code, natas_session

session, url = natas_session(8)

source_code = get_source_code(session, url)
secret = re.findall(r'\$encodedSecret *= *"([^"]+)" *;', source_code)[0]

# Reverse: bin2hex(strrev(base64_encode($secret)))
decoded_secret = base64.b64decode(bytes.fromhex(secret)[::-1]).decode()

# Submit the secret to get the password
response = session.post(url, data={"secret": decoded_secret, "submit": "submit"})

regex = r"Access granted. The password for natas9 is (.*)"
print(re.findall(regex, response.text)[0])
