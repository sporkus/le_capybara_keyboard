import math
import sys

def polar_to_cartesian(degrees, radius):
    radians = math.radians(degrees)
    d = 4
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    return round(x, 4), round(y, 4)

if __name__ == "__main__":
    r = float(sys.argv[1])

    for i in range(360):
        if i % 5 == 0:
            print("(xy", *polar_to_cartesian(i, r), ")")
