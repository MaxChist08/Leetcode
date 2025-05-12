def number__of_boomerangs(points):
    def find_distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    ans = 0

    for i in range(len(points)):
        distance = dict()

        for j in range(len(points)):
            dist = find_distance(points[i], points[j])
            if dist not in distance:
                distance[dist] = 1
            else:
                distance[dist] += 1

        for j in distance:
            ans += distance[j] * (distance[j] - 1)

    return ans