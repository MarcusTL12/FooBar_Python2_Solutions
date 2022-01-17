import itertools


def solution(num_buns, num_req):
    keys = [[] for _ in range(num_buns)]
    for (i, j) in enumerate(
            itertools.combinations(range(num_buns), num_buns - num_req + 1)):
        for k in j:
            keys[k].append(i)

    return keys


print(solution(2, 1))
print(solution(4, 4))
print(solution(5, 3))
