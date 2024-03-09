class Solution:
    def isValid(self, s: str) -> bool:
    
        arr = []

        print("check s", type(s))
        print("check a list of enumerate(s)", list(enumerate(s)))

        for i in enumerate(s):

            print("check i", i[1])
            if i[0] == 0:
                arr.append(i[1])

            print("check first index here",arr[0]) 

        print("check arr", arr)