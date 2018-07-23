# -*- coding:utf-8 -*-
"""1.17 Programming Exercises

准备内容:
class Fraction()
func gcd()
"""
import logging
logging.basicConfig(level='INFO')


class Fraction():
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        """==
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        """>
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __ge__(self, other):
        """>=
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum >= secondnum

    def __lt__(self, other):
        """<
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        """<=
        """
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum <= secondnum

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


def gcd(m, n):
    """
    greatest common divisor
    求最大公约数，用算法写是这样写，
    和中学时的方法不同，于是不太记得住， 需要强化记忆。
    """
    while m % n != 0:
        m, n = n, m % n
    return n


"1-4题，在类Franction中补充方法。"
"1. Implement the simple methods getNum and geDen."
"2. 分数在构建之后，自动约分。"
"3. operators (__sub__, __mul__, and __truediv__)."
"4. gt: >, ge: >=, lt: <, le: <="


def main():
    a_f = Fraction(3, 5)
    # 1.
    assert a_f.getNum() == 3, "getNum() unexpected."
    assert a_f.getDen() == 5, "getDen() unexpected."
    # 2.
    assert Fraction(15, 90).__str__() == "1/6", "分数在构造后，没有约分."
    # 3.
    # sub
    a = Fraction(31, 12)
    b = Fraction(23, 12)
    assert (a - b) == Fraction(2, 3), "31/12 - 23/12 = %s" % (a - b)
    # mul
    a = Fraction(3, 2)
    b = Fraction(5, 3)
    assert (a * b) == Fraction(5, 2), "3/2 * 5/3 = %s" % (a * b)
    # truediv
    a = Fraction(3, 2)
    b = Fraction(5, 3)
    c = Fraction(6, 4)
    assert (a / b) == Fraction(9, 10), "3/2 / 5/3 = %s" % (a / b)
    # 4. > <= >=
    assert (b > a), "(5/3 < 3/2): %s" % (b > a)
    assert (a < b), "(3/2 < 5/3): %s" % (a < b)
    assert (a <= c), "(3/2 <= 6/4): %s" % (a <= b)
    assert (a >= c), "(6/4 >= 3/2): %s" % (a >= b)


if __name__ == '__main__':
    main()
