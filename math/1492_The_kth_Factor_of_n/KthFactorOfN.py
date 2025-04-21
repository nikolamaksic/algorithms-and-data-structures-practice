import math

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorsL = []
        factorsR = []
        for i in range(1, int(math.sqrt(n)+1)):
            if n % i ==0:
                factorsL.append(i)
                if i!=int(n//i):
                    factorsR.append(n//i)
        k-=1
        if k>=len(factorsL)+len(factorsR):
            return -1
        if k<len(factorsL):
            return factorsL[k]
        k-=len(factorsL)-1
        return factorsR[-k]