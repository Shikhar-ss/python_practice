# Define function to add numbers

from pyrsistent import b


def sumOf(a, b):
    return a+b


# print(sumOf(2, 3))


# Define a class called Summation and its method sum

class Summation(object):

    def sum(self, a, b):
        self.result = a+b
        return self.result

    def sumOfThree(self, a, b, c):
        self.result = a + b + c
        return print(self.result)


newSum = Summation()

newSum.sumOfThree(1, 2, 3)
