class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A)) < 3:
            return False

        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i += 1

        if i == 1 or i == len(A): # line
            return False # line

        while i < len(A) and A[i] < A[i-1]: # while not if
            i += 1

        return i == len(A) # reached the end of the array
