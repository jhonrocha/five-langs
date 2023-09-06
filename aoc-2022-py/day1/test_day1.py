import os
import day1


def test_challenge1():
    score = day1.challenge1(os.path.join(
        os.path.dirname(__file__), "demo.txt"))
    assert score == 24000


def test_challenge2():
    score = day1.challenge2(os.path.join(
        os.path.dirname(__file__), "demo.txt"))
    assert score == 45000
