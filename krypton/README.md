# Krypton

Krypton is the cryptography-focused wargame from OverTheWire.

Unlike other games, many Krypton “passwords” are **non-sensitive puzzle strings** (especially early levels), so this directory may include them in results. Still: don’t publish real credentials/tokens for anything that grants ongoing access.

## Official Resources

- [OverTheWire Krypton](https://overthewire.org/wargames/krypton/)

## Connection Information

Check the official page for current host/port. Typical usage:

```bash
ssh krypton0@<host> -p <port>
```

## Running the solvers

From the `krypton/` directory:

```bash
cd krypton
uv run level00/solve.py
uv run level01/solve.py --all
uv run level02/solve.py --all
```
