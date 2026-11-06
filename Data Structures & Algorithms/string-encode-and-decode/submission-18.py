class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str: str = ""
        for s in strs:
            encoded_str = encoded_str + str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs : List[str] = []
        temp : int = 0
        i : int = 0

        if len(s) == 2:
            strs.append("")
            return strs
        
        while i < len(s):
            ls: str = ""
            while s[i].isdigit():
                ls += s[i]
                i += 1
            if ls:
                i += 1
                strs.append(s[i: i + int(ls)])
                i += int(ls)
        return strs
            




