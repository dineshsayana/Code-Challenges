'''
Write a function that takes a list of integers and returns the sum of all unique elements. An element is considered unique if it appears exactly once in the list.

Input:

A list of integers nums (1 <= length of nums <= 10^4).
Each integer in the list is between -10^4 and 10^4.
Output:

An integer representing the sum of all unique elements in the list.
​

Examples:​
Input: [1, 2, 3, 2]
Output: 4
Explanation: Only 1 and 3 are unique, so their sum is 4.
​
Input: [1, 1, 1, 1]
Output: 0
Explanation: There are no unique elements.
​
Input: [1, 2, 3, 4, 5]
Output: 15
Explanation: All elements are unique, so their sum is 15.
'''


def unique_element_sum(input_list):
    unique_list = []
    for i in input_list:
        # checking if element in unique_list if not adding it, if exists remove that element
        if unique_list is None or i not in unique_list :
            unique_list.append(i)
        else:
            unique_list.remove(i)
    return sum(unique_list)
            



print(unique_element_sum([1, 1, 1, 1]))
print(unique_element_sum([1, 2, 3, 2]))
print(unique_element_sum([1, 2, 3, 4, 5]))
