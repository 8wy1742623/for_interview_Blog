"""
14. 设计一个类表示一个张扑克牌。一个类代表一副牌。
    使用这两个类实现一个你喜欢的扑克牌游戏。
    21点 vs 电脑。

"""
import random

import logging

logging.basicConfig(level='INFO')

# ==============================================
# 14
class card():
    pass


class deck_cards():
    """一套牌，52张（去掉了大小王）。

    >>> decks = deck_cards()
    >>> print(decks.deck_dict)
    """
    deck_dict = {
        'A': 4,
        '2': 4,
        '3': 4,
        '4': 4,
        '5': 4,
        '6': 4,
        '7': 4,
        '8': 4,
        '9': 4,
        '10': 4,
        'J': 4,
        'Q': 4,
        'K': 4,
    }

    # def __init__(self):
    #     pass

    def pack_card(self):
        """发牌
        返回牌名，如‘A’，‘1’"""
        random_card = random.choice(list(self.deck_dict))
        self.deck_dict[random_card] -= 1
        if self.deck_dict[random_card] == 0:
            del self.deck_dict[random_card]
        return random_card


def play_a_turn():
    # 开始游戏
    print("The 21p Game Starts.")

    # 初始化玩家的手牌
    player_cards = []
    # 初始化 AI 的手牌
    ai_cards = []
    # 初始化一套牌库
    decks = deck_cards()

    # ai，玩家各发两张牌
    player_cards.append(decks.pack_card())
    ai_cards.append(decks.pack_card())
    player_cards.append(decks.pack_card())
    ai_cards.append(decks.pack_card())
    print("You would get 2 cards.")

    # 初始化ai与player的请求(要/不要牌)
    req_ai = True
    req_p = True

    # 循环
    # 条件：ai 或 player 要牌
    while req_ai or req_p:
        # 判断玩家请求，上一个请求是不要牌，则跳过玩家步骤
        if req_p:
            # 向玩家展示获得的手牌
            print("Your cards in hand:%s" % str(player_cards)[1:-1])
            # 循环，询问玩家是否继续要牌
            while True:
                print("If you wanna request another card(Y/N)?")
                judge = input()
                if judge == 'Y' or judge == 'y':
                    req_p = True
                    # 发牌给玩家
                    player_cards.append(decks.pack_card())
                    break
                elif judge == 'N' or judge == 'n':
                    req_p = False
                    break
                else:
                    print("Input Y or N instead.")
            # 计算玩家手牌的点数
            # TODO 07-31
            # sum()? 对列表求和？添加到 card 类方法中

            # 计算点数，不爆继续向下的流程，爆牌判负跳出循环。

        # 判断ai请求，上一个请求是不要牌，则跳过ai步骤
        if req_ai:
            # ai判断是否要牌
            #  发牌给ai
            # 计算点数，不爆继续向下的流程，爆牌判负跳出循环。
            pass
        # 判断请求，玩家，
            # ai同时为不要牌，则比较各自牌面总和大小，得出胜负，跳出循环。
            # 否则，回到循环开头


def play_21_point():
    while True:
        play_a_turn()

if __name__ == '__main__':
    # main()
    import doctest
    doctest.testmod(verbose=True)
