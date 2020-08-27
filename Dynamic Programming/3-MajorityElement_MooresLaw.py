def majority_ele(arr):
    size = len(arr)
    count = 1 
    curr_majority = arr[0]
    
    for i in range(1, size):
        if curr_majority == arr[i]:
            count = count + 1
        else:
            count = count - 1
            
        if count == 0:
            curr_majority = arr[i]
            count = 1 
            
    for i in range(size):
        if curr_majority == arr[i]:
            count=count+1
        if count>size/2:
            return curr_majority
            
arr = [2,1,2,3,2,1,1,1]

print(majority_ele(arr))
    