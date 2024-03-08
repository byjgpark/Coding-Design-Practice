class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s)

        while( L < R):

            # print("check",s[L])
            # L+=1

            if( not s[L].isalnum()):
                print("s[L]", s[L])
