import random
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(word_list)
print(f"Psst, choosen word {word}")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
display = []
for n in word:
    display += "_"

print(display)

end_of_game = False
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
while not end_of_game:
    user_guess = input("Guess a letter: ")
    for position in range(0, len(word)):
        letter = word[position]
        if letter == user_guess:
            display[position] = user_guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
