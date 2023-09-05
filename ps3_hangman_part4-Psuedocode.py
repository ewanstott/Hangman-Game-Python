#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:02:16 2023

@author: ewstott
"""
"""
PLAY: 
- Greeting "Welcome to the game, Hangman!"
- The game itself
    - "I am thinking of a word that is X letters long."
    - You have x guesses left <<< mistakesMade varialble to hold number of guesses/mistakes made
    - Report Available letters <<< Problem 3 <<< call this function here
    - Prompt for input - "Please guess a letter: ", create a list to store users guesses -> playerLetterGuessed
    - EVALUATE INPUT
        a) Player guesses a letter in word!
            - 'Good guess: _a_n' >>> Call getGuessedWord function
            - Update Available Letters >>> Call getAvailableLetters function
        b) Player guesses letter already guessed!
            - Repromt for input "Oops! You've already guessed that letter: _a_n"
        c) Player guesses a letter not in the word...
            - "Oops! That letter is not in my word: _a_n"
                - Next round, reduce guesses by -1
                - Remove that letter from availableLetters
                - Repromt for another guess
     - Continue play until either
        a) Player has no remaining guesses AKA player makes 8 mistakes 
            - "Sorry, you ran out of guesses. The word was ____."
        b) Player guesses all letters in word: yay!
            - "Congratulations, you won!"    
            
NOTES:
    - Loop happening - continue until 8 mistakesMade happen
"""
PSUEDOCODE:

mistakesMade - variable to count mistakes 

Greeting

print out
    Welcome to the game, Hangman!
    I am thinking of a word that is len(string) letters long.

The game itself

while (either the player has remaining guesses or while the player has not yes guessed the word)

        while mistakesMade < 8 and isWordGuesses is False
    
        break statesment in code (in while loop):
        if mistakesMade < 1
        break
        if getGuessedWord is True
        break

    Report remaning guesses, available letters, then prompt for input
    Evaluate input
     
    You have 8 guesses left.
	Available letters: abcdefghijklmnopqrstuvwxyz
	Please guess a letter: 
    
    Evaluate input
        # Nested condition (if something happends, do this etc)
        if player guesses a letter in word! 
            add that letter to the lettersGuessedList
            report Good guess: _w_n (<< Use function: getGuessedWord(secretWord, lettersGuessed))
            if user has guessed all letters, break:
             -> if getGuessedWord is True
                break
            mistakesMade += 1
            
        else if Player guesses letter already guessed
            continue back into main loop
            
        else player guesses a letter not in word
            add that letter to the lettersGuessed
            Oops! That letter is not in my word: _w_n
            mistakesMade += 1
    
    Continue play until either
        Player has no remaining guesses
        Player guesses all letters in word: yay! 




























