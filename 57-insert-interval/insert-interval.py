class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        insert=False
        new=[]
        res=[]

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0] and not insert :
                new.append(newInterval)
                insert=True
            new.append(intervals[i])
        if not insert:
            new.append(newInterval)

        start1=new[0][0]
        end1=new[0][1]
        for i in range(1,len(new)):
            start2=new[i][0]
            end2=new[i][1]
            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
            else:
                res.append([start1,end1])
                start1=start2
                end1=end2
        res.append([start1,end1])
        return res
        