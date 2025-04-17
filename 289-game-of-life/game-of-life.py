class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
      """
      Do not return anything, modify board in-place instead.
      0 - 0 -> 0
      1 - 0 -> 1
      0 - 1 -> 2
      1 - 1 -> 3
      """

      ROWS = len(board)
      COLS = len(board[0])

      def check(r, c):
        population = 0
        for i in range(r - 1, r + 2):
          for j in range(c - 1, c + 2):
            if (
              i < 0 or
              i >= ROWS or
              j < 0 or
              j >= COLS or
              (i == r and j == c)
            ):
              continue
            if board[i][j] in [1, 3]:
              population += 1
        return population
      
      for r in range(ROWS):
        for c in range(COLS):
          population = check(r, c)

          if board[r][c] == 1:
            if population in [2, 3]:
              board[r][c] = 3
          elif board[r][c] == 0:
            if population == 3:
              board[r][c] = 2

      # Update the board to the result
      for r in range(ROWS):
        for c in range(COLS):
          if board[r][c] in [2, 3]:
            board[r][c] = 1
          elif board[r][c] in [0, 1]:
            board[r][c] = 0

        

      