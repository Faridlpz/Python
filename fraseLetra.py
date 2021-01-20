frase=input("Ingrese una frase: ")
letra=input("Ingrese una letra: ")
contador=0
for i in frase:
    if(i==letra):
        contador=contador+1
print(f"La letra aparece {contador} veces")
input()