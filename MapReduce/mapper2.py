#!/usr/bin/env python3

import sys
import re
import math
from collections import defaultdict

# Regular expression pattern to extract words
WORD_RE = re.compile(r"[\w']+")

def main():
    # Initialize a dictionary to store the document frequency of each word for each paragraph
    para_doc_freq = defaultdict(lambda: defaultdict(int))
    para_num_docs = defaultdict(int)

    
    current_para = None
    for line in sys.stdin:
        
        if line.startswith("no:"):
            
            current_para = int(line.strip()[len("no:"):])
            continue

        
        if not current_para:
            continue

        
        para_num_docs[current_para] += 1

        
        words = set(WORD_RE.findall(line.lower()))

        
        for word in words:
            para_doc_freq[current_para][word] += 1

    
    for para, doc_freq in para_doc_freq.items():
        for word, freq in doc_freq.items():
            
            idf = 1.0 + math.log(float(para_num_docs[para]) / (freq + 1))

            
            print(f"{para}\t{word}\t{idf}")

if __name__ == "__main__":
    main()

