class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ans = 0

        d = dict()
        k = 0

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
                k+=1
            else:
                if i - d[s[i]] > k:
                    k+=1
                    d[s[i]] = i
                else:
                    ans = max(ans, k)
                    k = i - d[s[i]]
                    d[s[i]] = i

        return max(ans, k)"""

        d = set()
        i = 0
        r = 0
        ans = 0

        while i < len(s):
            if s[i] not in d:
                d.add(s[i])
                ans = max(ans, len(d))
                i += 1
            else:
                if s[i] in d:
                    d.remove(s[r])
                    r += 1

        return max(ans, len(d))

print(bin(23))