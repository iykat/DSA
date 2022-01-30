"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
class Solution:
  def firstUniqueChar(self, s: str) -> int:
    count = {} # char : value
    
    for char in s:
      if char in count:
        count[char] += 1
      else:
        count[char] = 1
      for char in count:
        if count[char] == 1:
          return s.index(char)
      return -1
