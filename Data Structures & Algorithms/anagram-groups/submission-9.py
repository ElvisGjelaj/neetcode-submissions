class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            sorted_word = sorted(word)
            if sorted_word not in groups.items():
                groups[sorted_word] = [word]
            else: 
                groups[sorted_word].append(word)
        return list(groups.values())