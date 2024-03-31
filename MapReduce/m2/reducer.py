#!/usr/bin/env python3
import sys

def main():
    """Groups words by paragraph ID and displays paragraph lines with hashed words."""
    current_paragraph_id = None
    paragraph_lines = []

    for line in sys.stdin:
        if line.startswith("ID"):
            # Extract paragraph ID
            current_paragraph_id = line
        else:
            # Process words in the paragraph
            words = line.strip().split()
            for word in words:
                hashed_word = word.strip()  # Assuming format "paragraph_id\thashed_word"
                print(f"{current_paragraph_id}\t{hashed_word}")

if __name__ == "__main__":
    main()

