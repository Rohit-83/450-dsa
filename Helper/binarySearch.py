# we have two types of searching linear and binary
# time complexity of linear is O(n)
# time complexity of binary is O(logn)
# in binary search always the array should present in sorted form

def binarySearch(arr,value):
    n = len(arr)
    start = 0
    end = n-1
    count = 0
    mid = (start+end)//2
    while start <= end:
        count+=1
        mid = (start+end)//2
        if arr[mid] == value:
            return mid,count
        elif arr[mid] > value:
            end = mid-1
        elif arr[mid] < value:
            start = mid+1

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    value = 4
    print(binarySearch(arr,value))

