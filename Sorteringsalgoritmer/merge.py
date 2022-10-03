def mergesort(a):
    n = len(a)
    if n <= 1:
        return a
    i = n//2
    a1 = mergesort(a[0:i])
    a2 = mergesort(a[i:n])
    return merge(a1, a2, a)

def merge(a1, a2, a):
    i = 0
    j = 0
    
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            a[i+j] = a1[i]
            i += 1
        else:
            a[i+j] = a2[j]
            j += 1
            
    while i < len(a1):
        a[i+j] = a1[i]
        i += 1
            
    while j < len(a2):
        a[i+j] = a2[j]
        j += 1
        
    return a
