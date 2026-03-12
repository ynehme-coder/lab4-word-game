from main import update_game_state


def test_hit_single_letter():
    secret = "DOG"
    guessed = []
    lives = 6
    word = ["_", "_", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "o", lives, word
    )

    assert new_word == ["_", "O", "_"]
    assert new_guessed == ["O"]
    assert new_lives == 6
    assert status == "hit"


def test_hit_multiple_letters():
    secret = "BANANA"
    guessed = []
    lives = 6
    word = ["_", "_", "_", "_", "_", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "a", lives, word
    )

    assert new_word == ["_", "A", "_", "A", "_", "A"]
    assert new_guessed == ["A"]
    assert new_lives == 6
    assert status == "hit"


def test_miss():
    secret = "DOG"
    guessed = []
    lives = 6
    word = ["_", "_", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "z", lives, word
    )

    assert new_word == ["_", "_", "_"]
    assert new_guessed == ["Z"]
    assert new_lives == 5
    assert status == "miss"


def test_repeat_guess():
    secret = "DOG"
    guessed = ["O"]
    lives = 6
    word = ["_", "O", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "o", lives, word
    )

    assert new_word == ["_", "O", "_"]
    assert new_guessed == ["O"]
    assert new_lives == 6
    assert status == "repeat"


def test_invalid_guess_number():
    secret = "DOG"
    guessed = []
    lives = 6
    word = ["_", "_", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "3", lives, word
    )

    assert new_word == ["_", "_", "_"]
    assert new_guessed == []
    assert new_lives == 6
    assert status == "invalid"


def test_invalid_guess_multiple_letters():
    secret = "DOG"
    guessed = []
    lives = 6
    word = ["_", "_", "_"]

    new_word, new_guessed, new_lives, status = update_game_state(
        secret, guessed, "ab", lives, word
    )

    assert new_word == ["_", "_", "_"]
    assert new_guessed == []
    assert new_lives == 6
    assert status == "invalid"
