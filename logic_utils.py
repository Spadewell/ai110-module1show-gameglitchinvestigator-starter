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
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int, difficulty: str = "Normal"):
    difficulty_multiplier = {"Easy": 1.0, "Normal": 1.5, "Hard": 2.0}  # Bonus for harder difficulties
    
    if outcome == "Win":
        points = (100 - 10 * (attempt_number + 1)) * difficulty_multiplier.get(difficulty, 1.0)
        if points < 10:
            points = 10
        return current_score + points
    
    # Existing logic for non-win outcomes remains unchanged
    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5
    
    if outcome == "Too Low":
        return current_score - 5
    
    return current_score
