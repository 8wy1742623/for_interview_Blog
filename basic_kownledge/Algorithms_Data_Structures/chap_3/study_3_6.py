"""
WHAT
3.6 节的练习

运行：ipython --pdb test_01.py
"""

import logging

logging.basicConfig(level='WARNING')

from stack_class import Stack


def parChecker(symbolString):
    """
    WHAT
    检查字符串中的括号数量是否是成对出现。
    括号平衡。

    HOW
    Stack，统计括号，出现左括号添加元素，出现右括号删除元素。
    检查完字符串后，判断该 Stack 是否是空。
    空 -> 平衡，非空 -> 不平衡。
    """
    s = Stack()
    balanced = True
    for char in symbolString:
        if char is '(':
            s.push(char)
        elif char is ')':
            if s.isEmpty():
                balanced = False
                break
            else:
                s.pop()
    if balanced and s.isEmpty():
        return True
    else:
        return False


def main():
    symbol_string = '(1 ()()()(9(())))))d )(sdf )'
    print(parChecker(symbol_string))


if __name__ == '__main__':
    main()