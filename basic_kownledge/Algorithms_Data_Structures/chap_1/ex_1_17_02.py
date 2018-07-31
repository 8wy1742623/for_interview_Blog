"""
14. 设计一个类表示一个张扑克牌。一个类代表一副牌。
    使用这两个类实现一个你喜欢的扑克牌游戏。
    21点 vs 电脑。

"""
import logging
import random

# 使用这个可以：
# py 运行此文件时，出现错误，进入ipdb调试模式。
import crash_on_ipy

logging.basicConfig(level='WARNING')


# ==============================================
# 14
class Card():
    deck_dict = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
    }


class Deck_cards:
    """一套牌，52张（去掉了大小王）。
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


def sum_cards(hand_cards):
    """对手牌的点数求和
    WHAT
    hand_cards: ['A', '3', 'J']
    return: 14(int)
    
    HOW
    借助 Card() 类中的字典，由'A'得到数值1。
    求得列表['A', '3', 'J']所代表的数值的和。
    """
    sum = 0
    for card in hand_cards:
        sum += Card().deck_dict[card]
        logging.info(sum)
    return sum

def whether_ai_req_card(ai_points):
    """根据ai手牌得分，判断ai是否继续要牌
    WHAT
    hand_cards: 13
    return: True / False
    HOW
    期望：从52张牌中获得的牌的点数的期望，6.5。
    逻辑：手牌点数加上期望>21,不要牌，否则要牌。
    (注解：这里没有动态的计算期望，而是使用的原始状态下的牌库的期望。
    可能不太麻烦，但暂时没这样做。)
    """
    if ai_points + 6.5 > 21:
        return False
    else:
        return True


def play_a_turn():
    # 开始游戏
    print("********************************")
    print("The 21p Game Starts.")

    # 初始化玩家的手牌和分数
    player_cards = []
    player_points = 0
    # 初始化 AI 的手牌和分数
    ai_cards = [] 
    ai_points = 0
    # 初始化一套牌库
    decks = Deck_cards()

    # ai，玩家各发两张牌
    player_cards.append(decks.pack_card())
    ai_cards.append(decks.pack_card())
    player_cards.append(decks.pack_card())
    ai_cards.append(decks.pack_card())
    print("You would get 2 cards.")

    # 初始化ai与player的请求(要/不要牌)
    req_ai = True
    req_p = True

    # 循环: 要牌阶段
    # 条件：ai 或 player 要牌
    while req_ai or req_p:
        print()
        print("The next turn to pack cards...")
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
                    # 向玩家展示获得的手牌
                    print("Your cards in hand:%s" % str(player_cards)[1:-1])
                    break
                elif judge == 'N' or judge == 'n':
                    req_p = False
                    break
                else:
                    print("Input Y or N instead.")
            # 计算玩家手牌的点数
            # TODO 07-31
            player_points = sum_cards(player_cards)
            # 判断点数，不爆继续向下的流程，爆牌判负跳出循环。
            if player_points > 21:
                print("Your Point is %s over 21. You lost." % player_points)
                print("********************************")
                print()
                return None

        # 判断ai请求，上一个请求是不要牌，则跳过ai步骤
        if req_ai:
            # ai判断是否要牌
            req_ai = whether_ai_req_card(ai_points)
            if req_ai:
                #  发牌给ai
                ai_cards.append(decks.pack_card())
                # 判断点数，不爆继续向下的流程，爆牌判负跳出循环。
                ai_points = sum_cards(ai_cards)
                if ai_points > 21:
                    print("AI Point is %s over 21. You Win!" % ai_points)
                    print("********************************")
                    print()
                    return None
    # 判断胜负
    if ai_points < player_points:
        print("Your Point: %s" % player_points)
        print("AI Point: %s" % ai_points)
        print("Your Point is over AI. You win!")
        print("********************************")
        print()
    elif ai_points > player_points:
        print("Your Point: %s" % player_points)
        print("AI Point: %s" % ai_points)
        print("AI Point is over you. You lost. Good luck next time!")
        print("********************************")
        print()
    else:
        print("Your Point: %s" % player_points)
        print("AI Point: %s" % ai_points)
        print("Your Point is equal to AI. It's a draw this time.")
        print("Good luck next time!")
        print("********************************")
        print()


def play_21_point():
    while True:
        play_a_turn()


def main():
    play_21_point()

if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod(verbose=True)
