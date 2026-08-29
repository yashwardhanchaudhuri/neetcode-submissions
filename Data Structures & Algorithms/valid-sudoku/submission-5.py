class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):

                num = board[r][c]

                if num == ".":
                    continue

                col = (c, num, "c")
                row = (r, num, "r")
                box = ((r//3 + (c//3)*3), num, "b")

                if (col in seen) or (row in seen) or (box in seen):
                    return False
                
                seen.add(col)
                seen.add(row)
                seen.add(box)

        return True