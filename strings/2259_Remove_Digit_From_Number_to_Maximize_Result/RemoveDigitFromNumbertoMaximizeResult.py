class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        currDig = 0
        currTargInd = None
        while currDig<len(number):
            if number[currDig]==digit:
                currTargInd = currDig
                if currDig==len(number)-1 or number[currDig]<number[currDig+1]:
                    return number[:currTargInd]+number[currTargInd+1:]
            currDig+=1
        if currTargInd is not None and number[currTargInd]==digit:
            return number[:currTargInd]+number[currTargInd+1:]
        else:
            return number