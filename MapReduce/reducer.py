#!/usr/bin/env python3

import sys
from collections import Counter

def main():
  """
  This reducer reads key-value pairs from standard input,
  aggregates word counts for each unique word,
  and emits the word and its total count, handling potential exceptions.
  """
  word_counts = Counter()
  try:
    for line in sys.stdin:
      
      word, count = line.strip().split('\t')
      # Convert count to integer 
      count = int(count)
     
      word_counts[word] += count
  except Exception as e:
    # Log the error and continue processing other entries (optional)
    sys.stderr.write(f"Error processing line: {line.strip()}. Exception: {str(e)}\n")

  
  for word, count in word_counts.items():
    sys.stdout.write(f"{word}\t{count}\n")

if __name__ == "__main__":
  main()

