# Function to accept a sentence and obtain the number of words

def word_counter():
    userinput = input('Enter a sentence: ')  # Prompt user for the sentence
    num_words = userinput.split()
    return num_words

example = word_counter()  # Calling the function

lower_case = list(map(lambda words:words.lower(),example))  # Converting the words to lowercase for better comparison

print(lower_case)
lower_case = list(set(lower_case))  # Removing duplicate words
print(lower_case)
lower_case.sort()  # Sorting the list alphanumerically
print(lower_case)







