words = ["python", "hangman", "random", "string", "loops"]
for word in words:
    guessed = ["_"] * len(word)
    attempts = 6
    used = set()

    print("\n=== New Game ===")
    print("Guess the word! Attempts:", attempts)

    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Used:", " ".join(sorted(used)) if used else "-")
        ch = input("Your guess: ").strip().lower()

        if len(ch) != 1 or not ch.isalpha():
            print("Enter exactly one letter (a-z).")
            continue
        if ch in used:
            print("You already tried that.")
            continue

        used.add(ch)
        if ch in word:
            for i, c in enumerate(word):
                if c == ch:
                    guessed[i] = ch
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    if "_" not in guessed:
        print("\n You win! The word was:", word)
    else:
        print("\n Game over! The word was:", word)
