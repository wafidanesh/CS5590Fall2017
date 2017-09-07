ROI = list(range(700,1701))  # The range of integers

numbers = []  # Numbers that fulfill conditions

# Checking for condition fulfilment
for i in ROI:
    if ((i%5==0) & (i%2==0)):
        numbers.append(i)

print(numbers)
