import random

word_list = ["python", "java", "kotlin", "javascript"]  # Word list can be expanded. Just add more words in this list.

random_word = list(word_list[random.randint(0, len(word_list) - 1)])

word_so_far = list("-" * len(random_word))
letters_guessed = []
alphabet = list("abcdefghijklmnopqrstuvwxyz")

tries = 0
while True:
    if tries < 8 and ("-" in word_so_far):
        print("")
        print("".join(word_so_far))
        letter_guess = input("Input a letter: ")
        if len(letter_guess) > 1:
            print("You should print a single letter")
        elif letter_guess not in alphabet:
            print("It is not an ASCII lowercase letter")
        elif letter_guess in letters_guessed:
            print("You already typed this letter")
        elif letter_guess not in random_word:
            print("No such letter in the word")
            tries += 1
        else:
            for i in range(0,len(random_word)):
                if letter_guess == random_word[i]:
                    word_so_far[i] = letter_guess
        letters_guessed.append(letter_guess)
    elif ("-" not in word_so_far):
        #print("".join(word_so_far))
        print("You guessed the word!\nYou survived!")
        break
    else:
        print("You are hanged!")
        break