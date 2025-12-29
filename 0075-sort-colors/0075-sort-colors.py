class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0          # Pointer for the end of the 0s
        mid = 0          # Pointer for the current element
        high = len(nums) - 1 # Pointer for the start of the 2s

        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with the 'low' pointer
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1s are in the correct place relative to 0s, just move forward
                mid += 1
            else: # nums[mid] == 2
                # Swap current element with the 'high' pointer
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                # Do NOT increment mid; we need to check the value we just swapped from 'high'