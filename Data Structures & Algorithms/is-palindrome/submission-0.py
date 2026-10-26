class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non alphanumeric chars
        c = ''.join(filter(str.isalnum, s)).lower()
        return c == c[::-1]