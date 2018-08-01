"""
WHAT
3.7 节的练习

运行：ipython --pdb test_01.py
"""

import logging

logging.basicConfig(level='INFO')

from stack_class import Stack


def match_char(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


def parChecker(symbolString):
    """
    WHAT
    检查字符串中的三种类型括号数量是否是成对出现。
    括号平衡。

    HOW
    Stack，统计括号，出现左括号添加元素，出现右括号删除元素。
    检查完字符串后，判断该 Stack 是否是空。
    空 -> 平衡，非空 -> 不平衡。
    """
    s = Stack()
    balanced = True
    for char in symbolString:
        if char in '([{':
            s.push(char)
        elif char in ')]}':
            if s.isEmpty():
                balanced = False
                break
            else:
                top = s.pop()
                if not match_char(top, char):
                    balanced = False

    if balanced and s.isEmpty():
        return True
    else:
        return False


def main():
    symbol_string = '(1 ()[]()(9({})d ))(sdf )'
    print(parChecker(symbol_string))
    symbol_string = '( 9d df)'
    print(parChecker(symbol_string))


if __name__ == '__main__':
    main()