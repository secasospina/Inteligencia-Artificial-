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
    def recetar(self,d):
        print("Usted es compatible en un ", d*100,"% ","con ",self.Enfermedad," requiere un Analgesico, puede tomar: ", self.Nombre)

class AntiInflamatorio(Tratamiento):
    def recetar(self,d):
        print("Usted es compatible en un ", d*100,"% ","con ",self.Enfermedad," requiere un antiInflamatorio, puede tomar: ", self.Nombre)

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
    relacion_sintomas_gripe = 0
    relacion_sintomas_faringitis = 0
    for s in listaSintomas:
        for e in listaEnfermedades:
            for se in e.Sintomas:
                if s == se[0]:
                    if e.Nombre == "Gripe":
                        relacion_sintomas_gripe += (1-relacion_sintomas_gripe)*se[1]
                    else:
                        relacion_sintomas_faringitis += (1-relacion_sintomas_faringitis)*se[1]

    print("Debido a sus sintomas, el sistema determina que: ")
    if relacion_sintomas_faringitis < relacion_sintomas_gripe:
        for t in listaTratamientos:
            if t.Enfermedad == "Gripe":
                print(t.recetar(relacion_sintomas_gripe))
    else:
        for t in listaTratamientos:
            if t.Enfermedad == "Faringitis":
                print(t.recetar(relacion_sintomas_faringitis))


def menu():
    agregarEnfermedades("Gripe",[['Fiebre',0.2],['Malestar',0.9],['Tos',0.7]])
    agregarEnfermedades("Faringitis",[['DolorGarganta',0.8],['Malestar',0.6]])
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
