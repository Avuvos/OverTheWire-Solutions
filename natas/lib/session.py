"""Session utilities for Natas challenges."""

import os
from pathlib import Path

import requests
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
    """Create an authenticated session for a natas level.

    Args:
        level: The natas level number (0-33).

    Returns:
        A tuple of (session, url) ready to use.

    Example:
        session, url = natas_session(5)
        response = session.get(url)
    """
    username = f"natas{level}"
    password = get_password(level)
    url = BASE_URL.format(level=level)

    session = requests.Session()
    session.auth = (username, password)

    return session, url
