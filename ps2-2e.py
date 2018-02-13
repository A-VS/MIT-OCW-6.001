# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    listed_secret_word = list(secret_word)
    stringed_letters_guessed = ''.join(letters_guessed)
    x = 0
    
    for char in listed_secret_word:
        if char not in stringed_letters_guessed:
            x = 'False'
            break
        else:
            x = 'True'
    return x
    
#print (is_word_guessed(secret_word, letters_guessed))    





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    x = ''
    
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            x +=secret_word[i]
        else:
            x+= '_ '
            
    return x

        

#print(get_guessed_word(secret_word, letters_guessed) )


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = list(string.ascii_lowercase)
    clone_available_letters = available_letters[:]
    counter = -1
    
    for i in clone_available_letters:
        counter += 1
        if i in letters_guessed:
            del(clone_available_letters[counter])
    return(''.join(clone_available_letters))
    
    

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    secret_word
    listed_secret_word = list(secret_word)
    turns = 0
    letters_guessed = ['_']
    wordlenght = len(secret_word)
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word ', wordlenght, ' characters long')
    warnings_left = 3
    print('You have ', warnings_left, ' warnings left')
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    
    while turns < 7:
        print('-------')
        #checks if word is correctly guessed
        if set(listed_secret_word) <= set(letters_guessed):
            print('Congratulations! You won.')
            print('Your total score for this game is: ', (6-turns)*(len(secret_word)))
            break
        #chekcs if amount of turns is exceeded
        elif turns >= 6:
            print('Sorry, you ran out of guesses. The word was: ', secret_word)
            break
        print('You have ', 6-turns, ' guesses left')
        print('Available letters: ', get_available_letters(letters_guessed))    
        guessed_letter = input('Please guess a letter: ')
        lowercase_guessed_letter = str.lower(guessed_letter)
        letters_guessed.append(lowercase_guessed_letter)
#        if guessed_letter == '*':
#            match_with_gaps(get_guessed_word(secret_word, letters_guessed), secret_word)
        #checks if letter already guessed
        if lowercase_guessed_letter in letters_guessed[:-1] and warnings_left > 0:
            warnings_left -= 1
            print("Oops! You've already guessed that letter. You now have ", warnings_left, " warnings left.")
        #checks if guessed letter is in alphabet
        elif str.isalpha(lowercase_guessed_letter) == False and warnings_left > 0:
            warnings_left -= 1
            print('Oops! That is not a valid letter. You have ', warnings_left, 'warnings left: ', get_guessed_word(secret_word, letters_guessed))
        #for already guessed, when out of warnings, adds turns
        elif warnings_left <= 0 and lowercase_guessed_letter in letters_guessed[:-1]:
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
            turns += 1
        #for invalid character, when out of warnings, adds turns
        elif warnings_left <= 0 and str.isalpha(lowercase_guessed_letter) == False:
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
            turns += 1
        #checks if guessed letter is in secret word
        elif lowercase_guessed_letter in listed_secret_word:
            print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        #if guessed is not in word then this for vowels
        elif lowercase_guessed_letter not in listed_secret_word and lowercase_guessed_letter in vowel_list:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            turns += 2
        #if guessed is not in word then this for not vowels
        elif lowercase_guessed_letter not in listed_secret_word and lowercase_guessed_letter not in vowel_list:
            print('Oops! That letter is not in my word: ', get_guessed_word(secret_word, letters_guessed))
            turns += 1
        #failsafe
        else:
            print('something weird is happening')
            break
    

    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    stripped_my_word = my_word.replace(' ', '')
    
    i = -1
    matches = 'False'

    for letter in stripped_my_word:
        i += 1
        if len(stripped_my_word) != len(other_word):
            matches = 'False'
            break
        elif letter == other_word[i] or letter == '_':
            matches = 'True'
        else:
            matches = 'False'
            break

    return matches


        
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
