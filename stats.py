def get_num_words(path):

        count = 0

        with open(path) as fstein:

                read_book = fstein.read()
                num_input = read_book.split()

                for words in num_input:
                         count += 1

        return count

def get_char(text):

	total_char = {}
	lower_case = text.lower()
	for char in lower_case:
	       
                if char in total_char:
                        total_char[char] += 1
                else:
                        total_char[char] = 1
	
	return total_char

def sort_on(dict):
        return dict["num"]

def sort_report(char_d):
        sorted_bet = []

        for letter in char_d: 
                if letter.isalpha():
                        sorted_bet.append({"char": letter, "num": char_d[letter]})
        
        sorted_bet.sort(reverse=True, key=sort_on)
        return sorted_bet
                