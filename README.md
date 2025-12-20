# OverTheWire Wargames Solutions

Educational solutions for [OverTheWire](https://overthewire.org/wargames/) wargames.

## About

This repository contains structured solutions for various OverTheWire wargames.

Each solution explains the underlying concepts and techniques rather than just providing answers.

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

## How to Use

1. Navigate to the game directory (e.g., `bandit/`)
2. Read the game's README for connection details
3. Work through levels sequentially
4. Use the solutions only after attempting each level yourself

## Running Python Scripts

Some levels include automation scripts. Run them with:

```bash
uv run python path/to/solve.py
```

## Ethical Notice

These solutions are for educational purposes only.

For most games, passwords and sensitive credentials are replaced with placeholders (e.g., `<password_level_X>`). For Krypton, early “passwords” are typically non-sensitive puzzle strings and may be included as-is.

Do not:
- Share actual passwords publicly
- Use these techniques against systems you do not own
- Skip the learning process by copying solutions without understanding

The goal is to learn security concepts, not to collect flags.

## Games Covered

| Game                | Description               | Status      |
|---------------------|---------------------------|-------------|
| [Bandit](bandit/)   | Linux command line basics | Complete    |
| [Krypton](krypton/) | Cryptography              | In Progress |
| [Natas](natas/)     | Web security              | In Progress |

## License

Licensed under the MIT License. See `LICENSE`.
