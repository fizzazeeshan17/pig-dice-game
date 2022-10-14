from game.dice import Dice
import io
import unittest
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')


class TestDice(unittest.TestCase):

    def test_get_dice_value_1(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(3, 4)
        self.assertIn(d.get_dice_value(), [3, 4])
        self.assertNotIn(d.get_dice_value(), [1, 2, 5, 6])

    def test_get_dice_value_2(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(1, 6)
        self.assertIn(d.get_dice_value(), [1, 2, 3, 4, 5, 6])
        self.assertNotIn(d.get_dice_value(), [0, 7, 8])

    def test_get_dice_value_3(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(2, 3)
        self.assertIn(d.get_dice_value(), [2, 3])
        self.assertNotIn(d.get_dice_value(), [1, 4, 5, 6])

    def test_get_dice_value_4(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(1, 3)
        self.assertIn(d.get_dice_value(), [1, 2, 3])
        self.assertNotIn(d.get_dice_value(), [4, 5, 6])

    def test_get_dice_value_5(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(5, 6)
        self.assertIn(d.get_dice_value(), [5, 6])
        self.assertNotIn(d.get_dice_value(), [1, 2, 3, 4])

    def test_get_dice_value_6(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(3, 6)
        self.assertIn(d.get_dice_value(), [3, 4, 5, 6])
        self.assertNotIn(d.get_dice_value(), [1, 2])

    def test_get_dice_value_7(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(1, 2)
        self.assertIn(d.get_dice_value(), [1, 2])
        self.assertNotIn(d.get_dice_value(), [3, 4, 5, 6])

    def test_get_dice_value_8(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(4, 6)
        self.assertIn(d.get_dice_value(), [4, 5, 6])
        self.assertNotIn(d.get_dice_value(), [1, 2, 3])

    def test_get_dice_value_9(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(2, 6)
        self.assertIn(d.get_dice_value(), [2, 3, 4, 5, 6])
        self.assertNotIn(d.get_dice_value(), [1, 7])

    def test_get_dice_value_10(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        d = Dice(1, 4)
        self.assertIn(d.get_dice_value(), [1, 2, 3, 4])
        self.assertNotIn(d.get_dice_value(), [0, 5, 6])
