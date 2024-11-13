def get_longest_word(sentence: str) -> str:
    longest_word = ""
    max_length = 0

    for word in sentence.split():
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word


print(get_longest_word("Python is simple and effective!"))
print(get_longest_word("Python is simple and easy to learn"))
