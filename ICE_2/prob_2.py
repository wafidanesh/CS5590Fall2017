str_example = '123eriororasd28opiu987654321'
digits = 0
letters = 0
somethingelse = 0

print(str_example.isdigit())

for i in str_example:
    print(i)
    if i.isalpha():
        letters = letters + 1
    elif i.isdigit():
        digits = digits + 1
    else:
        somethingelse = somethingelse + 1

print(letters,digits,somethingelse)
