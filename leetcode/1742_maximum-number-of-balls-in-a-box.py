class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        max_sum = len(str(highLimit)) * 9 + 1
        count = [0] * max_sum

        s = sum(int(c) for c in str(lowLimit))

        for num in range(lowLimit, highLimit + 1):
            count[s] += 1

            s += 1
            while num % 10 == 9:
                s -= 9
                num //= 10

        return max(count)
