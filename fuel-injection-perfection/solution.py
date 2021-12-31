def solution(n):
    n = int(n)

    ans = 0

    while n > 3:
        ans += 1
        if n % 2 == 0:
            n >>= 1
        else:
            if n & 2 == 0:
                n -= 1
            else:
                n += 1

    return ans + n - 1
