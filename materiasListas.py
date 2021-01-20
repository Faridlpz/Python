materias=["Español","Matematicas","Fisica","Quimica","Hstoria"]
calificaciones=[]
for i in range(len(materias)):
    calificaciones.append(1)
    calificaciones[i]=input(f"Ingresa tu calificacion de {materias[i]}: ")
for i in range(len(calificaciones)):
    print(f"En {materias[i]} has sacado: {calificaciones[i]}")
