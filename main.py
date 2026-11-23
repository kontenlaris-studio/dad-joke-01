#!/usr/bin/env python3
"""Dad Joke Showdown — writes one dad joke to /output/entry.txt.

The joke: a setup-and-punchline dad joke about embracing your
mistakes — the groan lands harder than a bare pun, because the wife
is the punchline. Switched from the facial-hair pun: a two-beat joke
beats a one-beat pun in a pairwise pick.
"""
import os

JOKE = "I told my wife she should embrace her mistakes. She hugged me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
