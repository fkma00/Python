def quicksort(a, low, high):
    if low >= high:
        return a
    p = partition(a, low, high)
    quicksort(a, low, p-1)
    quicksort(a, p+1, high)
    return a
    
def partition(a, low, high):
    p = choosePivot(a, low, high)
    a[p], a[high] = a[high], a[p]
    
    pivot = a[high]
    left = low
    right = high-1
    
    while left <= right:
        while left <= right and a[left] <= pivot:
            left += 1

        while right >= left and a[right] >= pivot:
            right -= 1
            
        if left < right:
            a[left], a[right] = a[right], a[left]
            
    a[left], a[high] = a[high], a[left]
            
    return left

def choosePivot(a, low, high):
    return (low + high) // 2
