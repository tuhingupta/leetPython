from typing import List

'''
__author__ = "Tuhin Gupta"

Given an array of integers and a sum. We have to find sum of subarray having maximum sum less than or equal to given sum in array.
Input : arr[] = { 1, 2, 3, 4, 5 }
        sum = 11
Output : 10
Subarray having maximum sum is { 1, 2, 3, 4 }

Input : arr[] = { 2, 4, 6, 8, 10 }
        sum = 7
Output : 6
Subarray having maximum sum is { 2, 4 } or { 6 }

https://www.geeksforgeeks.org/maximum-sum-subarray-sum-less-equal-given-sum/
'''
class MaxSubArrayLessThanK:

    def __init__(self, A:List[int], K:int):
        super().__init__()
        self.A = A
        self.K = K
        
        j=0

        self.sum = A[j]
        self.low = 0
        self.high = j
        
        #these are variables are just there for final max params to print
        self.maxS = A[j]
        self.maxL = 0
        self.maxH = j
        
        #recursion starts
        self.findMax(j+1)
        print(f"L={self.maxL}, H={self.maxH}, S={self.maxS}")

    def findMax(self, j:int):

        if(j < len(self.A)):
            #if next element added is still less than passed in K
            if (self.sum + self.A[j] < self.K):
                self.sum += self.A[j]
                self.high = j
            else:
                sumA = self.sum + self.A[j]
                #sliding window: keep decreasing the window of array so that sum is less than K
                while(sumA > self.K and self.low < j):
                    sumA = sumA - self.A[self.low]
                    self.low +=1 
                
                self.high = j
                self.sum = sumA

            if(self.sum > self.maxS):
                self.maxS = self.sum
                self.maxL = self.low
                self.maxH = self.high
            
            self.findMax(j+1)

        else:
            return


if __name__ == '__main__':
    MaxSubArrayLessThanK([1,2,3,4,5,6], 13)
    print("program ends.")
    
            
