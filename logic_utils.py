attempt_limit_map = {
    "Easy": 10,    # More attempts for easier difficulty
    "Normal": 7,   # Middle ground
    "Hard": 5,     # Fewest attempts for hardest difficulty
}

def get_attempt_limit(difficulty: str) -> int:
    return attempt_limit_map.get(difficulty, 10)


def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 25  # Slightly wider than 1-20 for more "easy" feel, but still small
    if difficulty == "Normal":
        return 1, 75  # Increased from 1-50 to create a bigger gap from Easy and Hard
    if difficulty == "Hard":
        return 1, 100  # Keep as-is, as it's already the widest
    return 1, 100  # Fallback


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret, low, high):
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > high or guess < low:
            return "Incorrect", "Your guess is out of bounds for the chosen difficulty."

        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int, difficulty: str = "Normal"):
    difficulty_multiplier = {"Easy": 1.0, "Normal": 1.5, "Hard": 2.0}  # Bonus for harder difficulties
    
    if outcome == "Win":
        points = (100 - 10 * (attempt_number + 1)) * difficulty_multiplier.get(difficulty, 1.0)
        if points < 10:
            points = 10
        return current_score + points
    
    # Existing logic for non-win outcomes remains unchanged
    if outcome == "Too High":
        return current_score - 5
    
    if outcome == "Too Low":
        return current_score - 5
    
    return current_score
