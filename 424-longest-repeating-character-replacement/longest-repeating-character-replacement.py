class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash={}
        low=0
        maxlen=0
        maxfreq=0

        for h in range(len(s)):
            hash[s[h]]=hash.get(s[h],0)+1
            maxfreq=max(maxfreq,hash[s[h]])
            while((h-low+1)-maxfreq > k):
                hash[s[low]] -=1
                low+=1
                        
            maxlen=max(maxlen,h-low+1)
        return maxlen
        