"""
Question: 
An array of integers is defined as being meandering order when the first two elements are the respective largest and smallest elements in the array 
and the subsequent elements alternate between its next largest and next smallest elements. 
In other words, the elements are in order of [first_largest, first_smallest, second_largest, second_smallest.....]

Example:
The array [-1, 1, 2, 3, -5] sorted normally is [-5, -1, 1, 2, 3].
Sorted in meandering order, it becomes [3, -5, 2, -1, 1]

Constraints:
2 <= n <= 10^4
-10^6 <= unsorted[i] <= 10^6
The unsorted array may contain duplicate elements
"""

def meander(arr):
  arr.sort()
  meander_arr = []
  small = 0 
  large = -1
  while(arr[small] != arr[large]):
    meander_arr.append(arr[large])
    meander_arr.append(arr[small])
    small = small + 1
    large = large - 1 
  if arr[small] == arr[large]:
    meander_arr.append(arr[large]) 
  return meander_arr
