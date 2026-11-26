class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map={}
        for m in magazine:
            hash_map[m]=hash_map.get(m,0)+1
        
        for r in ransomNote:
            if r not in hash_map or hash_map[r]==0:
                return False
            else:
                hash_map[r]-=1
        return True
       