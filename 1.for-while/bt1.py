# Con xúc xắc có 6 mặt (mặt số 1 đến số 6). 
# Viết chương trình mô phỏng ném con xúc xắc 10000 lần và đếm số lần xuất hiện của mỗi mặt.
import random


def dice(n):
    side_1 = 0
    side_2 = 0
    side_3 = 0
    side_4 = 0
    side_5 = 0
    side_6 = 0
    for i in range(n):
        side = random.randint(1, 6)
        if side == 1:
            side_1 += 1
        elif side == 2:
            side_2 += 1
        elif side == 3:
            side_3 += 1
        elif side == 4:
            side_4 += 1
        elif side == 5:
            side_5 += 1
        elif side == 6:
            side_6 += 1
    return "side_1:", side_1, "side_2:", side_2, "side_3:", side_3, "side_4:", side_4, "side_5:", side_5, "side_6:", side_6


dice(10000)
