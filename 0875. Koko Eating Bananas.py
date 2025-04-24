def min_eating_speed(piles, h):
    def t(speed):
        time = 0
        for x in piles:
            time += x // speed
            if x % speed != 0:
                time += 1
        return time

    start = 1
    finish = 0
    for x in piles:
        finish = max(x, finish)

    while start <= finish:
        middle = (start + finish) // 2
        if t(middle) <= h:
            finish = middle - 1
        else:
            start = middle + 1
    return start