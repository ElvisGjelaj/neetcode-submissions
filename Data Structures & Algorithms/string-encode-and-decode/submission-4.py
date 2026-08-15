class Solution:
    # encodes prefix length (converted to char) + delimiter "$" ex. "5$Hello"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for string in strs:
            length = len(string)
            encoded_str += chr(length)
            encoded_str += "$"
            encoded_str += string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        length = ""
        inWord = False
        curr_Word = ""
        for char in s:
            if char == "$":
                inWord = True
                length = int("".join(str(ord(chara))) for chara in length)
            if not inWord:
                length += char
            if inWord:
                curr_Word += char
                length -= 1
                if length == 0:
                    inWord = False
                    decoded_list.append(curr_word)
                    curr_word = ""
        return decoded_list
            
            
            
