def min_eating_speed(piles, h):
    def f(speed):
        time = 0
        for x in piles:
            time += x // speed
            if x % speed != 0:
                time += 1
        return time

    start = 1
    finish = 0
    for x in piles:
        finish += x

    while start <= finish:
        middle = (start + finish) // 2
        if f(middle) <= h:
            finish = middle - 1
        else:
            start = middle + 1
    return start