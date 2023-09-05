# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    """
    
    >>> secretWord = 'apple' 
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(isWordGuessed(secretWord, lettersGuessed))
    False
    
    PSUEDOCODE:
    for all the letters in secretWord:
        if the letter is not in lettersGuessed:
            Stop and return False
    """
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    """
    PSUEDOCODE:
    for each letter in secretWord:
        if letter is in secretWord:
            concatenate on the letter onto the word
    else: 
        add '_ ' to tempString
    """
    tempStr = ""
    
    for char in secretWord:
        if char in lettersGuessed:
            tempStr += char
        else:
            tempStr += "_ "
    return tempStr

# Solution 2 using list
    # tempList = []
    # for char in secretWord:
    #     if char in lettersGuessed:
    #         tempList.append(char)
    #     else: tempList.append("_ ")
    #     tempListToString = ''.join(tempList)
        
    # return tempListToString  
# Solution 3 - one liner: 
    # return ''.join(tempList ) ???
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = list(string.ascii_lowercase) #initialized with the whole alphabet
    
    for letter in lettersGuessed:
        if letter in availableLetters:
            availableLetters.remove(letter)
    
    availableLettersToString = ''.join(availableLetters)
    
    return availableLettersToString
  

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 8
    lettersGuessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")
    while guessesLeft > 0:
        print("-----------")
        print("You have", guessesLeft, "guesses left")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        userInput = input("Please guess a letter: ")
        if userInput in lettersGuessed:
            # Line bellow broken to comply with pep8
            print("Oops! You've already guessed that letter:",
                  getGuessedWord(secretWord, lettersGuessed))
        else:
            if userInput in secretWord:
                lettersGuessed.append(userInput)
                # Line bellow broken to comply with pep8
                print("Good guess: ", getGuessedWord(secretWord,
                      lettersGuessed))
                if isWordGuessed(secretWord, lettersGuessed):
                    print("-----------")
                    return print("Congratulations, you won!")
            else:
                # Line bellow broken to comply with pep8
                print("Oops! That letter is not in my word:",
                      getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(userInput)
                guessesLeft -= 1
    print("-----------")
    return print("Sorry, you ran out of guesses. The word was", secretWord)

secretWord = 'ewan' #chooseWord(wordlist).lower()
hangman(secretWord)


   # When you've completed your hangman function, uncomment these two lines
   # and run this file to test! (hint: you might want to pick your own
   # secretWord while you're testing)
