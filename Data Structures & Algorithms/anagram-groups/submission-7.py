class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_strs = []
        group_dicts = []
        first = True
        for word in strs:
            word_dict = self.makedictAnagram(word)
            if first == True:
                group_dicts.append(word_dict)
                group_strs.append([word])
                first = False
            else:
                matched = False
                for idx, group_dict in enumerate(group_dicts):
                    if group_dict == word_dict:
                        group_strs[idx].append(word)
                        matched = True
                        break
                if not matched:
                    group_dicts.append(word_dict)
                    group_strs.append([word])
        return group_strs

    def makedictAnagram(self, word: str) -> dict:
        seen = {}
        for char in word:
            try: 
                seen[char] += 1
            except KeyError:
                seen[char] = 1
        return seen
    
