def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    middle = arr[pivot]
    l = [x for x in arr if x < arr[pivot]]
    r = [x for x in arr if x > arr[pivot]]

    return quicksort(l) + [middle] + quicksort(r)

    
def main():
    print(quicksort([1,3,2]))
    print(quicksort([2,3,6,1,5,4,19,59,51,22]))



if __name__ == "__main__":
    main()
