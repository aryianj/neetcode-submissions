class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str: str = ""
        for s in strs:
            encoded_str = encoded_str + str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        strs : List[str] = []
        tempStr : str = ""
        temp : int = 0
        i : int = 0

        if len(s) == 2:
            strs.append("")
            return strs
        
        while i <len(s):
            while s[i].isdigit():
                tempStr = tempStr + s[i]
                i += 1
            if tempStr:
                temp = int(tempStr)
                tempStr = ""
                i += 1
                strs.append(s[i: i + temp])
                i = (i + temp)
        return strs
            




