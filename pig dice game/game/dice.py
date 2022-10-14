from random import randint
import sys
sys.path.append('C:/Users/fizza/Desktop/gitcode')

from game.visual_repr import VisualRepresentaion


class Dice:
    def __init__(self, start_dice_pos, end_dice_pos):
        """Initializing the values of start_dice_pos and end_dice_pos

        Args:
            start_dice_pos ([int]): start number given to randint
            end_dice_pos ([int]): end number given to randint
        """
        self.start_dice_val = start_dice_pos
        self.end_dice_val = end_dice_pos

    def get_dice_value(self):
        """Generates a random number between start_dice_pos and end_dice_pos

        Returns:
            [int]: dice_value
        """
        dice_value = randint(self.start_dice_val, self.end_dice_val)
        repr_obj = VisualRepresentaion()
        repr_obj.print_dice(dice_value)
        return dice_value
