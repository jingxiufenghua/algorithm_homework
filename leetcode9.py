class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        n = len(string)
        if n == 1 : return True
        for i in range(n):
            if string[i] != string[n-i-1]:
                return False
        return True