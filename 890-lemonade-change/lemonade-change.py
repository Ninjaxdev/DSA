class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        ans=False
        five=0
        ten=0
        balance=0
        if bills[0]==5:
            five+=1
            balance+=bills[0]
        else:
            return ans

        for i in range(1,len(bills)):
            if bills[i]==5:
                five+=1
                balance+=bills[i]
            elif bills[i]==10:
                if five==0:
                    return ans
                ten+=1
                five+=-1
                balance+=bills[i]-5
                
            else:
                if ten>0:
                    ten-=1
                    if five==0:
                        return ans
                    five-=1
                    balance+=bills[i]-15
                else:
                    if five<3:
                        return ans
                    five-=3
                    balance+=bills[i]-15
        return True

            
            
        