from typing import List

class MaxSubArraySumLessThanK:
    def maxSubArray(self, A: List[int], K:int)->int:
        maxSum: int
        lowInd: int
        highInd: int

        for j in range(len(A)):

