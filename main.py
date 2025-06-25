import sys;


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read();
        return file_contents;

def main():
    book_text = get_book_text("books/frankenstein.txt");
    print(book_text);


print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")

from stats import string_count
string_count(sys.argv[1])

print("--------- Character Count -------")

from stats import sorted_list
sorted_list(sys.argv[1])

print("============= END ===============")



