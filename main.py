def update_game_state(secret_word: str, guessed_letters: list[str], guess: str, lives: int) -> tuple[list[str],int]:
    word = ""
    guess.capitalize()
    
    for _ in range(len(secret_word)):
        word += "_"
    
    while guess in guessed_letters:
        print("Already guessed!")
        return[guessed_letters,lives]
    
    if guess in secret_word:
        print("Letter Guessed")
        s = secret_word
        
        while s.find(guess) != -1:
            i = s.find(guess)
            word = word[: i] + guess + word[i + 1:]
            s = s[i+1:]
        
        guessed_letters.append(guess)

        print(word)
        return[guessed_letters,lives]
    else:
        lives -= 1
        guessed_letters.append(guess)

        print("Wrong! Letter not in word.")
        print(f"Lives: {lives}")
        return[guessed_letters,lives]
