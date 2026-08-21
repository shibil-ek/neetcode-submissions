class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for string in strs:
            key="".join(sorted(string))
            if key in d:
                d[key].append(string)
            else:
                d[key] = [string]

        return list(d.values())

