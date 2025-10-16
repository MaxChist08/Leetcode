def is_additive_number(num):
    def F(num, prev_num_1, prev_num_2):
        if len(num) == 0:
            return True

        for i in range(1, len(num) + 1):
            if prev_num_1 + prev_num_2 == int(num[:i]) and str(int(num[:i])) == num[:i]:
                if F(num[i:], prev_num_2, int(num[:i])):
                    return True

        return False

    for i in range(1, len(num) + 1):
        for j in range(1, len(num) - i + 1):
            if str(int(num[:i])) == num[:i] and str(int(num[i:i + j])) == num[i:i + j] and len(num[i + j:]) >= 1:
                if F(num[i + j:], int(num[:i]), int(num[i:i + j])):
                    return True

    return False