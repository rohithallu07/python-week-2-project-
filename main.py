def count_words(sentence):
    if not sentence:
        print("Empty input")
        return 0

    words=sentence.split()
    return len(words)

# get input here

user_input=input("Enter a sentence: ")

word_count=count_words(user_input)
print(f"Number of words: {word_count}")


