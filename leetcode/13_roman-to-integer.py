from itertools import pairwise


class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        total = sum(
            -dictionary[curr]
            if dictionary[curr] < dictionary[nxt]
            else dictionary[curr]
            for curr, nxt in pairwise(s)
        )

        return total + dictionary[s[-1]]
