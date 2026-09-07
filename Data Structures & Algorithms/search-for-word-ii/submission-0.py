class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1 
        self.refs = 0 # number of words that pass through the node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build prefix tree
        root = TrieNode()
        for i, word in enumerate(words):
            curr = root
            for c in word:
                child_idx = ord(c) - ord("a")
                if not curr.children[child_idx]:
                    curr.children[child_idx] = TrieNode()
                curr = curr.children[child_idx]
                curr.refs += 1
            curr.idx = i

        res = []
        def dfs(node, r, c):
            if (
                r < 0 or r >= len(board)
                or c < 0 or c >= len(board[0])
                or board[r][c] == "*"
            ):
                return 0

            tmp = board[r][c]
            child_idx = ord(tmp) - ord("a")
            if not node.children[child_idx]:
                return 0

            node, prev = node.children[child_idx], node
            found = 0
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                found += 1

            board[r][c] = "*"
            found += dfs(node, r + 1, c)
            found += dfs(node, r - 1, c)
            found += dfs(node, r, c + 1)
            found += dfs(node, r, c - 1)
            board[r][c] = tmp

            node.refs -= found
            if not node.refs:
                prev.children[child_idx] = None
            return found

        for r in range(len(board)):
            for c in range(len(board[0])):
                root.refs -= dfs(root, r, c)

        return res
            
            