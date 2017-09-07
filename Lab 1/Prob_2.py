alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  # The alphabets

str_example = 'abccddefghijklmmmnnopqrstuvwxyz'  # Example string
print(str_example)

# Element checking
for i in str_example:
    if i not in alphabet:
        print('All elements not in string')

