def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
original_string = "hello"
reversed_string = reverse_string(original_string)
print("Reversed string:", reversed_string)