import itertools


def still_possible(p, c, i, j):
    if i < 0 or j < 0 or i >= len(c) or j >= len(c[0]):
        return True
    amt_false = amt_true = amt_none = 0
    for k in [0, 1]:
        for l in [0, 1]:
            el = p[i + k][j + l]
            if el == False:
                amt_false += 1
            elif el == True:
                amt_true += 1
            elif el == None:
                amt_none += 1
    if c[i][j] and (amt_true > 1 or (amt_true == 0 and amt_none == 0)):
        return False
    elif not c[i][j] and amt_true == 1 and amt_none == 0:
        return False
    else:
        return True


def count_from_col(p, c, j, memo):
    if j != 0:
        prevcol = tuple([row[j - 1] for row in p])
    else:
        prevcol = None

    if (j, prevcol) in memo:
        return memo[(j, prevcol)]

    counter = 0

    for col in itertools.product([False, True], repeat=len(p)):
        for i, v in enumerate(col):
            p[i][j] = v
        if all(still_possible(p, c, i, j - 1) for i in range(len(p))) and \
                all(still_possible(p, c, i, j) for i in range(len(p))):
            if j == len(p[0]) - 1:
                counter += 1
            else:
                counter += count_from_col(p, c, j + 1, memo)
        for i in range(len(p)):
            p[i][j] = None

    memo[(j, prevcol)] = counter
    return counter


def solution(g):
    p = [[None] * (len(g[0]) + 1) for _ in range(len(g) + 1)]
    return count_from_col(p, g, 0, {})


print(solution([[True, True, False, True, False,
                 True, False, True, True, False],
                [True, True, False, False, False,
                 False, True, True, True, False],
                [True, True, False, False, False,
                 False, False, False, False, True],
                [False, True, False, False, False,
                 False, True, True, False, False]]))
