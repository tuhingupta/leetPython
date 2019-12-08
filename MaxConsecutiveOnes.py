from typing import List

"""

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

Find the longest subarray with at most K zeros.
"""
class MaxConsecutiveOnes:
    def __init__(self):
        pass

    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1


if __name__ == '__main__':
    my_max = MaxConsecutiveOnes()
    print("running max")
    print(my_max.longestOnes([1,0,0,1,1,1,0], 2))