
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        minCardDist = len(cards)+1
        lastCardPosition = {}
        for i, c in enumerate(cards):
            if c in lastCardPosition:
                newDist = i - lastCardPosition[c]+1
                lastCardPosition[c] = i
                if newDist<minCardDist:
                    minCardDist = newDist
            else:
                lastCardPosition[c] = i
        if minCardDist>len(cards):
            return -1
        else:
            return minCardDist
