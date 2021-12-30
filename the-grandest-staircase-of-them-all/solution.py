def rec(n_brick, max_heigth, memo):
    if (n_brick, max_heigth) in memo:
        return memo[(n_brick, max_heigth)]
    amt_stairs = 0
    for bricks_here in range(1, min(n_brick, max_heigth) + 1):
        if bricks_here == n_brick:
            amt_stairs += 1
        else:
            amt_stairs += rec(n_brick - bricks_here, bricks_here - 1, memo)
    memo[(n_brick, max_heigth)] = amt_stairs
    return amt_stairs


def solution(n):
    memo = {(0, 0): 0}
    return rec(n, n - 1, memo)


print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(200))
