def longest_palindrome(s):
    ans = s[0]

    dynamic_matrix = list()
    for i in range(len(s)):
        dynamic_matrix.append([0] * len(s))

    for i in range(len(s)):
        dynamic_matrix[i][i] = 1

    for i in range(len(s)):
        if i + 1 >= len(s):
            break
        if s[i] == s[i + 1]:
            dynamic_matrix[i][i + 1] = 1
            ans = s[i:i + 2]

    for i in range(2, len(s)):
        for j in range(len(s)):
            if j + i >= len(s):
                break
            if s[j] == s[j + i] and dynamic_matrix[j + 1][i + j - 1] == 1:
                dynamic_matrix[j][j + i] = 1
                ans = s[j:j + i + 1]

    return ans