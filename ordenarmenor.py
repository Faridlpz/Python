numeros=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)-1,-1,-1):
    if i == 0:
        print(f"{numeros[i]}.",end="")
    else:
        print(f"{numeros[i]}, ",end="")

input()
