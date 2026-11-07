class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for s in strs:
            encodedString += "#" + str(len(s)) + "#" + s
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []
        i = 0
        while i < len(s):
            n = ""
            if s[i] == "#":
                while s[i+1].isdigit():
                   n += s[i+1]
                   i += 1
            n = int(n)
            decodedList.append(s[i+2:i+n+2])
            i += n + 2
        return decodedList