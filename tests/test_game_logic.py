import os
import sys

# Ensure test can import modules from the repo root.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import (
    check_guess,
    get_attempt_limit,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 25)
    assert get_range_for_difficulty("Normal") == (1, 75)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_attempt_limit_ordering():
    assert get_attempt_limit("Easy") > get_attempt_limit("Normal") > get_attempt_limit("Hard")


def test_parse_guess_accepts_float_and_int_strings():
    ok, value, err = parse_guess("42")
    assert ok and value == 42 and err is None

    ok, value, err = parse_guess("42.0")
    assert ok and value == 42 and err is None


def test_update_score_win_narrows_with_attempts():
    base = 0
    score_early = update_score(base, "Win", 1)
    score_late = update_score(base, "Win", 5)
    assert score_early > score_late
