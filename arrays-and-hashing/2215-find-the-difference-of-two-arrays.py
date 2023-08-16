class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        answer = [[],[]]
        for i in nums1:
            if i not in nums2 and i not in answer[0]:
                answer[0] += [i]
        for j in nums2:
            if j not in nums1 and j not in answer[1]:
                answer[1] += [j]
        return answer