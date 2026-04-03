import sys
sys.path.insert(0, 'agents/prioritizer')
from app import score_line


def test_urgent_keyword_scores():
    assert score_line("important task") == 1


def test_multiple_keywords_stack():
    assert score_line("there's an urgent and important deadline") == 3


def test_no_keywords_scores():
    assert score_line("we'll work on it") == 0


def test_case_insensitive_scoring():
    assert score_line("IMPORTANT WORK!") == 1