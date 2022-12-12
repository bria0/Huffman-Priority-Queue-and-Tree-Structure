'''

Created on Dec. 9, 2022

@author: Brianna Nguyen
Assignment: Huffman Priority Queue and Tree Structure Encoding
Date: December 11th, 2022
Description: Python program which takes in a text file to perform a 
            priority queue and tree structure [chapter 16 of CLRS].
            This program considers variable length codes opposed to 
            fixed length. It uses bitwise operations to encode. It 
            works for letters a-z (changes upper to lower), digits 
            0-9, commas, periods, and spaces.

Task Summary: It reads a filename from standard input, writes a frequency 
            table to frequency.txt generates Huffman codes, writes them to
            codes.txt, use Huffman coding to compress the file, writes the 
            results to a binary file named compressed.bin

'''
from collections import Counter
from queue import PriorityQueue
import heapq


def findCharIndex(char, array):
    # Given a character, for example 'a', and the 2d array from main,
    # findCharIndex will find 'a' in the array and return the index
    for i in range(0, 39):
        if array[i][0] == char or array[i][0].isspace():
            return i
    return -99

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

def buildHuffman(freq):
    # Build the Huffman tree
    heap = [[wt, [sym, ""]] for sym, wt in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # Generate the codes
    codes = dict(heapq.heappop(heap)[1:])

    with open('codes.txt', 'w') as f:
        for sym, code in codes.items():
            f.write(f"{sym}: {code}\n") 
    print("\nhuffman codes successfully written to codes.txt")  

def main():
    specialChars = set('., ')
    heap = []
    heapq.heapify(heap)
    d={}
    
    filename = input("Enter the file name \n(note that the file should seperate with spaces): \n")
    with open(filename, 'r') as file:
        # Read the file into a list of words
        for line in file:
            # Loop through each line
            for c in line:
                # Loop through each character
                if c.isalpha():
                    if c.lower() in d:
                        d[c.lower()] += 1
                    else:
                        d[c.lower()] = 1
                elif c in specialChars or c.isdigit():
                    if c in d:
                        d[c] += 1
                    else:
                        d[c] = 1
                else: 
                    print("skipping invalid character: " + c)
    print("\nFile read, creating frequency table: \n")
    
    #print(len(d))
    #heapq.heapify(charFreqArr)
    freq_table = Counter()
    for item in d:
        freq_table[item] += 1
    print("Char\tFrequency")
    for a,b in d.items():
        heapq.heappush(heap, (b, a))
    for i,j in heapq.nlargest(len(heap),heap):
        print(f"'{j}'\t{i}") 
    buildHuffman(d)
    
main()