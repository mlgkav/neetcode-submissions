class Solution:

    def encode(self, strs: List[str]) -> str:
        # use length of string followed by delimeter to denote the end of the value
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res


"""
This solution works because beggining of each string is guaranteed to start with "{string length}#"
"""