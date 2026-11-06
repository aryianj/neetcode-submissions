class Solution:
    def encode(self, strs: List[str]) -> str:
        ec : str = ""
        for strx in strs:
            lenx : int = len(strx)
            ec = ec + str(lenx) + "#" + strx
        return ec

    def decode(self, s: str) -> List[str]:
        strs : List[str] = []
        tempStr : str = ""
        temp : int = 0
        i : int = 0

        if len(s) == 2:
            strs.append("")
            return strs
        
        while i <len(s):
            while s[i].isdigit() and s[i] is not "#":
                tempStr = tempStr + s[i]
                i += 1
            if tempStr:
                temp = int(tempStr)
                tempStr = ""
                i += 1
                strs.append(s[i: i + temp])
                i = (i + temp)
        return strs
        