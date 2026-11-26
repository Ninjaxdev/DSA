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
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         hash_map = {}
#         for char in text:
#             hash_map[char] = hash_map.get(char, 0) + 1
#        # we need max of 2 os and 2 ls to form balloon 1 time thats why we use integer division //     
#         return min(
#             hash_map.get('b', 0),
#             hash_map.get('a', 0),
#             hash_map.get('l', 0) // 2,
#             hash_map.get('o', 0) // 2,
#             hash_map.get('n', 0)
#         )

