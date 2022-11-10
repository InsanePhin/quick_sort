def quick_sort(array):
    if len(array) < 2:
        return array

    p = array[len(array) // 2]

    l = [a for a in array if a < p]
    m = [a for a in array if a == p]
    r = [a for a in array if a > p]

    return quick_sort(l) + m + quick_sort(r)

arr = [3, 6, 8, 10, 1, 2, 5, 7, 14, 16, 9]

print(f"before {arr}")
print(f"after {quick_sort(arr)}")