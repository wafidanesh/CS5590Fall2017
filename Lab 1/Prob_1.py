text_file = open('Prob1.txt','r')  # Opening the text file

data = text_file.read()  # Reading the text file
print(data)

total_words = data.split()  # Determining the word count

count = {}  # Setting up the dictionary

for i in total_words:
    count[i] = total_words.count(i)

print(count)


