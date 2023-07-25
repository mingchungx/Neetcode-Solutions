class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        # Swapping rows
        for i in range(n):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
            matrix[i] = matrix[i][::-1]

        # Transposing
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]