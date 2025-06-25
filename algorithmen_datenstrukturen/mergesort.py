def merge(l, r):
    ans = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            ans.append(l[i])
            i += 1
        else:
            ans.append(r[j])
            j +=1
    ans = ans + l[i:] + r[j:]

    return ans

def merge_sort(shuffled_list):
    if len(shuffled_list) <= 1:
        return shuffled_list

    i = len(shuffled_list) // 2
    l = merge_sort(shuffled_list[i:])
    r = merge_sort(shuffled_list[:i])

    return merge(l, r)


def main():
    print(merge_sort([1,2,3,6,5,7,4,9]))
    print(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(merge_sort([1, 3, 2, 4, 6, 5, 7, 9, 8]))
    print(merge_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(merge_sort([5, 4, 3, 2, 1]))
    print(merge_sort([1, 2, 3, 4, 5]))
    print(merge_sort([2, 1, 3, 5, 4]))

if __name__ == "__main__":
    main()
