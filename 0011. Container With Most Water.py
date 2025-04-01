def max_area(height):
    value = 0

    start = 0
    finish = len(height) - 1

    while start != finish:
        value = max(value, min(height[start], height[finish]) * (finish - start))
        if height[start] >= height[finish]:
            finish -= 1
        else:
            start += 1

    return value