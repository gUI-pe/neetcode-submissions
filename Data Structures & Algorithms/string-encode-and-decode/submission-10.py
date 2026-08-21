class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        print(encoded_string)

        for string in strs:
            size = len(string)

            encoded_string += str(size) + "#" + string        

        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0

        while i < (len(s)): #delimeter = size#
            j = i
            while s[j] != "#":
                j += 1
            
            size = int(s[i:j])

            decoded_strs.append(s[j + 1: j + 1 + size])
            i = j + 1 + size

        return decoded_strs
