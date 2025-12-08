def calculate(s):
    nums = list()
    operations = list()

    num = ""

    for i in range(len(s)):
        if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
            nums.append(int(num))
            num = ""
            operations.append(s[i])
        else:
            num += s[i]

    nums.append(int(num))

    stack = list()
    stack.append(nums[0])

    i = 1

    while i < len(nums):
        if operations[i - 1] == '+':
            stack.append(nums[i])
        elif operations[i - 1] == '-':
            stack.append(-nums[i])
        elif operations[i - 1] == '*':
            n = stack[-1]
            stack.pop()
            stack.append(nums[i] * n)
        else:
            n = stack[-1]
            stack.pop()
            if n // nums[i] < 0:
                stack.append(-(abs(n) // abs(nums[i])))
            else:
                stack.append(n // nums[i])
        i += 1

    ans = 0
    while len(stack) > 0:
        ans += int(stack[-1])
        stack.pop()

    return ans