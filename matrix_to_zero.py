class Solution:
    def setZeroes(matrix) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):  # iterate over columns for the first row
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(m):  # iterate over rows for the first column
                matrix[i][0] = 0

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution.setZeroes(matrix)
    print(matrix)
    
main()