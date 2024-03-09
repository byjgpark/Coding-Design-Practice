class Solution:
    def isPalindrome(self, s: str) -> bool:

        L = 0
        R = len(s) - 1

        while L < R:
            print("check L :", L, "check R :",R)
            print("check s[L].lower() :",s[L].lower(), "s[R].lower()", s[R].lower())

            if not s[L].isalnum():
                L+= 1
                continue

            if not s[R].isalnum():
                R-= 1
                continue

      
            if s[L].lower() != s[R].lower():
                return False

            L+=1
            R-=1
        
        return True