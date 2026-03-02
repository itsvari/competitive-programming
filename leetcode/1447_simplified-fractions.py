from math import gcd
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [
            f"{numerator}/{denominator}"
            for numerator in range(1, n)
            for denominator in range(numerator + 1, n + 1)
            if gcd(numerator, denominator) == 1
        ]
