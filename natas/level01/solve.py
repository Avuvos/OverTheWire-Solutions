import re

from natas.lib import natas_session

session, url = natas_session(1)

response = session.get(url)
regex = r"<!--The password for natas2 is (.*) -->"
print(re.findall(regex, response.text)[0])
