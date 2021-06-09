# Given an array (or string), the task is to reverse the array/string
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

def reverse(arr):
    new_arr =[]
    n = len(arr)
    for i in range(n-1,-1,-1):
        new_arr.append(arr[i])
    return new_arr

if __name__ == '__main__':
    arr = [1,2,4]
    print(reverse(arr)) #first method
    print(arr[::-1]) #second method short trick

