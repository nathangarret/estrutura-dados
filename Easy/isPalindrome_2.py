class Solution:
    def isPalindrome(self, x: int) -> bool:
        check = str(x)
        left, right = 0, len(check)-1
        while left < right:
            if check[left] != check[right]:
                return False
            left += 1
            right -= 1
        return True