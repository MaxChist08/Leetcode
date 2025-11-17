def integer_replacement(n):
    """
    SOLUTION with BFS

    Queue = list()
    Queue.append((n, 0))

    ans = 1000000

    while len(Queue):
        first = Queue[0]
        Queue.pop(0)

        if first[0] == 1:
            ans = min(ans, first[1])
        else:
            if first[0] % 2 == 0:
                Queue.append((first[0] // 2, first[1] + 1))
            else:
                Queue.append((first[0] + 1, first[1] + 1))
                Queue.append((first[0] - 1, first[1] + 1))

    return ans
    """

    ans = 0

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            if n % 4 == 3 and n != 3:
                n += 1
            else:
                n -= 1
        ans += 1

    return ans