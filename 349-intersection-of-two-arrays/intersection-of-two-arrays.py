class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        unique = set()
        intersec = list()
        added = set()
        for i in range(len(nums1)):
            if nums1[i] not in unique:
                unique.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] in unique and nums2[i] not in added:
                intersec.append(nums2[i])
                added.add(nums2[i])
                    
        return intersec