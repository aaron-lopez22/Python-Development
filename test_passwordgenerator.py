from passwordgenerator import lower_character_generator, upper_case_generator, generate_password, symbol_generator
from pytest import approx
import pytest
import random
from random import randint




def test_lower_character_generator():

    lower_character = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"]

    for _ in range(26):

        word = lower_character_generator(1)


        assert word in lower_character


def test_symbol():


    symbol_character = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",]

    for _ in range(15):

        word = symbol_generator(1)


        assert word in symbol_character

    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])