class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0 or r >= len(board)
                or c < 0 or c >= len(board[0])
                or board[r][c] == "*"
                or board[r][c] != word[i]
            ):
                return False

            tmp = board[r][c]
            board[r][c] = "*"
            ret = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            board[r][c] = tmp
            return ret

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False