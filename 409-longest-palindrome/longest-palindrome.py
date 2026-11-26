class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map={}
        odd=False
        res=0
        for char in s:
            hash_map[char]=hash_map.get(char,0)+1
        
        for v in hash_map.values():
            if v%2==0:
                res+=v
            else:
                odd=True
                res+=v-1
            
        if odd:
            return res+1
        else:
            return res
    


        