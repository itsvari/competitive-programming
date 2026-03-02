class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 < cost2:
            cost1, cost2 = cost2, cost1

        count = 0

        for i in range((total // cost1) + 1):
            remaining = total - (i * cost1)
            count += (remaining // cost2) + 1

        return count
