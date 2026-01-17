import random

def hangman():
    words = {
        "python": "programming language",
        "internet": "global network",
        "coding": "software skill",
        "laptop": "electronic device",
        "matrix": "math concept"
    }

    word = random.choice(list(words.keys()))
    hint = words[word]
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("Welcome to Hangman Game")
    print("Hint:", hint)

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", used_letters)

        guess = input("Enter a letter: ").lower()

        if guess in used_letters:
            print("Already tried.")
            continue

        used_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

hangman()
