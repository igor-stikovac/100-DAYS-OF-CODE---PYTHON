import random
import mistakes_drawings

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
word = random.choice(word_list).upper()

correct_guesses = ["_ "] * len(word)
print("".join(correct_guesses),"\n")

ind_error = 0
ind_correct = 0

while ind_error < 6 and ind_correct < len(word):
    guess = input("Guess a letter: ").upper()
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                correct_guesses[i] = guess
                ind_correct += 1
    else:
        print("Wrong!")
        ind_error += 1
    print("".join(correct_guesses))
    print(mistakes_drawings.mistakes[ind_error])

if( ind_correct == len(word)):
    print("Congratulations! You guessed the word!")
else:    
    print("Game Over! The word was:", word)
