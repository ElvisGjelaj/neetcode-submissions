class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for char in strs[0]:
            prefix = prefix + char
            for word in strs:
                if prefix not in word:
                    prefix = prefix[:-1]
                    return prefix
        return prefix