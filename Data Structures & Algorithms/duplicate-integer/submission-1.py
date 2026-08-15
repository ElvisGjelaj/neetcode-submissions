class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repdict = {}
        for elem in List: 
            if elem in repdict:
                return false
            else: 
                repdict[elem] = 1
        return true
        
            
            
        