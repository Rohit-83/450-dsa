# it divides the array into two parts and sort the array

def mergeSort(arr):
    #base case
    if len(arr) == 1: #single element of the array is always sorted
        return arr
    mid = len (arr)//2

    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left,right)


# merge fucntion takes two array and merges it in ascending order
# both the array should be in ascending order
def merge(left,right):
    result = []
    i=0
    j=0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j =j+1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1

    return result

if __name__ == '__main__':
    arr = [4,1,5,0,2]
    print(mergeSort(arr))


