'''
Challenge: Write a function that encodes a given string using a simple Caesar cipher, 
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
'''


def encode(input_str,shift_value):
    encoded_text = []

    for char in input_str:
        if char.isupper():
            char = chr(( ord(char) - ord('A') + shift_value  ) % 26 + ord('A'))
            encoded_text.append(char)
        elif char.islower():
            char = chr(( ord(char) - ord('a') + shift_value  ) % 26 + ord('a'))
            encoded_text.append(char)
        else:
            encoded_text.append(char)
    return ''.join(encoded_text)


print(encode("Hello, World!",3))

