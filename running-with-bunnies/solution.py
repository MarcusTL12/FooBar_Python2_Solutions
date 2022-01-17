import heapq


def set_tuple(t, i, v):
    l = list(t)
    l[i] = v
    return tuple(l)


def solution(times, time_limit):
    bunnies = tuple([False] * (len(times) - 2))
    queue = [(-time_limit, (0, bunnies))]
    visited = {(0, bunnies): -time_limit}

    solutions = [(0, [])]

    while len(queue) != 0:
        time_spent, (pos, bunnies) = heapq.heappop(queue)

        if (pos, bunnies) in visited:
            visited[(pos, bunnies)] = min(visited[(pos, bunnies)], time_spent)
        else:
            visited[(pos, bunnies)] = time_spent

        if pos == len(times) - 1 and time_spent <= 0:
            saved_bunnies = [i for i in range(len(bunnies)) if bunnies[i]]
            solutions.append((-len(saved_bunnies), saved_bunnies))

        for new_pos in range(len(times)):
            if 1 <= new_pos <= len(times) - 2:
                new_bunnies = set_tuple(bunnies, new_pos - 1, True)
            else:
                new_bunnies = bunnies

            k = (new_pos, new_bunnies)

            new_time_spent = time_spent + times[pos][new_pos]

            if k not in visited:
                heapq.heappush(queue, (new_time_spent, k))
            elif visited[k] > new_time_spent:
                # Negative cycle detected, it will be possible to save up
                # time and save all bunnies
                return [i for i in range(len(times) - 2)]

    return min(solutions)[1]


print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))

print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
