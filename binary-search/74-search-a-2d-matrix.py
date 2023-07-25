class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # We can just use endpoints to pinpoint which row target could be in
        # Then we preform binary search on that row

        def inRange(row):
            # output > 0 if target is greater
            # output < 0 if target is smaller
            # output == 0 if target is in
            # assumes row is sorted
            if row[0] <= target <= row[-1]:
                return 0
            if target < row[0]:
                return -1
            if target > row[-1]:
                return 1
        
        def search(row):
            return target in row

        # First we search the matrix for the corresponding row
        left, right = 0, len(matrix) - 1
        while (left <= right):
            mid = (left + right) // 2
            row = matrix[mid]
            result = inRange(row)
            if result < 0:
                # print(f"Target {target} is below {row}, so we shift up a row.")
                right = mid - 1
            elif result > 0:
                # print(f"Target {target} is above {row}, so we shift up.")
                left = mid + 1
            else:
                return search(row)

        return False

        