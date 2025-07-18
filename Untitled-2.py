print("猜数字游戏")
import random
num = random.choice(range(1, 101))

aaaaa = 0
while aaaaa == 0:
    sum = int(input("请猜一个1-100的数字："))
    if sum < num:
        print("猜小了哦(*´・ｖ・)")
    elif sum > num:
        print("猜大了哦(*´・ｖ・)")
    else:
        print("恭喜你，猜对了！(^_^)")
        aaaaa = 1  # 退出循环
