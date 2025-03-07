from stats import count_words, count_chars

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        book_text = f.read()
    return book_text

def main(path_to_book):
    book_text = get_book_text(path_to_book)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")
    char_count = (count_chars(book_text))
    print(char_count)

main("books/frankenstein.txt")


