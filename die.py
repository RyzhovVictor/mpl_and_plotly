from random import randint


class Die():
    """Клас, представляющий один кубик"""

    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возврощает случайное число от 1 до числа граней"""
        return randint(1, self.num_sides)
