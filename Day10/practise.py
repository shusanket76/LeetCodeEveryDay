a = [1,2,3,4,5,6,7,8,9,10]

find = 11

def fin(a,find):
    l,r=0,len(a)-1
    while l<=r:
        mid = int((l+r)/2)
        if a[mid]==find:
            return("FOUND AT ", mid)
            
        else:
            if a[mid]>find:
                r=mid-1
            else:
                l=mid+1
    return("NOT FOUND", -1)

c = fin(a,find)
print(c)