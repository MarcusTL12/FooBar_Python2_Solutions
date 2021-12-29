def trig_num(n):
    return ((n + 1) * n) >> 1


def solution(x, y):
    return str(trig_num(x + y - 1) - y + 1)

