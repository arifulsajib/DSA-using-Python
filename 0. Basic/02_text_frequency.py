def text_frequency(text):
    letter_frequency = {}
    for letter in text:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    return letter_frequency


text = "hello, this is ariful islam"
sorted = sorted(text_frequency(text).items(),
                key=lambda x: x[1], reverse=True)
print(sorted[0])
