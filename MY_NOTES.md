# My Original Thinking


**Copilot Suggestions**
A Hangman-style word game is easiest to design as a small state machine. Core states:

START
Load word list, pick secret word, reset lives, clear guessed letters.

SHOW_STATUS
Display masked word (_ _ A _ _), used letters, and remaining lives.

GET_INPUT
Wait for player guess (letter or full word, depending on your rules).

VALIDATE_INPUT
Reject invalid input (empty, non-letter, too long, already guessed), then return to GET_INPUT.

APPLY_GUESS
Check if guess is correct or wrong, update revealed letters / guessed set / lives.

CHECK_WIN
If all letters are revealed, move to WIN.

CHECK_LOSE
If lives reach 0, move to LOSE.

WIN
Show success message and the word.

LOSE
Show failure message and reveal the word.

PLAY_AGAIN
Ask restart (yes/no).
yes -> START, no -> EXIT.

EXIT
End game.

A common loop is:
START -> SHOW_STATUS -> GET_INPUT -> VALIDATE_INPUT -> APPLY_GUESS -> CHECK_WIN/CHECK_LOSE -> SHOW_STATUS ... until WIN or LOSE.