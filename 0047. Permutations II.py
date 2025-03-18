def multiply(num1, num2):
    nums = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    string = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}

    num1int = 0
    num2int = 0

    for x in num1:
        num1int = num1int * 10 + nums[x]

    for x in num2:
        num2int = num2int * 10 + nums[x]

    ans = num1int * num2int
    ans_str = ""

    while ans > 9:
        ans_str = string[ans % 10] + ans_str
        ans //= 10

    ans_str = string[ans] + ans_str

    return ans_str