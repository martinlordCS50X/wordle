# wordle
## Introduction
This is an implementation of Wordle using Python and through the command line. On top of being a game you can play and learn from, instead of an app or website with ads, there are also some useful tools for if you want to make your own implementation of Wordle, or other apps, using my tools.
## Function 'check'
In helpers.py, I have made a function called 'check', that takes a word as input, assuming it is 5 letters, and returns a dictionary with each letter of the input word being linked with GREEN, YELLOW, or RED (grey if using NYT Wordle or the Wordle app). These three strings mean different things, that you will already know if you are a frequent user of Wordle.
## Function 'print_hint'
Also in helpers.py, there is a function named 'print_hint', which takes the output of 'check' as input, and prints a hint, with colored letters (GREEN, YELLOW, or RED), meaning different things. You will know what they mean if you are a frequent user of Wordle.
## Function 'is_word'
Finally, in helpers.py, I made a function called 'is_word'. It takes a word as input and returns True or False, depending on whether the input was a word.
## Module 'nyt_api'
Credit to sbplat for making code to work with the New York Times Wordle API, and get today's answer in readable JSON format. Visit https://github.com/sbplat/wordle for more details.
