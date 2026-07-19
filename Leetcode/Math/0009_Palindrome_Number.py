class Solution(object):
    
    def isPalindrome(self, x):
                    
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        r = 0

        while x > r:
            digit = x%10
            x = x // 10
            r = r * 10 + digit

        return x == r or x == r // 10

x = Solution()
print(x.isPalindrome(12321))