def solution(x, y):
    x = int(x)
    y = int(y)
    l = 0
    while x > 1 or y > 1:
        if x < 1 or y < 1:
            return "impossible"
        if x < y:
            l += y // x
            y %= x
        elif x > y:
            l += x // y
            x %= y
        else:
            return "impossible"
    return str(l - 1)
