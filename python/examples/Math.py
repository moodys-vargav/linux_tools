from unittest import TestCase

"""
Example code to demonstrate Sphinx capabilities.
Sphinx uses reStructuredText as its markup language,
and many of its strengths come from the power and straightforwardness of
reStructuredText and its parsing and translating suite, the Docutils.
"""


class Math:
    """ Methods for arithmetic operations """

    @staticmethod
    def multiply(*args: int):
        """
        Multiply input parameters

        :type  args: :class:`list` of :class:`int`
        :param args: List of integers
        """

        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def sum(*args: int):
        """
        Addition of input parameters

        :type  args: :class:`list` of :class:`int`
        :param args: List of integers
        """
        result = 0
        for x in args:
            result += x
        return result


class Test(TestCase):
    """ Methods for unittesting """

    def test_multiply(self):
        """ Unittest for Math.multiply """
        result = Math().multiply(4, 5, 6)
        self.assertEqual(result, 120, 'Multiplication error!')


def main():
    math = Math()
    print(math.sum(4, 5, 6))
    print(math.multiply(4, 5, 6))
    Test().test_multiply()


if __name__ == '__main__':
    main()
