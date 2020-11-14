def partition(arr, low, high):
    pivot = arr[high]
    j = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j + 1], arr[high] = arr[high], arr[j + 1]
    return j+1

def quick_sort(arr, low, high):
    if low < high:
        pivotal = partition(arr, low, high)
        quick_sort(arr, low, pivotal - 1)
        quick_sort(arr, pivotal + 1, high)

array = [11, 23, 98, 74, 10, 98, 54, 48, 63, 14]
quick_sort(array, 0, len(array)-1)
print(array)

