import re

from natas.lib import natas_session

session, url = natas_session(2)

response = session.get(url + "/files/users.txt")

regex = r"natas3:(.*)"
print(re.findall(regex, response.text)[0])
