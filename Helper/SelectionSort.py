# in selection sort the array is sorted from left side
# This algorithm divides the array into two parts: sorted (left) and unsorted (right) subarray.

def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minm = arr[i]
        for j in range(i+1,n):
            minm = min(minm,arr[j])
            temp = arr.index(minm)
        arr[i],arr[temp] = minm,arr[i]
    return arr

if __name__ == '__main__':
    arr = [5,4,2,0,-1]
    print(selectionSort(arr))

