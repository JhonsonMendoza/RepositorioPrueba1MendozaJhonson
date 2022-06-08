#Creamos la clase principal (Padre), para realizar la herencia.
class registroDocente:
    def __init__(self):
        self.nombre=[]
        self.apellido=[]
        self.edad=[]
        self.rol=[]
        self.departamento=[]
        self.salario=[]

    def datos(self, nombres, apellidos, edades, rols, departamentos, salarios):
        print("SUS NOMBRES SON:",self.nombre)
        nombres in self.nombre
        print("SUS APELLIDOS SON:",self.apellido)
        apellidos in self.apellido
        print("SUS EDADES SON:",self.edad)
        edades in self.edad
        print("SUS ROLES SON:", self.rol)
        rols in self.rol
        print("SUS DEPARTAMENTOS SON:",self.departamento)
        departamentos in self.departamento
        print("SUS SALARIOS SON:",self.salario)
        salarios in self.salario


docente=registroDocente()

#Pedimos datos de la clase principal acerca del docente.
print("-------------------------------------------")
docente.nombre.append(str(input("Registre el nombre del docente: ")))
docente.apellido.append(str(input("apellido del docente: ")))
docente.edad.append(int(input("Ingrese la edad del docente: ")))

#Pedimos datos de la clase hija acerca del docente.
docente.rol.append(str(input("ingrese el rol del docente: ")))
docente.departamento.append(str(input("Ingrese el departamento del docente: ")))
docente.salario.append(float(input("De cuanto es el sueldo del docente ")))

docente.nombre
docente.apellido
docente.edad
docente.rol
docente.departamento
docente.salario

