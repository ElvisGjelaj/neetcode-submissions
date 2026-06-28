class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = Counter(s1)
        counts2 = Counter(s2[:len(s1)])

        if counts1 == counts2: 
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            counts2[s2[l]] -= 1
            counts2[s2[r]] += 1
            l += 1

            if counts1 == counts2:
                return True
        return False

            