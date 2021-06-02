class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            print(matrix[i][n-1])
            if target <= matrix[i][n-1]:
                if target == matrix[i][n-1] or target == matrix[i][0]: return True
                return self.binarySearch(matrix[i], target)
        return False
    
    def binarySearch(self, arr, target):
        l = 0
        r = len(arr)-1
        while l<=r:
            
            mid = (l+r)//2
        
            if arr[mid] == target: 
                return True
            elif arr[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return 
        