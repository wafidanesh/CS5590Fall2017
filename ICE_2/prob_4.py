word_list = ["PHP", "Exercises", "Backend", "Red", "Bangladesh"]
word_len = []
combined = []

for i in word_list:
    print(i)
    word_len.append(len(i))

    print(word_len)
    a = (len(i),i)
    print(a)
    combined.append(a)
    print(combined)

combined.sort()
print(combined)
print(combined[-1])
