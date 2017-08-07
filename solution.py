def find_uniq(arr):
    # your code here
    arr.sort()

    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]


    return n   # n: unique integer in the array
