import pytest
from  main import count_vowels
def test_count_vowel():
    assert count_vowels("Hello") == 2

@pytest.mark.parametrize("s, expected", [
    ("math", 1),
    ("Aaaaaiiaae", 10),
    ("qwrtP", 0),
    ("Хрен", 1),
    ("СамOлет", 3),
    ("Computer", 3),
    ("selenium", 4),
])
def test_count_vowels(s, expected):
    assert count_vowels(s) == expected
