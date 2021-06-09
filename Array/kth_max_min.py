# Given an array and a number k where k is smaller than the size of the array,
# we need to find the k’th smallest element in the given array.
# It is given that all array elements are distinct.

def kthSmallest(arr,k):
    arr.sort()
    return arr[k-1]
def kthLargest(arr,k):
    arr.sort()
    return arr[-k]

if __name__ == '__main__':
    arr = [1,4,2,7,9]
    k=2
    print(kthSmallest(arr,k))
    print(kthLargest(arr,k))