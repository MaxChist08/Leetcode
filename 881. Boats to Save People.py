people = [1,2, 1]
limit = 3

people = sorted(people)
ans = 0

while len(people) != 0:
    big_index = len(people) - 1
    small_index = -1
    while small_index < big_index and people[small_index + 1] <= limit - people[big_index]:
        small_index += 1
    people.pop(big_index)
    print(people, small_index)
    if len(people) > 0 and small_index != -1:
        people.pop(small_index)

    ans += 1

print(ans)
