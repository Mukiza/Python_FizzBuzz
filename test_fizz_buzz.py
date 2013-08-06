import unittest
from fizz_buzz import FizzBuzzGame


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.game = FizzBuzzGame()

    def test_returns_a_one_when_given_one(self):
        self.assertEqual("1", self.game.play(1))

    def test_returns_Fizz_when_given_two(self):
        self.assertEqual("2", self.game.play(2))

    def test_returns_Buzz_when_given_three(self):
        self.assertEqual("Fizz", self.game.play(3))

    def test_return_Fizz_when_given_four(self):
        self.assertEqual("4", self.game.play(4))

    def test_return_buzz_if_given_five(self):
        self.assertEqual("Buzz", self.game.play(5))

    def test_fizz_buzz_return_6_when_given_6(self):
        self.assertEqual("Fizz", self.game.play(6))

    def test_fizz_buzz_returns_fizz_when_given_six(self):
        self.assertEqual("Fizz", self.game.play(9))

    def test_fizz_buzz_returns_buzz_given_ten(self):
        self.assertEqual("Buzz", self.game.play(10))

    def test_game_return_Fizz_given_thirteen(self):
        self.assertEqual("Fizz", self.game.play(13))

    def test_game_returns_fizz_buzz_when_given(self):
        self.assertEquals("Fizz Buzz", self.game.play(15))

    def test_game_returns_fizz_when_given_fifty_one(self):
        self.assertEquals("Fizz", self.game.play(54))
