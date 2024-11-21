def correct_jumbled_text(text, words) -> str:
    word_dict = {}
    for word in words:
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + "".join(sorted(word[1:-1])) + word[-1]
        word_dict[key] = word

    corrected_words = []
    for word in text.split():
        if len(word) <= 2:
            key = word
        else:
            key = word[0] + "".join(sorted(word[1:-1])) + word[-1]
        corrected_word = word_dict.get(key, word)
        if word.istitle():
            corrected_word = corrected_word.title()
        corrected_words.append(corrected_word)

    return " ".join(corrected_words)


if __name__ == "__main__":
    words = ["correct", "someone", "words", "to", "collect", "wants"]
    text = "Somoene watns to colelct corcert wodrs"
    print(correct_jumbled_text(text, words))
    text = "The quick brown fox jumps over the lazy Dog"
    words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    print(correct_jumbled_text(text, words))
