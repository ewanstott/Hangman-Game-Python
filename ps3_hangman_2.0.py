#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 07:47:42 2023

@author: ewstott
"""

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
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)) , "letters long.")
    print("-----------")    
    
    while guessesLeft > 0:
        print("You have", guessesLeft, "guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        currentLetterGuessed = input("Please give a letter: ")
        
        
        # Scenario 1 - player guesses letter in word!
        if currentLetterGuessed in secretWord:
            lettersGuessed.append(currentLetterGuessed)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            print('-----------') 
            guessesLeft -= 1
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print('Congratulations, you won!')
                break
        
        # Scenario 2 - player guesses letter already guessed!
        elif currentLetterGuessed in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print('-----------') 
        
        # Scenario 3 - player guesses letter not in the word!
        else: 
            lettersGuessed.append(currentLetterGuessed)
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            print('-----------') 
            guessesLeft -= 1
            
        if guessesLeft == 0:
            print("Sorry, you ran out of guesses. The word was", secretWord)
            break
        
            
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)       
    
    
    
    
    