class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        print("Check piles =", piles)

## 2nd trial
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                return speed
            speed += 1
        return speed


## 3rd trial
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = 1
        while True:
            res = 0    
            print("check k =",k)
            for pile in piles:
                # print("check pile =", pile)
                # print(" ceil =" ,math.ceil(pile/k))
                res += math.ceil(pile/k)
                print("Check res =", res)
            # print("Check res =", res)

            k+=1
            if res<=h:
                return res
            

        return res
            
