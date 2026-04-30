def is_wake_word(text):
    text = text.lower()

    wake_words = [
        "tushar",
        "tusar",
        "tusher",
        "t-shirt",
        "teacher",
        "teshar"
    ]

    return any(word in text for word in wake_words)