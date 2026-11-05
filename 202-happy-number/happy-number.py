class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=self.calsquare(n)
        while(fast!=1 and slow!=fast):
            slow=self.calsquare(slow)
            fast=self.calsquare(self.calsquare(fast))
            
        return fast==1

    #    num=n
    #    sum=0
    #    while(num>0):
    #        digit=num%10
    #        sum=sum+digit**2
    #        num=num//10
    #        if num==0:
    #            num=sum
    #            if sum==1:
    #                return True
    #            sum=0


    def calsquare(self,n):
        num=n
        sum=0
        while(num>0):
            digit=num%10
            sum=sum+digit**2
            num=num//10
        return sum