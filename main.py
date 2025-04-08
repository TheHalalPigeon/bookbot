import sys

from stats import get_num_words, count_chars, sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
        return book

def main():
    # GETTING TEXT
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        text = get_book_text(path)
    
    # GETTING DATA
    num_words = get_num_words(text)
    char_count = count_chars(text)
    sorted_chars = sort_chars(char_count)
    
    # PRINTING
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["name"]}: {char["count"]}")
    
main()