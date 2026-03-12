def update_game_state(secret_word: str,
                      guessed_letters: list[str],
                      guess: str,
                      lives: int,
                      word: list[str]) -> tuple[list[str], list[str], int, str]:
    """Update Hangman state for one guess.

    Args:
        secret_word: The target word.
        guessed_letters: Letters already guessed in previous turns.
        guess: The new letter guess for this turn.
        lives: Remaining lives before applying the guess.
        word: Current revealed-word state, for example ['A', '_', '_'].

    Returns:
        A tuple of (word, guessed_letters, lives, status), where status is one
        of "invalid", "repeat", "hit", or "miss".
    """

    guess = guess.upper()
    secret_word = secret_word.upper()

    # INVALID
    if len(guess) != 1 or not guess.isalpha():
        return (word, guessed_letters, lives, "invalid")

    # REPEATED
    if guess in guessed_letters:
        return (word, guessed_letters, lives, "repeat")

    guessed_letters = guessed_letters.copy()
    guessed_letters.append(guess)

    hit = False
    
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            word[i] = guess
            hit = True

    if hit: #CORRECT
        return (word, guessed_letters, lives, "hit")
    else: #INCORRECT
        lives -= 1
        return (word, guessed_letters, lives, "miss")