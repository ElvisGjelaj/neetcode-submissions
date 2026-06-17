class Solution:
    # encodes prefix length (converted to char) + delimiter "$" ex. "5$Hello"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "$" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i 

            while s[j] != "$":
                j += 1

            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            decoded_list.append(s[word_start:word_end])
            i = word_end

        return decoded_list
            
            
            
