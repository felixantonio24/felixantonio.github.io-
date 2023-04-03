# La aplicacion en la que pedira al usuario los datos de cada estudiante y hara la suma total.
nombre1 = input("Ingrese el nombre del primer estudiante: ")
asignatura1 = input("Ingrese la asignatura del  estudiante: ")
horas1 = int(input("Ingrese las horas lectivas de la asignatura del primer estudiante: "))
monto1 = float(input("Ingrese el monto por hora de la asignatura del primer estudiante: "))
total1 = horas1 * monto1
print("el costo total es:", total1)

nombre2 = input("Ingrese el nombre del  segundo estudiante: ")
asignatura2 = input("Ingrese la asignatura del estudiante: ")
horas2 = int(input("Ingrese las horas lectivas  del estudiante: "))
monto2 = float(input("Ingrese el monto por hora de la asignatura del  estudiante: "))
total2 = horas2 * monto2
print("El costo de la asignaruta es:", total2)

nombre3 = input("Ingrese el nombre del tercer estudiante: ")
asignatura3 = input("Ingrese la asignatura del estudiante: ")
horas3 = int(input("Ingrese las horas lectivas  del estudiante: "))
monto3 = float(input("Ingrese el monto por hora de la asignatura del  estudiante: "))
total3 = horas3 * monto3
print("El costo de la asignaruta es:", total3)

nombre4 = input("Ingrese el nombre del cuarto estudiante: ")
asignatura4 = input("Ingrese la asignatura del  estudiante: ")
horas4 = int(input("Ingrese las horas lectivas del estudiante: "))
monto4 = float(input("Ingrese el monto por hora de la asignatura del estudiante: "))
total4 = horas4 * monto4
print("El costo de la asignaruta es:", total4)

nombre5 = input("Ingrese el nombre del quinto estudiante: ")
asignatura5 = input("Ingrese la asignatura del estudiante: ")
horas5 = int(input("Ingrese las horas lectivas del  estudiante: "))
monto5 = float(input("Ingrese el monto por hora de la asignatura del  estudiante: "))
total5 = horas5 * monto5
print("El costo de la asignaruta es:", total5)

nombre6 = input("Ingrese el nombre del sexto estudiante: ")
asignatura6 = input("Ingrese la asignatura del  estudiante: ")
horas6 = int(input("Ingrese las horas lectivas  del  estudiante: "))
monto6 = float(input("Ingrese el monto por hora de la asignatura del estudiante: "))
total6 = horas6 * monto6
print("El costo de la asignaruta es:", total6)

suma_total = (total1 + total2 +total3 + total4 + total5 + total6)
print("El costo total de todos los estudiantes es :", suma_total)