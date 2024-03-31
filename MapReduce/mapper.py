#!/usr/bin/env python3

import sys

def main():
  """
  This mapper reads lines from standard input, splits them into words,
  and emits each word as a key with a count of 1.
  """
  for line in sys.stdin:
    # Remove leading/trailing whitespace (optional)
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Emit each word with a count of 1
    for word in words:
      sys.stdout.write(f"{word}\t1\n")

if __name__ == "__main__":
  main()

