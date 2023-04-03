#ejercicio número 2 
class Estudiantes:
    
    def __init__(self, carrera, edad, creditos, semestre, nacionalidad):
        self.carrera = carrera
        self.edad = edad
        self.creditos = creditos
        self.semestre = semestre
        self.nacionalidad = nacionalidad
        
    def metodo(self):
        output = ("Estoy estudiando la carrera de  {}, tengo {} años, por ahora tengo {} créditos , estoy cursando el {} semestre, por otro lado mencionar que soy {}.")
        print(output.format(self.carrera, self.edad, self.creditos, self.semestre, self.nacionalidad))

    def ingresar_nombre():
        print("Felix Antonio")
        
    ingresar_nombre()
    
    def ingresar_apellido():
        print("Pinedo Tello")
        
    ingresar_apellido()
    
    def ingresar_estado_civil():
        print("Soltero")
        
    ingresar_estado_civil()
    
    def ingresar_nombre_de_asignaturas():
        print("Redacción, Programación.")
        
    ingresar_nombre_de_asignaturas()
    
    def ingresar_numero_horas_estudio():
        print("15 horas a la semana academicamente")
        
    ingresar_numero_horas_estudio()
        
x = Estudiantes("Ingeniería de Minas", "25", "4", "segundo", "peruano")
x.metodo()  
