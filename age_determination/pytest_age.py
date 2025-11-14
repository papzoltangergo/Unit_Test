import pytest
from age import categorize_by_age

def test_categorize_by_age():
    assert categorize_by_age(5) == "Child"
    assert categorize_by_age(15) == "Teenager"
    assert categorize_by_age(30) == "Adult"
    assert categorize_by_age(70) == "Golden Age"
    assert categorize_by_age(-1) == "Invalid Age: -1"
    assert categorize_by_age(130) == "Invalid Age: 130"

def test_boundary_conditions():
    assert categorize_by_age(0) == "Child"
    assert categorize_by_age(9) == "Child"
    assert categorize_by_age(10) == "Teenager"
    assert categorize_by_age(18) == "Teenager"
    assert categorize_by_age(19) == "Adult"
    assert categorize_by_age(64) == "Adult"
    assert categorize_by_age(65) == "Golden Age"
    assert categorize_by_age(120) == "Golden Age"