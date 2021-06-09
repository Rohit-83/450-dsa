# Write a function to return minimum and maximum in an array.Your program should make the minimum number of comparisons.
# this can be simply done by using sort fucntion arr.sort() and after that we should return first and last element.

def max_min(arr):
    arr.sort()
    n = len(arr)
    print("max_value =",arr[-1])
    print("min_value =", arr[0])

if __name__ == '__main__':
    arr = [12,4,56,90,14]
    max_min(arr)



