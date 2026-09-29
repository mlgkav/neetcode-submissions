class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Standard split + filtering handles consecutive and trailing slashes automatically
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion and portion != ".":  # 'if portion' filters out ""
                stack.append(portion)
                
        return "/" + "/".join(stack)
