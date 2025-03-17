class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""

        flag = True

        for i in range(0, len(strs[0])):
            for j in range(0, len(strs) - 1):
                if i >= len(strs[j + 1]):
                    flag = False
                    break
                if strs[j][i] != strs[j + 1][i]:
                    flag = False
            if flag:
                ans += strs[0][i]
            else:
                break

        return ans
