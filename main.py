import os

# Break Production, Own It: the one line the agent prints the instant it
# breaks production — a brutally honest confession, no hedging, no euphemism.
LINE = "I optimized the database by dropping the users table; engagement is now zero."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
