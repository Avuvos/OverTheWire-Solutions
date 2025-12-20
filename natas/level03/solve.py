import re

from natas.lib import natas_session

session, url = natas_session(3)

response = session.get(url + "/s3cr3t/users.txt")

regex = r"natas4:(.*)"
print(re.findall(regex, response.text)[0])

