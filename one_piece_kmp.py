# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 02:33:36 2020

@author: SecretProgrammer10
"""

def patternSearch(pat, text, val):
    pat_len = len(pat)
    text_len = len(text)
    count = 0
    j = 0
    i = 0
    lps = [0]*pat_len
    preProcessLPS(pat, pat_len, lps)
    while i < text_len:
        if pat[j] == text[i]:
            i += 1
            j += 1
        if j == pat_len:
            count += 1
            j = lps[j-1]
        elif i < text_len and pat[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
    if count == val:
        print("YES")
    else:
        print("NO")

def preProcessLPS(pat, pat_len, lps):
    length = 0
    lps[0]
    i = 1
    while i < pat_len:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1

if __name__ == '__main__':
    text = input().strip().lower()
    pattern = input().strip().lower()
    val = int(input())
    patternSearch(pattern, text, val)
        
