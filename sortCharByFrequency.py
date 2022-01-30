"""
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        result = ''
        
        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        s = sorted(dict, key = lambda x : dict[x], reverse = True)
        
        for char in s:
            result += char * dict[char]
        
        return result
        
        
    
