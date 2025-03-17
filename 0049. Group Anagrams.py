class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        ANS = []
        k = 0

        for x in strs:
            if str(sorted(x)) not in ans.keys():
                ans[str(sorted(x))] = k
                ANS.append(list())
                ANS[k].append(x)
                k+=1
            else:
                ANS[ans[str(sorted(x))]].append(x)

        return ANS