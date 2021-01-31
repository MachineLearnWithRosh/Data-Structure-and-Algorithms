def min_max(L):
    l=len(L)
    if l==1:
        if isinstance(L[0],list):
            return min_max(L[0])
        else:
            return [L[0],L[0]]
    else:
        mid=l//2
        l1 = min_max(L[:mid])
        l2 = min_max(L[mid:])
        if l1[0]>l2[0]:
            l1[0]=l2[0]
        if l1[1]<l2[1]:
            l1[1]=l2[1]
        return l1
        
arr = [1,2,3]
res = min_max(arr)
print(res)