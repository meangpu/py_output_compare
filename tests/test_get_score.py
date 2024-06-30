from py_output_compare import get_score_emoji


def test_get_score_emoji_all_green():
    score = 5
    max_score = 5
    assert get_score_emoji(score, max_score) == "🟢🟢🟢🟢🟢"


def test_get_score_emoji_mixed():
    score = 3
    max_score = 5
    assert get_score_emoji(score, max_score) == "🟢🟢🟢🔴🔴"


def test_get_score_emoji_all_red():
    score = 0
    max_score = 3
    assert get_score_emoji(score, max_score) == "🔴🔴🔴"


def test_get_score_emoji_invalid_score():
    score = -1
    max_score = 5
    assert get_score_emoji(score, max_score) == ""


def test_get_score_emoji_max_score_zero():
    score = 3
    max_score = 0
    assert get_score_emoji(score, max_score) == ""
