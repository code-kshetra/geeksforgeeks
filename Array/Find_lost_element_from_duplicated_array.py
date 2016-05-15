'''
Find lost element from a duplicated array
Given two arrays which are duplicates of each other except one element, that is one element from one of the array is missing, we need to find that missing element.

Examples:

Input:  arr1[] = {1, 4, 5, 7, 9}
        arr2[] = {4, 5, 7, 9}
Output: 1
1 is missing from second array.

Input: arr1[] = {2, 3, 4, 5}
       arr2[] = {2, 3, 4, 5, 6}
Output: 6
6 is missing from first array.

'''


input_array1 = map(int, raw_input().split(' '))
input_array2 = map(int, raw_input().split(' '))
ln1 = len(input_array1)
ln2 = len(input_array2)
result =0
if ln1 > ln2:
    for indx, each in enumerate(input_array1):
        if indx < len(input_array2):
            result += input_array1[indx] - input_array2[indx]
        else:
            result += input_array1[indx]
else:
    for indx, each in enumerate(input_array2):
        if indx < len(input_array1):
            result += input_array2[indx] - input_array1[indx]
        else:
            result += input_array2[indx]
print result
