#Lenke til kattis oppgave: https://open.kattis.com/contests/yrtze2/problems/trainpassengers

ints = input().split()

capacity = int(ints[0])
n = int(ints[1])

on_train = 0

ret = "possible"

for i in range(n):
    nums = input().split()
    off = int(nums[0])
    on = int(nums[1])
    stay = int(nums[2])
    
    if on_train < off:
        ret = "impossible"
    
    on_train += on
    on_train -= off
    
    
    if on_train > capacity:
        ret = "impossible"
    if on_train < capacity and stay > 0:
        ret = "impossible"
    if on_train < 0:
        ret = "impossible"
        
if on_train != 0:
    ret = "impossible"
print(ret)
