import random
import string


class RandomGenerator:

    @staticmethod
    def random_string(string_length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))

    @staticmethod
    def random_email(string_length=10):
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(string_length)) + '@test.test'
