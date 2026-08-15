class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repdict = {}
        for elem in nums: 
            if elem in repdict:
                return True
            else: 
                repdict[elem] = 1
        return False
        
            
            
        