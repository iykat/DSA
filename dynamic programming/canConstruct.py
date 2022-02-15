 """Write a functioin 'canConstruct(target, wordBank)' that accepts a target string 
 and an array of strings.
 
 The function should return a boolean indicating whether or not the 'target' can be constructed 
 by concatenating elements of the 'wordBank' array.
 
 You may reuse elements of 'wordBank' as many times as needed.
 """
 
# non-optimal solution
def canConstruct(target, wordBank):
  if target == '':
    return True

  for word in wordBank:
    if target.startswith(word):
      suffix = target[len(word):]
      if canConstruct(suffix, wordBank) == True:
        return True
  return False 

# memoized solution

def canConstruct(target, wordBank, memo={}):
  if target in memo: return memo[target]
  if target == '': return True
  
  for word in wordBank:
    if target.startswith(word):
      suffix = target[len(word):]
      if canConstruct(suffix, wordBank, memo) == True:
        memo[target] = True
        return True
  
  memo[target] = False
  return False
  
