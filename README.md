# Hangman Word Game

A Python implementation of the classic Hangman guessing game.

## Project Structure

- `main.py` — Core game logic, specifically the `update_game_state()` function
- `test_update_game_state.py` — Test suite for the game logic

## Running the Tests

### Prerequisites
- Python 3.9 or later
- `pytest` (optional, but recommended for cleaner output)

### Using pytest (recommended)

```bash
pytest test_update_game_state.py
```

Or with verbose output:

```bash
pytest test_update_game_state.py -v
```

### Using Python's built-in unittest discovery

```bash
python -m pytest test_update_game_state.py
```

### Running tests directly with Python

```bash
python test_update_game_state.py
```

## Running the Game

The main game loop is not yet implemented. Currently, `main.py` contains the `update_game_state()` function that handles a single guess.

To play the full game, implement:
1. A main game loop in `main.py`
2. Game initialization (select secret word, create empty word state)
3. User input handling
4. Game end conditions (win/lose)

## Function Reference

### `update_game_state(secret_word, guessed_letters, guess, lives, word)`

Updates the game state after a player guess.

**Parameters:**
- `secret_word` (str): The target word to guess
- `guessed_letters` (list[str]): Letters guessed in previous turns
- `guess` (str): The new letter guess (lowercase or uppercase)
- `lives` (int): Remaining lives before this guess
- `word` (list[str]): Current revealed-word state, e.g., `['_', 'A', '_']`

**Returns:**
A tuple of `(word, guessed_letters, lives, status)` where:
- `word` (list[str]): Updated revealed state
- `guessed_letters` (list[str]): Updated list of all guessed letters
- `lives` (int): Updated lives count
- `status` (str): One of `"hit"`, `"miss"`, `"repeat"`, or `"invalid"`

**Status codes:**
- `"hit"` — Letter found; word revealed
- `"miss"` — Letter not found; lives decremented
- `"repeat"` — Letter already guessed; state unchanged
- `"invalid"` — Invalid input (not a letter or multiple chars); state unchanged

## Test Coverage

The test suite covers:
- Single-letter hits
- Multi-letter hits (repeated letters in word)
- Misses
- Repeated guesses
- Invalid inputs (digits, multiple letters)
- Case-insensitivity (lowercase user input treated as uppercase)
