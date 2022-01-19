from fractions import Fraction


def root2_fraction(n):
    if n == 0:
        return Fraction(1, 1)
    else:
        return 1 + 1 / (1 + root2_fraction(n - 1))


root2 = root2_fraction(500)


def rec(n):
    if n == 0:
        return 0
    np = int((root2 - 1) * n)
    return n * np + (n * (n + 1) - np * (np + 1)) // 2 - rec(np)


def solution(s):
    return str(rec(int(s)))


print(solution('1' + '0' * 100))
