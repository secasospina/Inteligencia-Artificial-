class Enfermedad:
    def __init__(self, nombre, sintomas):
        self.Nombre = nombre
        self.Sintomas = sintomas
        self.CantidadSintomas = len(self.Sintomas)

class Tratamiento:
    def __init__(self, nombre, enfermedad):
        self.Nombre = nombre
        self.Enfermedad = enfermedad

class Analgesico(Tratamiento):
    def recetar(self):
        print("Usted tiene ",self.Enfermedad," requiere un Analgesico, puede tomar: ", self.Nombre)

class AntiInflamatorio(Tratamiento):
    def recetar(self):
        print("Usted tiene ",self.Enfermedad," requiere un antiInflamatorio, puede tomar: ", self.Nombre)

def agregarEnfermedades(nombre,sintomas):
    listaEnfermedades.append(Enfermedad(nombre,sintomas))

def agregarTratamiento(nombre,enfermedad,tipo):
    if tipo == "Analgesico":
        listaTratamientos.append(Analgesico(nombre,enfermedad))
    else:
        listaTratamientos.append(AntiInflamatorio(nombre,enfermedad))

def sintomasUsuario():
    condicional = True
    while condicional == True:
        sintoma = str(input("¿Que Sintoma tiene?: "))
        listaSintomas.append(sintoma)
        condicional = bool(input("Si ya no desea ingresar sintomas presione enter de lo contrario ingrese lo que sea: "))

def comparar_sintomas_enfermedades():
    contador_sintomas_gripe = 0
    contador_sintomas_faringitis = 0
    for s in listaSintomas:
        for e in listaEnfermedades:
            for se in e.Sintomas:
                if s == se:
                    if e.Nombre == "Gripe":
                        contador_sintomas_gripe += 1
                    else:
                        contador_sintomas_faringitis += 1

    print("Debido a sus sintomas, el sistema determina que: ")
    if contador_sintomas_faringitis < contador_sintomas_gripe:
        for t in listaTratamientos:
            if t.Enfermedad == "Gripe":
                print(t.recetar())
    elif contador_sintomas_faringitis > contador_sintomas_gripe:
        for t in listaTratamientos:
            if t.Enfermedad == "Faringitis":
                print(t.recetar())
    else:
        print("No se puede recetar, se necesita más informacion")


def menu():
    agregarEnfermedades("Gripe",['Fiebre','Malestar','Tos'])
    agregarEnfermedades("Faringitis",['DolorGarganta','Malestar'])
    agregarTratamiento("Acetaminofen","Gripe","Analgesico")
    agregarTratamiento("Diclofenaco","Faringitis","AntiInflamatorio")
    sintomasUsuario()
    print("Sus sintomas son: ",listaSintomas)
    comparar_sintomas_enfermedades()

if __name__ == "__main__":
    listaEnfermedades = []
    listaTratamientos = []
    listaSintomas = []
    menu()
