def num_rescue_boats(people, limit):
    people = sorted(people)
    ans = 0
    j = -1

    for i in range(len(people) - 1, -1, -1):
        if i <= j:
            return ans
        if people[j + 1] + people[i] <= limit:
            j += 1
        ans += 1

    return ans