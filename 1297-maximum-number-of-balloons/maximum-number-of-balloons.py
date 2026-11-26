class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map={}
        res="balloon"
        count=0
        for char in text:
            hash_map[char]=hash_map.get(char,0)+1
        
        while True:
            for r in res:
                if r in hash_map and hash_map[r]>0:
                    hash_map[r]-=1
                else:
                    return count
            count+=1
       