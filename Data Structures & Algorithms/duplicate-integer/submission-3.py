class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repdict = {}
        for elem in nums: 
            if elem in repdict:
                return False
            else: 
                repdict[elem] = 1
        return True
        
            
            
        