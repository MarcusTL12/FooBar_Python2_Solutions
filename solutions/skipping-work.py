def solution(x, y):
    s1 = set(x)
    s2 = set(y)
    if len(s1) > len(s2):
        return s1.difference(s2).pop()
    else:
        return s2.difference(s1).pop()
