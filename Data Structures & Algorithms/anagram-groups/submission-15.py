from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            s_sorted = tuple(sorted(s))
            groups[s_sorted].append(s)

            
        return list(groups.values())

        
        
        