class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        """ d=distance to cycle entrance
            m=distance from cycle entrance to meeting
            c=distance of one cycle
            slow = 1x speed, fast = 2x speed
            at m slow traveled (d+m) and fast traveled 2(d+m)
            we know fast might have made a 1 or more since it entered cycle first. 
            kc = 2(d+m) - (d+m) because its distance fast traveled minus the distance before
            it started a cycle. then kc = d+m, and so m = kc - d. so this means meeting spot 
            have same distance to entrance if we allow the meeting spot to cycle k times and
            if they are the same speed.
            """
        # finds meeting spot
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # finds entrance of cycle
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return fast
            

