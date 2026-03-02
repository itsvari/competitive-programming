from string import ascii_lowercase, ascii_uppercase


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        return sum(
            a in chars and b in chars for a, b in zip(ascii_lowercase, ascii_uppercase)
        )
