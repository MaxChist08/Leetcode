def strong_password_checker(password):
    nums = "0123456789"
    flag1 = 0
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    flag2 = 0
    big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    flag3 = 0

    for p in password:
        if p in nums:
            flag1 = 1
        elif p in small_letters:
            flag2 = 1
        elif p in big_letters:
            flag3 = 1

    lens = list()

    index = 0
    for i in range(len(password)):
        if password[i] != password[index]:
            if i - index >= 3:
                lens.append(i - index)
            index = i

    if len(password) - index >= 3:
        lens.append(len(password) - index)

    if len(password) < 6:
        ans = 0
        for i in range(len(lens)):
            ans += lens[i] // 3

        return max(6 - len(password), ans, 3 - flag1 - flag2 - flag3)

    elif (len(password) <= 20) and (len(password) >= 6):
        ans = 0
        for i in range(len(lens)):
            ans += lens[i] // 3

        return max(ans, 3 - flag1 - flag2 - flag3)

    else:
        lens = sorted(lens, key=lambda l: l % 3)

        k = len(password) - 20
        for i in range(len(lens)):
            if k >= lens[i] - (lens[i] // 3 * 3 - 1):
                if (lens[i] + 1) % 3 != 0:
                    k -= lens[i] - (lens[i] // 3 * 3 - 1)
                    lens[i] = lens[i] // 3 * 3 - 1
            else:
                lens[i] = lens[i] - k
                k = 0
                break

        for i in range(len(lens)):
            if k < 3:
                break
            if k >= lens[i] - 2:
                k -= lens[i] - 2
                lens[i] = 2
            else:
                lens[i] -= k
                k = 0

        ans = 0
        for i in range(len(lens)):
            ans += lens[i] // 3

        return len(password) - 20 + max(ans, 3 - flag1 - flag2 - flag3)