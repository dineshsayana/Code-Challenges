# Code-Challenges
-----------
### Unique Element Sum 

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

-------------
### Caesar cipher

Write a function that encodes a given string using a simple Caesar cipher, 
shifting each letter by a specified number of places down the alphabet. 
The function should handle both uppercase and lowercase letters and ignore non-alphabetical characters.

Input:

A string to encode.
An integer representing the shift value.
Output:

The encoded string.
Example:

Input: "Hello, World!", Shift: 3
Output: "Khoor, Zruog!"
