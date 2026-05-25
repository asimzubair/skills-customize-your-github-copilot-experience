
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game using Python to practice string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Create the game loop

#### Description

Write a Python program that randomly selects a word, accepts letter guesses, and updates the displayed word state until the player wins or runs out of attempts.

#### Requirements
Completed program should:

- Choose a random word from a predefined list
- Show the hidden word progress using underscores for unguessed letters
- Accept player letter input and update the display after each guess
- Prevent duplicate guesses from affecting remaining attempts

### 🛠️ Handle win/lose conditions

#### Description

Add logic to determine when the player has won or lost and display a clear final message.

#### Requirements
Completed program should:

- Track the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts reach zero
- Display a winning message when the player guesses the word
- Display a losing message and reveal the word when the player uses all attempts
