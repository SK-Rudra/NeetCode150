class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) < 2:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            # Odd length palindrome
            odd = expand(i, i)

            # Even length palindrome
            even = expand(i, i + 1)

            length = max(odd, even)

            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2

        return s[start:start + max_len]