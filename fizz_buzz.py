class FizzBuzzGame(object):

    def play(self, number):
        stringfied_number = str(number)

        if self.__is_divisible_by_three(number) and self.__is_divisible_by_five(number):
            return "Fizz Buzz"

        if self.__is_divisible_by_three(number) or self.__contains_three(stringfied_number):
            return "Fizz"

        if self.__is_divisible_by_five(number) or self.__contains_five(stringfied_number):
            return "Buzz"

        return stringfied_number

    def __contains_three(self, number):
        return number.find('3') is not -1

    def __contains_five(self, number):
        return number.find('5') is not -1

    def __is_divisible_by_three(self, number):
        return number % 3 == 0

    def __is_divisible_by_five(self, number):
        return number % 5 == 0
