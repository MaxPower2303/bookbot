def count_words(get_book_text):
    word_count = len(get_book_text.split())
    return word_count

def count_chars(get_book_text):
    book_text = get_book_text.lower()
    char_count = {}
    for char in book_text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

