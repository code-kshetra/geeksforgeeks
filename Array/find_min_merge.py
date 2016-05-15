'''
Find minimum number of merge operations to make an array palindrome
Given an array of positive integers. We need to make the given array a ‘Palindrome’. Only allowed operation on array is merge. Merging two adjacent elements means replacing them with their sum. The task is to find minimum number of merge operations required to make given array a ‘Palindrome’.

To make an array a palindromic we can simply apply merging operations n-1 times where n is the size of array (Note a single element array is alway palindrome similar to single character string). In that case, size of array will be reduced to 1. But in this problem we are asked to do it in minimum number of operations.

Example:

Input : arr[] = {15, 4, 15}
Output : 0
Array is already a palindrome. So we
do not need any merge operation.

Input : arr[] = {1, 4, 5, 1}
Output : 1
We can make given array palindrome with
minimum one merging (merging 4 and 5 to
make 9)

Input : arr[] = {11, 14, 15, 99}
Output : 3
We need to merge all elements to make
a palindrome.
Expected time complexity is O(n).
'''

import math
test_case = int(raw_input())
for _ in range(0,test_case):
    array_data = map(int, raw_input().split(' '))
    array_mid = int(math.ceil(len(array_data)/2))
    first_index =0 
    last_index = len(array_data)-1
    count = 0
    
    while first_index <= array_mid and last_index >= array_mid:
        if array_data[first_index] == array_data[last_index]:
            first_index +=1
            last_index -=1
            continue
        if array_data[first_index] > array_data[last_index]:
            array_data[last_index-1] += array_data[last_index]
            last_index -=1
        else:
            array_data[first_index+1] += array_data[first_index]
            first_index +=1
        count +=1
    print count
