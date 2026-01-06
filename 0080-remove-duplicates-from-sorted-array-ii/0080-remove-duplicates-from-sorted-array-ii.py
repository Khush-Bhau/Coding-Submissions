class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array has 2 or fewer elements, we can keep all of them.
        if len(nums) <= 2:
            return len(nums)
        
        # Initialize the write_index (k) at 2.
        # We start at 2 because the first two elements (indices 0 and 1) 
        # are always kept in a sorted array (at most 2 duplicates allowed).
        k = 2
        
        # Iterate through the array starting from the third element.
        for i in range(2, len(nums)):
            # Compare the current element (nums[i]) with the element 
            # two positions back in our "valid" portion (nums[k-2]).
            # If they are different, it means we haven't added this number 
            # more than twice yet.
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
                
        return k