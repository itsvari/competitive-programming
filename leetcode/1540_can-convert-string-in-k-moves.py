class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        shiftCount = [0] * 26

        for char_s, char_t in zip(s.lower(), t.lower()):
            shiftDist = (ord(char_t) - ord(char_s) + 26) % 26
            shiftCount[shiftDist] += 1

        for shift in range(1, 26):
            maxMovesPerShift = shift + 26 * (shiftCount[shift] - 1)

            if maxMovesPerShift > k:
                return False

        return True
