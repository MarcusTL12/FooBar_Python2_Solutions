from fractions import Fraction


def check_non_negative(diffs, r):
    for d in diffs:
        if r < 1:
            return False
        r = d - r
    return r >= 1


def solution(pegs):
    diffs = [pegs[i + 1] - pegs[i] for i in range(len(pegs) - 1)]
    sgn = 1
    dd = 0
    for i in range(len(diffs)):
        dd += sgn * diffs[i]
        sgn = -sgn

    if len(pegs) % 2 != 0:
        r = 2 * dd
    else:
        r = Fraction(2 * dd, 3)

    if check_non_negative(diffs, r):
        return [r.numerator, r.denominator]
    else:
        return [-1, -1]
