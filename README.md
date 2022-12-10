# Huffman-Priority-Queue-and-Tree-Structure
Uses Huffman Coding using Priority Queue 

## Description 
Python program which takes in a text file to perform a priority queue and tree structure [chapter 16 of CLRS]. This program considers variable length codes opposed to fixed length. It uses bitwise operations to encode. It works for letters a-z (changes upper to lower), digits 0-9, commas, periods, and spaces.

## Encoding Tasks 
It reads a filename from standard input, writes a frequency table to frequency.txt generates Huffman codes, writes them to codes.txt, use Huffman coding to compress the file, writes the results to a binary file named compressed.bin

## Decoding Tasks
It reconstructs the Huffman tree and use the Huffman tree to efficiently converts the compressed file to ASCII, and writes the results in decoded.txt


Time Complexity: O(n*logn) 
Auxiliary Space: O(n)
