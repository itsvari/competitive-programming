class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(number: int) -> bool:
            if number < 2:
                return False
            if number in (2, 3):
                return True
            if number % 2 == 0 or number % 3 == 0:
                return False

            # fast primality test: all primes > 3 take the form of 6k ± 1.
            # we check divisors up to the square root of the number.
            divisor = 5
            while divisor * divisor <= number:
                if number % divisor == 0 or number % (divisor + 2) == 0:
                    return False
                divisor += 6
            return True

        # base case: 11 is the ONLY even-length prime palindrome.
        if n <= 11:
            for prime in [2, 3, 5, 7, 11]:
                if prime >= n:
                    return prime

        n_str = str(n)
        digit_length = len(n_str)

        if digit_length % 2 == 0:
            # skip even lengths completely
            starting_root = 10 ** (digit_length // 2)
        else:
            # if odd length, slice the exact first half of 'n' (including the middle digit)
            # Example: n = 135 (length 3) -> slice first 2 digits -> root is 13
            half_length = (digit_length + 1) // 2
            starting_root = int(n_str[:half_length])

        current_root = starting_root

        while True:
            # construct the palindrome
            # example: current_root = "123" -> right_half = "21" -> palindrome = 12321
            left_half = str(current_root)
            right_half = left_half[:-1][::-1]
            palindrome = int(left_half + right_half)

            if palindrome >= n and is_prime(palindrome):
                return palindrome

            current_root += 1
