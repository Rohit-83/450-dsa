# in the array we form two parts in one part the sorted array is placed
# if the array has one element then it is sorted

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    arr = [9,8,1,3,5,10]
    print(insertionSort(arr))
