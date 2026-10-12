class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        one = m-1
        two = n-1
        pos = m+n-1

        while two > -1:
            if one >= 0 and nums1[one] > nums2[two]:
                nums1[pos] = nums1[one]
                one-=1
            else:
                nums1[pos] = nums2[two]
                two-=1
            
            pos-=1

        