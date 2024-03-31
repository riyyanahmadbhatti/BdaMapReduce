#!/usr/bin/env python3



import sys

def main():
    
    for line in sys.stdin:
        
        para, word, idf = line.strip().split('\t')
        idf = float(idf)

        
        print(f"{word}\t{para}\t{idf}")

if __name__ == "__main__":
    main()


