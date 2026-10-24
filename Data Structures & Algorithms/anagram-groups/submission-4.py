class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if temp not in d:
                d[temp] = []
            d[temp].append(strs[i])
        
        for key in d.keys():
            ans.append(d[key])
        return ans 
