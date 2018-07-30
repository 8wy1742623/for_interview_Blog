# -*- coding:utf-8 -*-
"""1.17 Programming Exercises

准备内容:
class Fraction()
func gcd()


1-9题，在类Franction中补充方法。
10-_题，在类LogicGate中补充方法。
1. Implement the simple methods getNum and geDen.
2. 分数在构建之后，自动约分。
3. operators (__sub__, __mul__, and __truediv__).
4. gt: >, ge: >=, lt: <, le: <=
5. 核实构造类Franction的两个参数必须是整数。
6. 允许创建分数时，传入分母为负数。但构造成的分母需要保持正数，
以此避免计算的错误发生
7. 研究一下 __radd__ 方法，实现它。
    __add__ 应用于：
        a_fraction + _

    __radd__ 应用于：
        _ + a_fraction

    要点 i.
    要点 i._'这个变量上使用任何类型变量，
    只要你在__add__中实现了“各种类型的处理方式”。

    ii.
    有个先后顺序值得注意，
    a + b，会先找 a 的 '__add__' 方法。
    如果没有该方法/此方法返回 NotImplemented，
    则找 b 的 '__radd__' 方法。同样地，
    没有方法/此方法返回 NotImplemented，就不能执行 +，
    会返回TypeError：
    unsupported operand type(s) for +: 'a' and 'b'。
8. __iadd__ 定义了 += 操作 x += y
9. 添加 __repr__
10. 了解其他的逻辑门（such as NAND 与非, NOR 或非, and XOR 异或）
    XNOR异或非
11. 实现半加器
    真值表
    加数A，被加数B，半加和数S，进位数C
    0 0 0 0
    0 1 1 0
    1 0 1 0
    1 1 0 1
    S = A`*B + A*B`
    C = A*B
12. 实现8位全加器
    需要做的事情：
    这类电路，使用一个父类 Circuit
    这个类的函数：
        获取输入getPin_,(不同电路的输入值又不同，
        如全加器比半加器多一个输入值，那么就设定为：
        父类统一是两个输入，而子类再去继承/改写方法)
13. (大致意思，
    原教程中，使用的是电路是向后的工作方式，
    例如，想象在一个复杂电路中，结构是由连接器连接着多个门。
    求电路最终输出的步骤是，开始求解电路最后一个门的输出，
    接着求电路最后一个门的输入。然后根据连接器，求上一个门的输出，
    或者是要求用户输入这个门的输入。

    这样的由结果推导到输出的过程，称之为‘向后的工作方式’。
    现在你需要优化下程序，变成‘向前的工作方式’，
    让程序先获取用户输入，由输入推导出结果。
    )
    原文说“在接收输入时，电路产生输出。”？不理解。

14. 见文件ex_1_17_02.py
"""
import logging


logging.basicConfig(level='INFO')


def gcd(m, n):
    """
    greatest common divisor
    求最大公约数，用算法写是这样写，
    和中学时的方法不同，于是不太记得住， 需要强化记忆。
    """
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction():
    def __init__(self, top, bottom):
        if not isinstance(top, int):
            raise TypeError("num is %s. Using int value instead" % top)
        if not isinstance(bottom, int):
            raise TypeError("den is %s. Using int value instead" % bottom)

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    __repr__ = __str__

    def __add__(self, otherfraction):
        if isinstance(otherfraction, Fraction):
            newnum = (
                self.num * otherfraction.den + self.den * otherfraction.num)
            newden = self.den * otherfraction.den
            return Fraction(newnum, newden)
        else:
            return NotImplemented

    def __radd__(self, otherfraction):
        if isinstance(otherfraction, Fraction):
            newnum = (
                self.num * otherfraction.den + self.den * otherfraction.num)
            newden = self.den * otherfraction.den
            return Fraction(newnum, newden)
        else:
            return NotImplemented

    def __iadd__(self, otherfraction):
        if isinstance(otherfraction, Fraction):
            newnum = (
                self.num * otherfraction.den + self.den * otherfraction.num)
            newden = self.den * otherfraction.den
            self.num = newnum
            self.den = newden
        else:
            return NotImplemented

    def __sub__(self, otherfraction):
        newnum = (self.num * otherfraction.den - self.den * otherfraction.num)
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


