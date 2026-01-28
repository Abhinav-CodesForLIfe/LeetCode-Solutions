class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        rev = "".join(reversed(s))

        if s == rev:
            return True
        else:
            return False
