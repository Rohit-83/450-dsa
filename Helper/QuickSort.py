# in Quick sort we have to choose a pivot and around pivot we have to sort
# such a way that in left side the smaller element are present and right side larger element

# pivot is chossen with the help of partition function

def QuickSort(arr,l,r):
    if l<r:
        pi = partition(arr,l,r)
        #pi is the partition index from partiton occur

        QuickSort(arr,l,pi-1)
        QuickSort(arr,pi+1,r)
    return arr


def partition(arr,l,r):
    pivot = arr[r]
    i = l-1
    for j in range(l,r):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return  i+1

if __name__ == '__main__':
    l = 0
    arr = [6,3,9,5,2,8,7]
    r = len(arr)-1
    print(QuickSort(arr,l,r))