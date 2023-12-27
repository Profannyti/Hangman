import random

logo = ''' 
██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                  '''

print(logo)



#add anything to this list
list = ["orange", "peach", "mango", "apple","banana","lemon","strawberry","kiwi","watermelon","grapes","guava",
        "dragonfruit","melon","raspberry","blackberry","blueberry"]




stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


lives = 6

chosen_word = random.choice(list)

display = []



#creating blanks
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"
print(display)

#taking input from user


while "_" in display:
    print(\n)
    guess = input("Guess a letter: ").lower()

#replacing underscore with the letter if correct

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print("YOU LOSE!")
            print(f"The word was '{chosen_word}'")
            quit()

        print(f"You have {lives} lives left!")
    print(stages[lives])

    print(display)
print("YOU WIN!")






