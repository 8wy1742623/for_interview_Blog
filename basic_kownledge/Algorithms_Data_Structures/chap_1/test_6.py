# -*- coding:utf-8 -*-

"""题6分析
gcd(1, -1) -> -1
gcd(-1, 1) -> 1
gcd(-1, -1) -> -1

gcd(15, -90) -> -15
gcd(-15, 90) -> 15
gcd(-15, -90) -> -15

1. gcd(m, n) 结果的正负情况，与n的相同。
2. 构造分数类的过程中，使用到gcd(m, n)（记作common）的结果，
    于是情形如下：n为负，则common为负，得到分母n // common为正；
        n为正，common正，分母正；

    于是如列出的这几个例子所示，设计到有负号的情况，
    由于有 common 存在，
    得到的分数的结果都能满足需要的形式：
    不论传入分母为负还是为正，构造后的分母都是正数。
"""

from exercises_1_17 import *

print(str(Fraction(15, -90)))  # -1/6
print(str(Fraction(-15, 90)))  # -1/6
print(str(Fraction(-15, -90))) # 1/6

print(str(Fraction(1, -1)))  # -1/1
print(str(Fraction(-1, 1)))  # -1/1
print(str(Fraction(-1, -1))) # 1/1
