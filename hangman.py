import random

print("====================================")
print("          HANGMAN GAME")
print("====================================")

words = ["python", "computer", "programming", "database", "developer"]
word = random.choice(words)
guessed = set()
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display = " ".join(letter if letter in guessed else "_" for letter in word)
    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.add(guess)

    if guess in word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
else:
    print("\nGame Over!")
    print("The word was:", word)

print("\nHangman game ended.")
