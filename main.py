from functools import lru_cache

class NumberCreator:
    @staticmethod
    def create_1() -> int:
        """
        this method returns the number 1.
        """
        return ord(chr(ord(chr(ord(chr(1))))))

    @lru_cache
    @staticmethod
    def create_10() -> int:
        """
        this method returns the number 10.
        """
        expected_value = 0
        for i in range(10):
            expected_value += i
        while expected_value > 10:
            expected_value -= NumberCreator.create_1()
        return expected_value

    @lru_cache
    @staticmethod
    def add_1(number: int) -> int:
        """
        this method returns a integer that is one larger than the `number`.
        """
        original_number = number
        ten = NumberCreator.create_10()
        one = ten // ten
        original_number += one
        return original_number

class WordCreator:
    def create_p(self) -> str:
        """
        this method returns the letter 'P' from the latin alphabet.
        """
        ascii_code_point = 0
        ten = NumberCreator.create_10()
        one = NumberCreator.create_1()
        target_ascii_code_point = ten * (one + one + one + one) * (one + one)
        while ascii_code_point != target_ascii_code_point:
            ascii_code_point = NumberCreator.add_1(ascii_code_point)
        return chr(ascii_code_point)
    
class Printer:
    def __init__(self):
        self.print_function = lambda x: print(x, end="\n", sep=" ")

    def print(self, string: str):
        self.print_function(string)

if __name__ == "__main__":
    printer = Printer()
    word_creator = WordCreator()
    printer.print(word_creator.create_p())