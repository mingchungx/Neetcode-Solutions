class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        # To generate the next row, we'll always refer to triangle[-1] (last)
        triangle = [[1], [1, 1], [1, 2, 1]]

        def generateRow(prev):
            # Exclude the ends (1s)
            row = [1]
            j = 1
            for i in range(1, len(prev)):
                row.append(prev[i] + prev[i - 1])
            row.append(1)
            return row
                

        for i in range(numRows - 3):
            prev = triangle[-1]
            row = generateRow(prev)
            triangle.append(row)

        return triangle