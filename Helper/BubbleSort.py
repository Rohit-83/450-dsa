def bubbleSort(arr):
    n = len(arr)
    flag = False
    count = 0
    for i in range(n-1):
        for j in range(n-1-i):
            count+=1
            if arr[j]>arr[j+1]:
                flag = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if flag == False:
            break
    return arr,count

if __name__ == '__main__':
    arr = [1,2,9,4,5]
    print(bubbleSort(arr))

