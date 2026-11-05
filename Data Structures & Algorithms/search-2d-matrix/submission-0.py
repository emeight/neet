class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # determine the row
        for i in reversed(range(m)):
            # walk backwards, if lead val is less it must be in this row
            if matrix[i][0] <= target:
                break

        # slice out the row
        row = matrix[i]

        # determine the column, stand high / low
        high = n - 1
        low = 0
        while low <= high:
            # calc midpoint
            mid = low + ((high - low) // 2)
            
            if row[mid] < target:
                low = mid + 1
            elif row[mid] > target:
                high = mid - 1
            else:
                # found it
                return True

        return False
        