class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        string = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}

        num1int = 0
        num2int = 0

        for x in num1:
            num1int = num1int * 10 + nums[x]

        for x in num2:
            num2int = num2int * 10 + nums[x]

        ans = num1int * num2int
        ansstr = ""

        while ans > 9:
            ansstr = string[ans % 10] + ansstr
            ans //= 10

        ansstr = string[ans] + ansstr

        return ansstr