from app import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_at_boundaries():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"

def test_guess_just_off():
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"


# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, value, _ = parse_guess("")
    assert ok is False
    assert value is None

def test_parse_none():
    ok, value, _ = parse_guess(None)
    assert ok is False
    assert value is None

def test_parse_non_numeric():
    ok, value, _ = parse_guess("abc")
    assert ok is False
    assert value is None

def test_parse_float_string():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7

def test_parse_negative_number():
    ok, value, _ = parse_guess("-5")
    assert ok is True
    assert value == -5


# --- get_range_for_difficulty ---

def test_easy_range():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_hard_range():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

def test_unknown_difficulty_defaults():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# --- update_score ---

def test_win_on_first_attempt():
    # attempt_number=1 → points = 100 - 10*(1+1) = 80
    new_score = update_score(0, "Win", 1)
    assert new_score == 80

def test_win_score_minimum_10():
    # attempt_number=9 → 100 - 10*10 = 0, clamped to 10
    new_score = update_score(0, "Win", 9)
    assert new_score == 10

def test_too_high_even_attempt_adds_points():
    new_score = update_score(50, "Too High", 2)  # even attempt
    assert new_score == 55

def test_too_high_odd_attempt_removes_points():
    new_score = update_score(50, "Too High", 3)  # odd attempt
    assert new_score == 45

def test_too_low_always_removes_points():
    new_score = update_score(50, "Too Low", 1)
    assert new_score == 45

    new_score = update_score(50, "Too Low", 2)
    assert new_score == 45

def test_unknown_outcome_unchanged():
    new_score = update_score(50, "SomeOtherOutcome", 1)
    assert new_score == 50
