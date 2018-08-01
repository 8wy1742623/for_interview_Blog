"""
WHAT
练习使用 ipdb 调试代码

HOW
运行：ipython --ipdb test_01.py
"""

s = 0

for c in ['a', 'b', 1]:
    from ipdb import set_trace; set_trace()
    s += c()
