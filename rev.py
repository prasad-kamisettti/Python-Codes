
### code to check reverese of a word 

# string = input("Enter a string: ")

# words_split = string.split()

# reversed_words = ""

# for word in words_split:
#     reversed_word = word[::-1]
#     reversed_words += reversed_word + " "

# reversed_words = reversed_words.strip()

# print(reversed_words)



string = input("Enter a string: ")

words_split = string.split()

reversed_words = ""

for word in reversed(words_split):
    reversed_words += word + " "

reversed_words = reversed_words.strip()

print(reversed_words)
