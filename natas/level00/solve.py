import re

from natas.lib import natas_session

session, url = natas_session(0)

response = session.get(url)
regex = r"<!--The password for natas1 is (.*) -->"
print(re.findall(regex, response.text)[0])
