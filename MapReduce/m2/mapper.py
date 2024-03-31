#!/usr/bin/python3

import sys

def simple_hash(word):
 """Calculates a simple hash value for a word."""
 hash_value = 0
 for char in word:
   hash_value += ord(char)
 return hash_value % 50000 # Adjust modulo based on desired range

def main():
 """Processes lines, emitting paragraph ID and hashed words with counts."""
 current_paragraph_id = None

 for line in sys.stdin:
   line = line.strip() # Remove leading/trailing whitespace

   if line.startswith("no "):
     # Extract paragraph ID
     current_paragraph_id = line[2]
     #print(f"{current_paragraph_id}\n") # Emit paragraph ID
   else:
     # Process words in the paragraph
     words = line.strip().split('\t')
     for word in words:
       hashed_word = f"{simple_hash(word)}"
       print(f"{hashed_word}\t1")

if __name__ == "__main__":
 main()

