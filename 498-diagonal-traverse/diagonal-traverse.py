class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        res = []

        up = True

        cur_row = cur_col = 0

        while len(res) != rows * cols:
            if up:
                while cur_row >= 0 and cur_col < cols:
                    res.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                
                up = False
            else:
                while cur_col >= 0 and cur_row < rows:
                    res.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                
                if cur_row == rows:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                
                up = True
        
        return res