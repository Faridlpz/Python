materias=[]
indice=0
while True:
    materias.append("")
    materias[indice]=input("Ingrese una materia de su horario: ")
    if materias[indice] == "salir":
        materias.pop(indice)
        break
    else:
        indice+=1
print("Sus materias son: ",end="")
for i in range(len(materias)):
    print(f'{materias[i]}, ',end="")