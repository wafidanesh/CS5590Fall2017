geometric_seq = {}  # Dictionary for the geometric sequence

k = 10  # Length of the sequence

# Populating the dictionary to generate the sequence
for i in list(range(1,k+1)):
    geometric_seq[i] = i*i

print(geometric_seq)

a = list(geometric_seq.values())
print(sum(a))

