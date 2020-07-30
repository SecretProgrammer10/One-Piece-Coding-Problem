# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:21:37 2020

@author: SecretProgrammer10
"""

d = 256
prime_no = int(1e9+9)

def onePiece(pat, text, val):
    text_len = len(text)
    pat_len = len(pat)
    h = 1
    pat_hash = 0
    text_hash = 0
    count = 0
    i = 0
    j = 0
    
    h = pow(d, pat_len - 1)%prime_no
    
    for i in range(pat_len):
        pat_hash = (d*pat_hash + ord(pat[i]))%prime_no
        text_hash = (d*text_hash + ord(text[i]))%prime_no
    
    for i in range(text_len - pat_len + 1):
        if pat_hash == text_hash:
            for j in range(pat_len):
                if text[i+j] != pat[j]:
                    break
            
            j += 1
            
            if j==pat_len:
                count += 1
            
        if i < (text_len - pat_len):
            text_hash = (d*(text_hash - ord(text[i])*h) + ord(text[i + pat_len]))%prime_no
            if text_hash < 0:
                text_hash += prime_no
    
    if count == val:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    text = input().strip().lower()
    pat = input().strip().lower()
    val = int(input())
    onePiece(pat, text, val)

                
