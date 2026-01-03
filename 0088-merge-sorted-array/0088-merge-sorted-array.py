class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Pointer for the last valid element in nums1
        p1 = m - 1
        # Pointer for the last element in nums2
        p2 = n - 1
        # Pointer for the insertion position (end of nums1)
        p = m + n - 1

        # While both arrays have elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are leftover elements in nums2, copy them.
        # Note: We don't need to copy leftover nums1 elements because 
        # they are already in their correct place.
        nums1[:p2 + 1] = nums2[:p2 + 1]