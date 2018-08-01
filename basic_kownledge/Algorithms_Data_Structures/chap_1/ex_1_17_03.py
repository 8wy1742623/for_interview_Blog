"""
15. 在当地报纸上找一个数独谜题，写一个程序来解决它。
    先解决入门级别的数独
    Q: 需要哪些方法解决入门级数独问题?
    A: 
    一, 筛选出三个列表中仅有一个空格的列表, 填充它. 这就够用吗? 需要试一试.
       
    
1, 录入数独表: OK
    [[...][...]...9个...[...]]
    空格填0.

2, 收集三种列表: 行row, 列column, 九宫格sudoku_9.

3, 利用方法解出空格.
    把 0 改为1-9之间的数字.

4, 打印: OK
    123 456 798
    xxx xxx xxx
    xxx xxx xxx

(pdb 运行文件
ipython --pdb xx.py)
"""
import logging
# import random

logging.basicConfig(level='WARNING')


def typing_sodoku():
    # input()
    rows_1 = [2, 0, 0, 6, 0, 3, 0, 0, 0]
    rows_2 = [0, 0, 0, 0, 1, 0, 0, 0, 8]
    rows_3 = [0, 5, 4, 0, 0, 0, 0, 0, 0]
    rows_4 = [7, 0, 0, 5, 4, 6, 8, 0, 0]
    rows_5 = [3, 0, 0, 0, 8, 9, 1, 0, 0]
    rows_6 = [0, 0, 2, 0, 7, 0, 4, 9, 5]
    rows_7 = [4, 0, 6, 0, 3, 2, 9, 5, 1]
    rows_8 = [5, 2, 9, 1, 0, 4, 0, 8, 3]
    rows_9 = [1, 8, 3, 9, 0, 7, 2, 0, 6]
    return [
        rows_1, rows_2, rows_3, rows_4, rows_5, rows_6, rows_7, rows_8, rows_9
    ]

def print_sodoku(l):
    i = 0
    for row in l:
        row_2_str = str(row)[1:-1]
        format_row = (row_2_str[0:9] + " " + 
            row_2_str[9:18] + " " + row_2_str[18:])
        print(format_row)
        i += 1
        if i % 3 == 0:
            print()
    

def main():
    print('Game Begin.')
    l = typing_sodoku()
    print_sodoku(l)


if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=True)
