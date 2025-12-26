"""Session utilities for Natas challenges."""

import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".natas.env")


BASE_URL = "http://natas{level}.natas.labs.overthewire.org"


def get_password(level: int) -> str:
    """Get password for a natas level from environment variable."""
    env_var = f"NATAS{level}"
    password = os.getenv(env_var)

    if password is None:
        msg = f"Environment variable {env_var} not set. Solve level {level - 1} first!"
        raise ValueError(msg)

    return password


def natas_session(level: int) -> tuple[requests.Session, str]:
    """Create an authenticated session and return (session, url) for the given level."""
    username = f"natas{level}"
    password = get_password(level)
    url = BASE_URL.format(level=level)

    session = requests.Session()
    session.auth = (username, password)

    return session, url


def get_source_code(session: requests.Session, base_url: str, source_code_index: str = "index-source.html") -> str:
    """Fetch and return cleaned source code from the specified endpoint."""
    url = f"{base_url}/{source_code_index}"
    response = session.get(url)
    text = response.text.replace("<br />", "\n").replace("&nbsp;", " ")
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()
