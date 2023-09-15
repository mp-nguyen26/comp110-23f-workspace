"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730574011"

five_char_word : str = input("Enter a 5-character word: ")
single_char : str = input("Enter a single character: ")
print("Searching for " + single_char + " in " + five_char_word)

num_of_matches : int = 0

if str(five_char_word[0]) == str(single_char): 
    num_of_matches = num_of_matches + 1
    print (single_char + " found at index 0" )

if str(five_char_word[1]) == str(single_char): 
    num_of_matches = num_of_matches + 1
    print (single_char + " found at index 1" )

if str(five_char_word[2]) == str(single_char): 
    num_of_matches = num_of_matches + 1
    print (single_char + " found at index 2" )

if str(five_char_word[3]) == str(single_char): 
   num_of_matches = num_of_matches + 1
   print (single_char + " found at index 3" )

if str(five_char_word[4]) == str(single_char): 
    num_of_matches = num_of_matches + 1
    print (single_char + " found at index 4" )

if num_of_matches == 0:
    print("No instances of " + single_char + " found in " + five_char_word)

if num_of_matches == 1:
    print(str(num_of_matches) +" instance of " + single_char + " found in " + five_char_word)

if num_of_matches > 1:
    print(str(num_of_matches) +" instances of " + single_char + " found in " + five_char_word)


















