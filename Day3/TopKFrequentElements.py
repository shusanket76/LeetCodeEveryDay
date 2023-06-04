# link="https://leetcode.com/problems/top-k-frequent-elements/description/"


def topKFrequent(nums, k):
    hasmap={}
    res=[]
    for x in nums:
        hasmap[x] = hasmap.get(x,0)+1
    
    count = [[] for x in range(len(nums)+1)]
    for a,b in hasmap.items():
        count[b].append(a)
    for dl in range(len(count)-1,-1,-1):
        if count[dl]:
            
                for ite in count[dl]:
                    if len(res)<k:
                        res.append(ite)
    return res
    