class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for r in range(m):
            for c in range(n):
                cell = board[r][c]

                # skip empty cells.
                if cell == ".":
                    continue

                # if repeated value, return false.
                elif (
                    cell in rows[r] or
                    cell in cols[c] or
                    cell in sqrs[(r//3, c//3)]
                ):
                    return False
                
                # collect cell for validation.
                rows[r].add(cell)
                cols[c].add(cell)
                sqrs[(r//3, c//3)].add(cell)

        return True