def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Array pertama: [7, 2, 1, 6, 8, 5, 3, 4]
array1 = [7, 2, 1, 6, 8, 5, 3, 4]

quick_sorted1 = quick_sort(array1.copy())
merge_sorted1 = merge_sort(array1.copy())

print("Array 1 Sebelum Diurutkan:", array1)
print("Quick Sort (Array 1):", quick_sorted1)
print("Merge Sort (Array 1):", merge_sorted1)

# Array kedua: [9, 7, 5, 11, 12, 2, 14, 3]
array2 = [9, 7, 5, 11, 12, 2, 14, 3]

quick_sorted2 = quick_sort(array2.copy())
merge_sorted2 = merge_sort(array2.copy())

print("Array 2 Sebelum Diurutkan:", array2)
print("Quick Sort (Array 2):", quick_sorted2)
print("Merge Sort (Array 2):", merge_sorted2)

# Array ketiga: [3, 8, 2, 7, 6, 4, 5, 1]
array3 = [3, 8, 2, 7, 6, 4, 5, 1]

quick_sorted3 = quick_sort(array3.copy())
merge_sorted3 = merge_sort(array3.copy())

print("Array 3 Sebelum Diurutkan:", array3)
print("Quick Sort (Array 3):", quick_sorted3)
print("Merge Sort (Array 3):", merge_sorted3)
