def climb_stairs(n):
    dynamic_list = [0] * (n + 1)

    dynamic_list[0] = dynamic_list[1] = 1

    for i in range(2, len(dynamic_list)):
        dynamic_list[i] = dynamic_list[i - 1] + dynamic_list[i - 2]

    return dynamic_list[-1]