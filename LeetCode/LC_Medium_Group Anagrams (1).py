class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for str in strs:    

            arr = [0] * 26    

            # print("check arr here ", arr)        

            for s in str:

                # print("check s :",s,"ord(s) :", ord(s))
                diffOrd = ord(s) - ord('a')
                # print("check diffOrd :", diffOrd)
                arr[diffOrd] +=1
            
            tupleArr = tuple(arr)
            if tupleArr not in map:
                map[tupleArr] = []
            
            map[tupleArr].append(str)   

            # print("check str ", str, "arr :", arr)  
            # print("check map object :", map)      
            # print("check map", list(map.values()))      
        
        return list(map.values())   

