# fichier: test_calculatrice.py

import pytest
from docker_rep.app.function1 import addition, soustraction, multiplication, division


def test_addition():
    assert addition(3, 2) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


def test_soustraction():
    assert soustraction(3, 2) == 1
    assert soustraction(-1, 1) == -2
    assert soustraction(0, 0) == 0


def test_multiplication():
    assert multiplication(3, 2) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 10) == 0


def test_division():
    assert division(6, 2) == 3
    assert division(-6, 2) == -3
    assert division(5, 2) == 2.5
    assert division(0, 1) == 0
    assert division(5, 0) is None  # Pour vérifier la division par zéro

