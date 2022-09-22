from set import Set

def hovedprogram():
    set = Set()
    
    n = int(input())
    if (n >= 1 and n <= 1000000):
        print("True")
    else:
        print("False")
    
    for i in range(n):
        inp = input()
        linje = inp.split() 
        command = linje[0]
        if (command == "insert"):
            set.insert(int(linje[1]))
        elif (command == "remove"):
            set.remove(int(linje[1]))   
        elif command == "contains":
            set.contains(int(linje[1]))   
        else: 
            set.size()
                    
hovedprogram()