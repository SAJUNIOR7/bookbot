import sys
from stats import get_book_text, count_words, count_characters, chars_dict_to_sorted_list

def main():
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line argument
    book_path = sys.argv[1]
    
    # Read the book
    book_content = get_book_text(book_path)
    word_count = count_words(book_content)
    print(f"Found {word_count} total words")
    
    # Get character counts and sort them
    char_counts = count_characters(book_content)
    sorted_chars = chars_dict_to_sorted_list(char_counts)
    
    # Print the report
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()
    
    
