def max_sum_subarray(arr):
    c_sum = 0
    curr_maxValue = arr[0]
    st, end, poi = 0, 0 ,0
    
    for i in range(0, len(arr)):
        
        c_sum = c_sum + arr[i]
        
        if c_sum > curr_maxValue:
            curr_maxValue = c_sum
            st = poi
            end = i
        
        if c_sum<0:
            c_sum = 0
            poi = i+1
        
    print("Maximum sum Subarray is",curr_maxValue)
    print("Start Index of window is",st)
    print("End Index of window is",end)

array = [4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]

max_sum_subarray(array)