class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerCount = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                # Left side is empty if it is the leftmost flower, or if the left side is actually empty
                leftEmpty = (i == 0) or (flowerbed[i - 1] == 0)

                # Same logic as above for right side
                rightEmpty = (i == length - 1) or (flowerbed[i + 1] == 0)

                # If both sides are empty, we can place
                if leftEmpty and rightEmpty:
                    # Place the flower
                    flowerCount += 1
                    flowerbed[i] = 1
                    
                    if flowerCount >= n:
                        return True

        return flowerCount >= n