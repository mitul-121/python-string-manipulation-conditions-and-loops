import string

sentence = input("Enter a sentence: ")
wordlist = list()
for char in sentence:
    if char in wordlist:
        continue
    wordlist.append(char)
    if char == string.punctuation or char == ' ':
        continue
    num = -1
    for char1 in sentence:
        if char.lower() == char1.lower():
            num += 1
    print(f"{char} repeated {num} times")
