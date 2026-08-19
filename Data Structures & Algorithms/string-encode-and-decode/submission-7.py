class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        #print(encoded_string)

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0
        
        word = ""
        while i < (len(s) - 1):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j + 1

            decoded_strs.append(s[i: i + size])
            i = i + size

        return decoded_strs
    
