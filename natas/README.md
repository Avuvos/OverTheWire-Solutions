# Natas

Natas is the web security wargame from OverTheWire, teaching server-side security basics.

Each level involves finding a vulnerability in a web application to retrieve the password for the next level. Passwords are stored in environment variables and loaded via the shared session utility.

## Level Overview

| Level | Key Concept |
|-------|-------------|
| 0     | View page source |
| 1     | View source (right-click disabled) |
| 2     | Directory listing / exposed files |
| 3     | Robots.txt / hidden directories |
| 4     | HTTP Referer header spoofing |

## Shared Library (`lib/`)

Common utilities are extracted into `lib/` to avoid duplication across levels:

| Module | Purpose |
|--------|---------|
| [`session.py`](lib/session.py) | Authenticated session setup |

Passwords are loaded from environment variables (`NATAS0`, `NATAS1`, etc.) via a `.natas.env` file.

## Setup

From the `natas/` directory:

```bash
cd natas
cp lib/.natas.env.example lib/.natas.env
```

Then fill in passwords as you solve each level.

## Running the Solvers

From the `natas/` directory:

```bash
cd natas
uv run levelXX/solve.py
```

## Official Resources

- [OverTheWire Natas](https://overthewire.org/wargames/natas/)

## Connection Information

Each level is accessed via HTTP at:

```
http://natasX.natas.labs.overthewire.org
```

Authentication uses HTTP Basic Auth with username `natasX` and the corresponding password.
