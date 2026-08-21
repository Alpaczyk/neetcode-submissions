from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            new_s = "".join(sorted(s))
            res[new_s].append(s)
        return list(res.values())
