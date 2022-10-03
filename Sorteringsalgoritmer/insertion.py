def insertionsort(a):
    i = 1
    n = len(a)
    for i in range(n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
            
    return a

a = [80, 91, 7, 33, 50, 70, 13, 321, 12]       
insertionsort(a)
print(a)