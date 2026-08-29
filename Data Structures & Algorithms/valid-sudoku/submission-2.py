class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for i in range(len(board))]
        columns = [set() for i in range(len(board))]
        rows = [set() for i in range(len(board))]

        #box indexing = ((r//3) + (c//3)*3)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                boxi = (r//3) + (c//3)*3

                if num == ".":
                    continue

                if (num in boxes[boxi]) or (num in columns[c]) or (num in rows[r]):
                    return False
                
                boxes[boxi].add(num)
                columns[c].add(num)
                rows[r].add(num)

        return True