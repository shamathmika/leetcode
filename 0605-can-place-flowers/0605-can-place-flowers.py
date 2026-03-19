class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = flowerbed

        for i in range(len(f)):
            if n <= 0:
                return True
            
            if f[i] == 0:
                if ((i == 0) or (f[i - 1] == 0)) and ((i == len(f) - 1) or f[i + 1] == 0):
                    f[i] = 1
                    n -= 1
            
        return True if n <= 0 else False

# TC: O(n)
# SC: O(1)