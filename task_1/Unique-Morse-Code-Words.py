class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morsed_code = set()
        for word in words:
            code = ""
            for char in word:
                 code += morse[ord(char) - ord("a")]
            morsed_code.add(code)
        return len(morsed_code)