class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            if  target in matrix[0]:
                return True
            else:
                return False
        low=0
        high=len(matrix)-1
        row_len=len(matrix[0])-1
       # mid = (high+low)//2
        # check if target is greater than or less than row start
        # if in range of a row need to check the row
        while (low<= high):
            #find the right row where number is , then itrarte through
            mid=( low + high)//2
            if target in matrix[mid]:
                for num in matrix[mid]:
                    if num==target:
                        return True
            if target> matrix[mid][len(matrix[mid])-1]:
                low = mid + 1
            else :
                high = mid - 1
        return False