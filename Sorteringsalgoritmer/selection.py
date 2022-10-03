def selectionsort(a):
    n = len(a)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
                        
        if i != k:
            a[i], a[k] = a[k], a[i]
            
a = [80, 91, 7, 33, 50, 70, 13, 321, 12]       
selectionsort(a)
print(a)