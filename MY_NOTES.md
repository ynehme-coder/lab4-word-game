# MY NOTES
**My Original Thinking**


**Copilot Suggestions**
**APP STATES:**

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

**APP VARIABLES**

secret_word: String - The target word that player must guess (never changes during a game).
guessed_letters: Set - All letters already guessed by the player (case-insensitive).
lives: Integer - Remaining wrong guesses allowed (decreases on wrong guess, ends game at 0).
revealed_letters: Set - Letters that have been correctly guessed and are now visible.
game_state: String - Current state: START, SHOW_STATUS, GET_INPUT, VALIDATE_INPUT, APPLY_GUESS, CHECK_WIN, CHECK_LOSE, WIN, LOSE, PLAY_AGAIN, EXIT.
current_guess: String - The input from the player (letter or full word).
word_list: List - All available words loaded from the word file at START.
masked_word: String - Visual display of the word with revealed letters and underscores (e.g., "_ A _ _").

**APP RULES AND INVARIANT**

The secret_word must be set once at START and never changed until the game ends or restarts.
Each letter in guessed_letters must be a single alphabetic character (A-Z), case-insensitive.
guessed_letters can only grow (letters added) or be cleared on restart, never removed mid-game.
lives must never go below 0; game moves to LOSE when lives == 0.
revealed_letters is a subset of secret_word; initially empty, grows as guesses succeed.
A guess is invalid if: empty, non-alphabetic, already in guessed_letters, or too many characters.
A correct guess reveals ALL instances of that letter in the word (not just the first).
A wrong guess decreases lives by exactly 1.
A repeated correct guess should not change game state (letter already revealed).
A repeated wrong guess should not decrease lives again (already in guessed_letters).
WIN condition: all letters of secret_word are in revealed_letters.
LOSE condition: lives reaches 0 before all letters are revealed.
masked_word must always reflect the current state of revealed_letters accurately.
PLAY_AGAIN must fully reset all game variables (secret_word, guessed_letters, lives, revealed_letters) for a fresh game.

**APP BUGS:**

1) Input validation bugs
Accepts empty input or spaces as guesses.
Accepts multi-letter input when only one letter is allowed.
Case sensitivity issue (a and A treated as different guesses).
Non-alphabetic characters (7, ?) not rejected.

2) Repeated guess handling
Repeated correct letter reveals again or gives extra points.
Repeated wrong letter decreases lives again (usually should not).
Duplicate tracking mismatch (guessed_letters not updated correctly).

3) Word reveal logic bugs
Only first occurrence of a letter is revealed (e.g., letter reveals one t instead of both).
Incorrect indexing causes wrong letters to appear.
Revealed state not persisted between turns.

4) Win/Lose condition bugs
Win triggers too early (e.g., comparing sets and ignoring repeated letters).
Lose triggers one turn late or one turn early (lives < 0 vs lives == 0).
Both win and lose conditions can trigger in same turn due to bad check order.

5) State transition bugs
Game gets stuck in VALIDATE_INPUT or GET_INPUT.
PLAY_AGAIN doesn’t fully reset state (old guessed letters/lives remain).
START doesn’t pick a fresh word.

6) Display/status bugs
Masked word display out of sync with internal revealed letters.
Used letters list shows duplicates or unsorted clutter.
Remaining lives displayed incorrectly after guess.

7) Word source/randomization bugs
Empty word list crashes game.
Leading/trailing whitespace/newline in chosen word.
Random selection not random (same word repeatedly due to seeding/misuse).

8) Scoring/progress bugs (if scoring exists)
Points awarded for invalid or repeated guesses.
Wrong guesses don’t reduce score/lives consistently.

9) Edge-case word bugs
Hyphen/apostrophe words break validation/display.
Very short words (a) cause immediate win logic issues.
Unicode/accented letters (é) fail in normalization checks.

10) Loop/control-flow bugs
Infinite loop when invalid input is entered.
EXIT path not reachable from PLAY_AGAIN.
Crash on Ctrl+C/EOF input not handled.