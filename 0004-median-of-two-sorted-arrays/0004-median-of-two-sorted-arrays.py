class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        li = (nums1+nums2)
        li.sort()
        size = len(li)
        if size % 2 == 0:
            return ((li[size/2] + li[(size/2)-1])/2.0)
        else:
            return (li[(size//2)])