#Lenke til kattis oppgave: https://open.kattis.com/problems/babybites

n = int(input())
sentence = input().split()

fishy = True

for i in range(n):
    if sentence[i] != str(i+1) and sentence[i] != "mumble":
        fishy = False
        break
        
if (fishy):
    print("makes sense")
else:
    print("something is fishy")