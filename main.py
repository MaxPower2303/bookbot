# Import your stats functions
import sys
from stats import count_words, count_chars, get_sorted_list

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        # Define the file path
        path = sys.argv[1]
        
        # Read the book
        with open(path) as f:
            book_text = f.read()
        
        # Get word count
        word_count = count_words(book_text)
        
        # Get character counts and sorted list
        char_counts = count_chars(book_text)
        sorted_chars = get_sorted_list(char_counts)
        
        # Print the report
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        
        # Print each character count, but only if it's alphabetical
        for char_dict in sorted_chars:
            char = char_dict["char"]
            count = char_dict["count"]
            if char.isalpha():  # Only print alphabetical characters
                print(f"{char}: {count}")
        
        print("============= END ===============")

# Call the main function
if __name__ == "__main__":
    main()


