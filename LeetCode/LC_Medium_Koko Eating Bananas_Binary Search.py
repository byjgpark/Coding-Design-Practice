class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res

    
## 2nd trial
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        print("check l =",l," r =", r)

        res=r
    
        while l<=r:

            k=(l+r)//2

            print("check k =", k)
            
            remaining = 0
            for pile in piles:
                remaining+=math.ceil(pile/k)
                # print("Check pile =", pile)
                # print("Check ceil =", math.ceil(1.2))
                print("Check remaining =", remaining)




        