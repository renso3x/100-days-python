
from cgi import test

import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_cal(height, width, cover):
    area = (height * width)
    cans = area / cover
    print(f"You need {math.ceil(cans)} to paint the wall")

paint_cal(height=test_h,width=test_w, cover=coverage)