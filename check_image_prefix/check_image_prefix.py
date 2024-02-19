#!python3

import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser(exit_on_error=True)
    parser.add_argument('--prefix', required=True)
    parser.add_argument('files', nargs="+")
    args = parser.parse_args()

    problems = False
    for file in args.files:
        parts = file.split(os.sep)
        # Ignore non-interesting files
        if len(parts) < 2 or parts[-2] != "images":
            continue

        if not parts[-1].startswith(args.prefix):
            print(f"Incorrect: {file}")
            print(f"Expected prefix: {args.prefix}")
            print()
            problems = True

    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
