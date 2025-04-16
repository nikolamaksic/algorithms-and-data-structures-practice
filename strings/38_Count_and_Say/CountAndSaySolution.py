class Solution:
    
    def countAndSayCurrentStr(self, s):
        newS = ""
        count = 1
        i = 1
        currDig = s[0]
        while i<len(s):
            if s[i]!=currDig:
                newS+=str(count)+currDig
                currDig = s[i]
                count = 1
            else:
                count += 1
            i+=1
        newS+=str(count)+currDig
        return newS
                

    def countAndSay(self, n: int) -> str:
        currstr = "1"
        for k in range(n-1):
            currstr = self.countAndSayCurrentStr(currstr)
        return currstr

    
        