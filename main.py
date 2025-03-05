def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_book):
    file_contents = get_book_text(path_to_book)
    print(file_contents)

main("books/frankenstein.txt")


