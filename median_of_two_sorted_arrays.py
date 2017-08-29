class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        lenth = len(nums1)
        new_nums = sorted(nums1)

        if lenth % 2 == 0:
            return (new_nums[lenth/2] + new_nums[lenth/2 -1])/float(2)
        else:
            return new_nums[lenth/2]