class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        inter = set()

        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in inter:
                    inter.add(nums1[i])

        
        return list(inter)