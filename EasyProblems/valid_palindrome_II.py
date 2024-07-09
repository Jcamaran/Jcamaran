class Solution(object):
    def validPalindrome(self, s):
        if s is None:
            return True
        def is_palindrome_range(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1 
                right -= 1
            return True
        
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1] != s[p2]:
                # Check by skipping one character either from the left or the right
                return is_palindrome_range(s, p1+1, p2) or is_palindrome_range(s, p1, p2-1)
            p1 += 1
            p2 -= 1
        return True





        
