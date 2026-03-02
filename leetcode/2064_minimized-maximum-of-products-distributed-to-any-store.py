from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        def numberOfStores(m: int) -> int:
            return sum((q - 1) // m + 1 for q in quantities)

        while left < right:
            mid = (left + right) // 2
            if numberOfStores(mid) <= n:
                right = mid
            else:
                left = mid + 1

        return left
