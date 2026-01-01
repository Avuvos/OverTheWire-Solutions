# OverTheWire Wargames Solutions

Educational solutions for [OverTheWire](https://overthewire.org/wargames/) wargames.

## About

This repository contains structured solutions for various OverTheWire wargames.

Each level has its own README that explains the underlying concepts and techniques rather than just providing answers.

**Krypton** and **Natas** feature fully automated Python solvers. Each script automatically retrieves the password for the next level.

## Repository Structure

```
├── bandit/          # Bandit wargame (Linux basics)
│   ├── README.md    # Game overview and connection info
│   └── levelXX.md   # Individual level solutions
├── krypton/         # Krypton wargame (Cryptography)
│   ├── README.md    # Game overview and how to run solvers
│   ├── lib/         # Shared crypto helpers
│   └── levelXX/     # One folder per level
│       ├── README.md
│       └── solve.py
├── natas/           # Natas wargame (Web security)
│   ├── README.md    # Game overview and how to run solvers
│   ├── lib/         # Shared session utility
│   └── levelXX/     # One folder per level
│       ├── README.md
│       └── solve.py
└── ...              # Additional games
```

## Running the Solvers

The **Krypton** and **Natas** solvers are fully automatic. Simply run the script and it will output the password for the next level:

```bash
# Krypton (Cryptography)
uv run krypton/level00/solve.py
uv run krypton/level01/solve.py

# Natas (Web Security)
uv run natas/level00/solve.py
uv run natas/level11/solve.py
```

Each game directory contains its own README with detailed setup instructions and connection information.

## Ethical Notice

These solutions are for educational purposes only.

For most games, passwords and sensitive credentials are replaced with placeholders (e.g., `<password_level_X>`). For Krypton, early “passwords” are typically non-sensitive puzzle strings and may be included as-is.

Do not:
- Share actual passwords publicly
- Use these techniques against systems you do not own
- Skip the learning process by copying solutions without understanding

The goal is to learn security concepts, not to collect flags.

## Games Covered

| Game                | Description               | Progress    |
|---------------------|---------------------------|-------------|
| [Bandit](bandit/)   | Linux command line basics | **34 / 34** |
| [Krypton](krypton/) | Cryptography              | **6 / 7**   |
| [Natas](natas/)     | Web security              | **15 / 34** |

## License

Licensed under the MIT License. See `LICENSE`.
