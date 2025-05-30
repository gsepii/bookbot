import sys
from stats import get_num_words
from stats import get_char
from stats import sort_on
from stats import sort_report

def main():
	
	if len(sys.argv) == 2:
		book_path = sys.argv[1]
	else:
		print("Usage: python3 main.py <path_to_book>")
		return sys.exit(1)
	
	num_words = get_num_words(book_path)

	with open(book_path) as fstein:
		str_book = fstein.read()
	
	
	char_counts = get_char(str_book)
	alphabet_sort = sort_report(char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")

	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")

	print("--------- Character Count -------")
	for letter in alphabet_sort:
		print(f"{letter["char"]}: {letter["num"]}")

	print("============= END ===============")

main()