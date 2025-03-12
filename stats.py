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

def get_sorted_list(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list