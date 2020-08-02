__author__ = 'Angelus1987'

import sys
import load_dictionary

dicionary_list = load_dictionary.load('words.txt')
word_list = load_dictionary.load('words.txt')

"""Where import statements and any variables should be declared.And if necessary manipulated for global use."""


def find_anagrams(word_for_search, search_list_dictionary):
    """Find dictionary palingrams."""

    pass


def find_palingrams(dictionary_list):
    """Find dictionary palingrams."""
    palingram_list = []
    for word in dictionary_list:
        end = len(word)
        reversed_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reversed_word[:end - i] and reversed_word[end - i:] in dictionary_list:
                    palingram_list.append((word, reversed_word[end - i:]))
                if word[:i] == reversed_word[end - i:] and reversed_word[:end - i] in dictionary_list:
                    palingram_list.append(reversed_word[:end - i])
            return palingram_list

        palingrams = find_palingrams(dictionary_list)
        palingrams_sorted = sorted(palingrams)
        print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
        for first, second in palingrams_sorted:
            print("{} {}".format(first, second))
        pass


def print_generic_list(list_items_category_name, list_to_print):
    """Print a list of the items in any list passed to the function. Use the first parameter to describe the list."""
    pass


def find_palindromes(anagram_list):
    """Find palindromes in the anagrams list."""
    palindrome_list = []
    for word in anagram_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)
            print("\nNumber of palindromes found = {}\n".format(len(palindrome_list)))
            # print in list format with no quotes or commas:
            print(*palindrome_list, sep='\n')
            pass


def print_pairs_of_twos(dictionary_of_pairs):
    """Print the keywords and values of an dictionary passed to the method."""
    pass


def print_explanation():
    print(
        '''
        An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once. It can however us on a few of the letters.    
        A palindrome is a word, number, phrase, or other sequence of characters which reads the same 
        backward as forward, such as "madam" or "racecar".

        A palingram – a letter palingram. A palingram can also be created using syllables
        or words, in addition to individual letters. An example of this using words is, “He was, was he?” 
        Notice that the words can be reversed and the sentence still reads the same. 
        A sentence that is a palingram and a palindrome is, “I did, did I”  

        This application allows three activities.

          Activity A: Finds the anagrams for any word you enter. Then identifies palindromes, if there are any, 
                      in the identified anagrams. 

          Activity B: Finds all the word pairs in the dictionary list which form palingrams. 
                      The palingrams ignore spaces and hyphens.   

          Activity C: Find all the palindromes in the dictionary.
          ''')
pass

def write_anagrams_palindromes_to_file(original_word, anagrams_list, palindromes_list):
    """Write the lists of anagrams and the palindromes to a file.
    Use the original word in the file names and descriptions ."""
    pass

def menu():
    print("\nHere are the options: ")
    print()
    choice = input("""           MENU Options: Please use | A | B | C | #
                              1: Would you like to: Enter Activity A?
                              2: Would you like to: Enter Activity B?
                              3: Would you like to: See all palindromes in the dictionary ?
                              4: Exit ? Enter #
                              Please enter your choice: """)

    # ensure only capital A, B or C is used to make the choice; small letters and other characters will not be accepted
    # the # key is also set up as a valid character to allow the user to exit the program
    if choice == "A":
        activitya()
    elif choice == "a":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "B":
        activityb()
    elif choice == "b":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "C":
        activityc()
    elif choice == "c":
        print("please only use capital letters like A, B or C")
        menu()
    elif choice == "#":
        sys.exit()
    elif choice == str:
        print("Please use # to exit")

    elif choice == int or float:
        print('''Invalid entry






            Only Strings / letters are allowed please try again




            ''')
        print("")
        print("Please use A | B | C | #")
        print("Please try again")

        menu()
    else:
        print("Please use A | B | C | #")
        print("Please try again")
        menu()


def activitya():
    # immediately print a statement that lets the user know what Activity A does
    print('''    
        Activity A: Finds the anagrams for any word you enter.
        Then identifies palindromes, if there are any, in the identified anagrams.
        ''')

    menu()

    pass


def activityb():
    # immediately print a statement that lets the user know what Activity B does
    print('''
        Activity B: Finds all the word pairs in the dictionary list which form palingrams.
        The palingrams ignore spaces and hyphens.
        ''')
    print(find_palingrams(word_list))

    menu()
    pass


def activityc():
    # immediately print a statement that lets the user know what Activity C does
    print('''
    Activity C: Finding all the palindromes in the dictionary.


    Please wait.






    Loading


    ''')
    menu()
    pass


def main():
    """The main method with primary functionality of the application."""
    running = True
    pass


# ______________________________________________________________________________


if __name__ == '__main__':
    menu()
