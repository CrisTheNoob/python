word_list = ['Ardwark', 'Baboon', 'Camel']
#TODO-1 Randomly choose a word from the world_list and assign it to a variable called chosen_word.

import random

chosen_word = random.choice(word_list)

#TODO-2 Ask the user to guess a letter and assign thier answer to a variable called guess. Make guess lowercase.

guess = input('Guess a letter: ').lower()

print(f'Pssst, the solution is {chosen_word}')

display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input('Guess a leter: ').lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f'Current position: {position}\n Current Letter: {letter}\n Guessed letter: {guess}')
        if letter == guess:
            display[position] = letter

    print(display)

    if '_' not in display:
        end_of_game = True
        print('You win.')