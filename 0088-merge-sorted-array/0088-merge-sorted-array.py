class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = list(iterate_sorted_nums(nums1[:m], nums2))

def iterate_sorted_nums(nums1, nums2):
    i,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            yield nums1[i]
            i += 1
        else:
            yield nums2[j]
            j += 1
    while i < len(nums1) or j < len(nums2):
        if i < len(nums1):
            yield nums1[i]
            i += 1
        else:
            yield nums2[j]
            j += 1