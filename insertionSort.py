"""Python code for performing insertion-sort on a list."""

def insertion_sort(A):
  """Sort list of comparable elements into nondescending order."""
  for k in range(1, len(A)):
    cur = A[k]
    j = k
    while j > 0 A[j-1] > cur:
      A[j] = A[j-1]
      j -= 1
    A[j] = cur 
  
