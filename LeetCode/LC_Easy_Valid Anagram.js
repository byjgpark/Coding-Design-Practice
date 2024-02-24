 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t))
            return False

        # print("check " , len(s))
        # print("check here " , len(t))
        # print("check range", range(len(t)))

        # print("chjeck s", s)

        # for i in range(len(s)):
        #     print("check s", s[i])

        countS, countT = {}, {}

        for i in range(len(s)):

            print("countS :", countS, "countT :", countT)

            # print(f"1st print -> i : {i} | s[i] : {s[i]} | count : ", countS.get(s[i], 0), "countS :",countS)

            print(f"1st print -> i : {i} | s[i] : {s[i]} | count : ", countS.get(s[i], 0), "countS : ",countS)
            print(f"2nd print -> i : {i} | t[i] : {t[i]} | count : ", countT.get(t[i], 0), "countT : ",countT)

            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        
        countA = {'a': 3, 'n': 2, 'g': 1, 'r': 1, 'm': 1}
        countB = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}

        return countS == countT


        print("check countS", countS)
        print("check countT", countT)

        print("compare between twos = ", countA == countB)

        