class LogicGate():
    """逻辑门电路
    电路输入值，要求是0或1.

    attr:
        name 标签，用于命名；
        output 输出
    """

    def __init__(self, n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """二元逻辑门，如 and， or等
    """

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinA is None:
            return int(
                input("Enter Pin A input for gate " + self.getName() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinB is None:
            return int(
                input("Enter Pin B input for gate " + self.getName() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):
    """一元逻辑门，如： not"""

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pin is None:
            return int(
                input("Enter Pin input for gate " + self.getName() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    """and门"""

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """or门"""

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    """not门"""

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1


class NandGate(BinaryGate):
    """NAND, 与非门
    先与，后非。
    1, 1 (1*1 -> 1 -> 0)
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class NorGate(BinaryGate):
    """NAND, 或非门
    先或，后非。
    1, 0 (1+0 -> 1 -> 0)
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 0
        else:
            return 1


class XorGate(BinaryGate):
    """NAND, 异或门
    相同出0，相异出1
    F = A * B'+A' * B
    """

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1


class Connector:
    """连接器
    连接一个门的输出，和另一个门的输入。
    """

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


# @todo
class Circuit(LogicGate):
    """类：电路
    其子类如：半加器，全加器
    """

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None


class Half_adder(Circuit):
    """半加器
    类型继承电路
    """

    def __init__(self, n):
        Circuit.__init__(self, n)

    def getPinA(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinA is None:
            return int(
                input("Enter Pin A input for gate " + self.getName() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinB is None:
            return int(
                input("Enter Pin B input for gate " + self.getName() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")

    def performGateLogic(self):
        """返回了S，C"""
        a = self.getPinA()
        b = self.getPinB()
        result = '_', '_'
        # 计算S
        if a == b:
            result[0] = 1
        else:
            result[0] = 0
        # 计算C
        result[1] = a * b
        return result


class Full_adder(Circuit):
    """全加器
    类型继承电路
    """

    def __init__(self, n):
        Circuit.__init__(self, n)

    def setPinA(self, integer):
        self.pinA = integer

    def setPinB(self, integer):
        self.pinB = integer

    def setPinC_1(self, integer):
        self.pinC_1 = integer

    def getPinA(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinA is None:
            return int(
                input("Enter Pin A input for gate " + self.getName() + "-->"))
        else:
            return self.pinA

    def getPinB(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinB is None:
            return int(
                input("Enter Pin B input for gate " + self.getName() + "-->"))
        else:
            return self.pinB

    def getPinC_1(self):
        """需要在交互式解释器中手动输入，得到值。"""
        if self.pinC_1 is None:
            return int(
                input(
                    "Enter Pin C-1 input for gate " + self.getName() + "-->"))
        else:
            return self.pinC_1

    def performGateLogic(self):
        """返回了S，C"""
        a = self.getPinA()
        b = self.getPinB()
        c = self.getPinC_1()
        result = 0, 0
        judge = a + b + c
        d = {
            0: [0, 0],
            1: [1, 0],
            2: [0, 1],
            3: [1, 1]
        }
        result = d.get(judge, 0)
        return result


class Full_adder_8_bit(Full_adder):
    """8位全加器"""

    def __init__(self, n):
        Full_adder.__init__(self, n)

    def getPinA(self):
        # pinA应当是怎样的类型？
        # 1，int，但是这样的'0001010'不好处理
        # 2，str，可以操作字符串，
        # 3，列表0,0,0,0,1,0,1,0
        # 4，由字符串输入得到二进制数：
        #   bytes('0001'.encode('utf-8')) -> b'0001'
        #   或者直接：'0001'.encode('utf-8') -> b'0001'
        #   字节码转成字符串
        #   b'1001'.decode() -> '1001'
        # 暂用第3种
        if self.pinA is None:
            result = []
            input_l = input(
                "Enter Pin A(8 bit) input for gate " + self.getName() + "-->")
            l_str = str(int(input_l))
            for elem in l_str:
                result.append(int(elem))
            return result
        else:
            return self.pinA

    def getPinB(self):
        if self.pinA is None:
            result = []
            l_str = input(
                "Enter Pin B(8 bit) input for gate " + self.getName() + "-->")
            l_str = str(int(l_str))
            for elem in l_str:
                result.append(int(elem))
            return result
        else:
            return self.pinB

    def performGateLogic(self):
        """
        a，b 一个list，8位，由0/1整数组成。

        # @review 逻辑过程中也许可以用到 Connector。
        暂时没有用到，于是getPinB函数中都没有
        else:
            return self.pinB.getFrom().getOutput()
        """
        # 1, 1, 1, 1, 1, 0, 0, 1
        a = self.getPinA()
        b = self.getPinB()
        # for test
        # a = 1, 1, 0, 0, 1, 0, 0, 1
        # b = 1, 0, 0, 1, 1, 0, 0, 1

        # 结果：1个进位，后面加上8位。
        result = 0, 0, 0, 0, 0, 0, 0, 0, 0
        single_a = Full_adder('single_f_a')
        for i in range(1, 9):
            single_a.setPinA(a - i)
            single_a.setPinB(b - i)
            single_a.setPinC_1(result - i)

            s_output = single_a.getOutput()
            result[-i] = s_output[0]
            result[-i - 1] = s_output[1]
        return result


def main():
    a = Fraction(3, 2)
    # 1.
    assert a.getNum() == 3, "getNum() unexpected."
    assert a.getDen() == 2, "getDen() unexpected."
    # 2.
    assert str(Fraction(15, 90)) == "1/6", "分数在构造后，没有约分."
    # 3.
    # sub
    b = Fraction(5, 3)
    assert str(a - b) == "-1/6", "31/12 - 23/12 = %s" % (a - b)
    # mul
    assert str(a * b) == "5/2", "3/2 * 5/3 = %s" % (a * b)
    # truediv
    c = Fraction(6, 4)
    assert str(a / b) == "9/10", "3/2 / 5/3 = %s" % (a / b)
    # 4. > <= >=
    assert (b > a), "(5/3 < 3/2): %s" % (b > a)
    assert (a < b), "(3/2 < 5/3): %s" % (a < b)
    assert (a <= c), "(3/2 <= 6/4): %s" % (a <= b)
    assert (a >= c), "(6/4 >= 3/2): %s" % (a >= b)
    # 5. 添加了非整数异常抛出
    # 6. 构造时 common 的存在，保证了分母为正数，分析见'./test_6.py'。
    # 7-9

    # 门电路测试

    # 10
    # 11. 测试半加器
    # g_h1 = Half_adder('g_h1')
    # print(g_h1.getOutput())
    # 12. 测试全加器8位
    # g_f1 = Full_adder_8_bit('g_f1')
    # print(g_f1.getOutput())
    #
    # 13.
    #
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=True)
