import pymysql as sql
from abc import ABC, abstractmethod

class ICrud(ABC):
    @abstractmethod
    def get_by_id(self, **kwargs):
        raise NotImplementedError

class Animal(ICrud):
    host = "",
    user = "",
    passwd = "",
    database = ""
    bd = ""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = ""
        self.database = "bd_prediccion"
        self.bd = sql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )

    def get_all(self):
        cursor = self.bd.cursor()
        sql = "SELECT * FROM animales"
        cursor.execute(sql)
        r = cursor.fetchall()
        for animales in r:
            Animal_Information.append(animales)
        print("")
        return len(r)

    def get_by_id(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Nombre_animal FROM animales where (Id_animal) = (%s)"
        cursor.execute(sql, (kwargs['Id_animal']))
        r = cursor.fetchall()
        #print("De casualidad estás pensando en un: ")
        for animales in r:
            #print(animales)
            return animales
        print("")

    def get_id_by_type(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Id_animal, Nombre_animal, Nombre_tipo_animal FROM animales, tipo_animal where animales.Id_tipo_animal = tipo_animal.Id_tipo_animal and Nombre_tipo_animal = (%s)"
        cursor.execute(sql, (kwargs['Nombre_tipo_animal']))
        r = cursor.fetchall()
        print("Posibles respuestas")
        for animales in r:
            print(animales)
        print("")
        return r
    
    def get_id_by_name(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Id_animal FROM animales where Nombre_animal = (%s)"
        cursor.execute(sql, (kwargs['Nombre_animal']))
        r = cursor.fetchall()
        for nombre in r:
            #print(nombre)
            return nombre
        print("")
        #return r

    def compare_animal_caracteristics(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT animales.Id_animal, Nombre_animal, Nombre_caracteristica FROM animales, caracteristicas, caracteristicas_animales where caracteristicas_animales.Id_animal = (%s) and Nombre_caracteristica = (%s) and caracteristicas_animales.Id_animal = animales.Id_animal and caracteristicas.Id_caracteristica=caracteristicas_animales.Id_caracteristica"
        cursor.execute(sql, (kwargs['Id_animal'], kwargs['Nombre_caracteristica']))
        r = cursor.fetchall()
        for animales in r:
            animales_coinciden.append(animales)

    def add_animal(self, **kwargs):
        sql = "insert into animales(Id_animal,Nombre_animal,Id_tipo_animal) values (%s,%s,%s)"
        datos = (kwargs['Id_animal'], kwargs['Nombre_animal'], kwargs['Id_tipo_animal'])
        cursor = self.bd.cursor()
        cursor.execute(sql, datos)
        self.bd.commit()
        print("Animal agregado")

class Caracteristicas(ICrud):
    host = "",
    user = "",
    passwd = "",
    database = ""
    bd = ""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = ""
        self.database = "bd_prediccion"
        self.bd = sql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
    
    def get_by_id(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Nombre_animal FROM animales where (Id_animal) = (%s)"
        cursor.execute(sql, (kwargs['Id_animal']))
        r = cursor.fetchall()
        print("De casualidad estás pensando en un: ")
        for animales in r:
            #print(animales)
            return animales
        print("")

    def get_all(self):
        cursor = self.bd.cursor()
        sql = "SELECT * FROM caracteristicas"
        cursor.execute(sql)
        r = cursor.fetchall()
        for caracteristicas in r:
            Caracteristicas_Information.append(caracteristicas)
        print("")
        return len(r)

    def get_id_by_caracteristic(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Id_caracteristica FROM caracteristicas where Nombre_caracteristica = (%s)"
        cursor.execute(sql, (kwargs['Nombre_caracteristica']))
        r = cursor.fetchall()
        for caracteristica in r:
            #print(caracteristica)
            return caracteristica
        print("")
        #return r

    def add_caracteristics(self, **kwargs):
        sql = "insert into caracteristicas values (%s,%s)"
        datos = (kwargs['Id_caracteristica'], kwargs['Nombre_caracteristica'])
        cursor = self.bd.cursor()
        cursor.execute(sql, datos)
        self.bd.commit()
        print("Caracteristica agregada")

class Tipo_animal(ICrud):
    host = "",
    user = "",
    passwd = "",
    database = ""
    bd = ""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = ""
        self.database = "bd_prediccion"
        self.bd = sql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )

    def get_by_id(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Nombre_animal FROM animales where (Id_animal) = (%s)"
        cursor.execute(sql, (kwargs['Id_animal']))
        r = cursor.fetchall()
        print("De casualidad estás pensando en un: ")
        for animales in r:
            print(animales)
            return animales
        print("")

    def get_id_by_type(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Id_tipo_animal FROM tipo_animal where (Nombre_tipo_animal) = (%s)"
        cursor.execute(sql, (kwargs['Nombre_tipo_animal']))
        r = cursor.fetchall()
        for i in r:
            #print(i[0])
            return i[0]
        print("")

    def get_all(self):
        cursor = self.bd.cursor()
        sql = "SELECT * FROM tipo_animal"
        cursor.execute(sql)
        r = cursor.fetchall()
        for tipo in r:
            Tipo_Information.append(tipo)
        print("")
        return len(r)

    def add_type(self, **kwargs):
        sql = "insert into tipo_animal values (%s,%s)"
        datos = (kwargs['Id_tipo_animal'], kwargs['Nombre_tipo_animal'])
        cursor = self.bd.cursor()
        cursor.execute(sql, datos)
        self.bd.commit()
        print("Tipo agregado")

class Caracteristicas_animal(ICrud):
    host = "",
    user = "",
    passwd = "",
    database = ""
    bd = ""

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.passwd = ""
        self.database = "bd_prediccion"
        self.bd = sql.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )

    def get_by_id(self, **kwargs):
        cursor = self.bd.cursor()
        sql = "SELECT Nombre_animal FROM animales where (Id_animal) = (%s)"
        cursor.execute(sql, (kwargs['Id_animal']))
        r = cursor.fetchall()
        print("De casualidad estás pensando en un: ")
        for animales in r:
            print(animales)
            return animales
        print("")

    def get_all(self):
        cursor = self.bd.cursor()
        sql = "SELECT * FROM caracteristicas_animales"
        cursor.execute(sql)
        r = cursor.fetchall()
        for caracteristicas in r:
            Relacion_Information.append(caracteristicas)
        print("")
        return len(r)

    def add_relation(self, **kwargs):
        sql = "insert into caracteristicas_animales values (%s,%s,%s)"
        datos = (kwargs['Id_caracteristica_animal'], kwargs['Id_animal'], kwargs['Id_caracteristica'])
        cursor = self.bd.cursor()
        cursor.execute(sql, datos)
        self.bd.commit()
        print("Relacion agregada")

def Consultar_animal():
    Animal = str(input("No se me ocurre ningun animal, ¿podrias decirme en cual piensas?: "))
    return Animal

def Consultar_tipo():
    Tipo=str(input("¿En que tipo de animal piensas?: "))
    return Tipo

def Consultar_caracteristicas():
    print("Dame alguna pista")
    condicional = True
    while condicional == True:
        Caracteristicas = str(input("Dime una caracteristica: "))
        Lista_Caracteristicas.append(Caracteristicas)
        condicional = bool(input("Si ya no desea ingresar caracteristicas presione enter de lo contrario ingrese lo que sea: "))

def Comparar():
    Consultar_caracteristicas()
    Respuesta = []
    #for a in Posibles_Animales:
    #    print(a)
    
    for a in Posibles_Animales:
        for c in Lista_Caracteristicas:
            animal.compare_animal_caracteristics(Id_animal=a[0],Nombre_caracteristica=c)
    
    list(animales_coinciden)
    i=0
    for p in Posibles_Animales:
        for a in animales_coinciden:
            if a[0] == p[0]:
                i+=1
        animales.append([p[0],i])
        i=0
    if animales == []:
        max_values=0
    else:
        idx,max_values=max(animales, key=lambda item: item[1])
    list(animales)

    if max_values > 0:
        for a in animales:
            if a[1] == max_values:
                Respuesta.append(animal.get_by_id(Id_animal=a[0]))
    list(Respuesta)
    if len(Respuesta) > 1:
        print("Aun no estoy seguro de lo que piensas ")
        Comparar()
    elif len(Respuesta) == 1:
        print(" ")
        print("Estas pensando en un ",Respuesta[0][0])
        opcion = int(input("Si es correcto ingrese 1, de lo contrario ingrese 0. "))
        if opcion == 0:
            animal_usuario.append(Consultar_animal())
            print("Podrias decirme en que se diferencian?. ")
            Consultar_caracteristicas()
            Agregar_en_tablas()
        else:
            animal_usuario.append(Respuesta[0][0])
            Agregar_en_tablas()
    elif len(Respuesta) == 0:
        animal_usuario.append(Consultar_animal())
        Agregar_en_tablas()

def Tamaño_tablas():
    LLaves.append(tipos.get_all())
    LLaves.append(animal.get_all())
    LLaves.append(caracteristicas.get_all())
    LLaves.append(caracteristicas_animal.get_all())
    #Ver_info_tablas()
    

def Ver_info_tablas():
    for a in Animal_Information:
        print(a)
    print("")

    for t in Tipo_Information:
        print(t)
    print("")
  
    for c in Caracteristicas_Information:
        print(c)
    print("")

    for r in Relacion_Information:
        print(r)

def Agregar_en_tablas():
    contador = 0
    for t in Tipo_Information:
        if Tipo == t[1]:
            contador += 1
    
    if contador == 0:
        LLaves[0] += 1
        tipos.add_type(Id_tipo_animal = LLaves[0], Nombre_tipo_animal = Tipo)
    id_tipo = tipos.get_id_by_type(Nombre_tipo_animal = Tipo)

    contador = 0
    for a in Animal_Information:
        if animal_usuario[0] == a[1]:
            contador += 1
    
    if contador == 0:
        LLaves[1] += 1
        animal.add_animal(Id_animal = LLaves[1], Nombre_animal = animal_usuario[0], Id_tipo_animal = id_tipo)
        #jueputa
    
    contador = 0
    for ca in Lista_Caracteristicas:
        for c in Caracteristicas_Information:
            if ca == c[1]:
                contador += 1
        
        if contador == 0:
            LLaves[2] += 1
            caracteristicas.add_caracteristics(Id_caracteristica = LLaves[2], Nombre_caracteristica = ca)
        contador = 0

    contador = 0
    nom_id=animal.get_id_by_name(Nombre_animal=animal_usuario[0])
    for ca in Lista_Caracteristicas:  
        car_id=caracteristicas.get_id_by_caracteristic(Nombre_caracteristica=ca) 
        for r in Relacion_Information:
            if (nom_id[0]==r[1] and car_id[0]==r[2]):
                contador += 1

        if contador == 0:
            LLaves[3] += 1
            caracteristicas_animal.add_relation(Id_caracteristica_animal = LLaves[3], Id_animal = nom_id, Id_caracteristica = car_id)
        contador = 0
        

if __name__ == "__main__":
    tipos = Tipo_animal()
    animal = Animal()
    caracteristicas = Caracteristicas()
    caracteristicas_animal = Caracteristicas_animal()
    print("Hola, juguemos...")
    
    animales = []
    contadores = []
    LLaves = []

    Animal_Information = []
    Tipo_Information = []
    Caracteristicas_Information = []
    Relacion_Information = []

    Posibles_Animales = []
    animales_coinciden = []
    Lista_Caracteristicas = []

    Tamaño_tablas()

    animal_usuario = []
    Tipo = Consultar_tipo()
    Posibles_Animales=animal.get_id_by_type(Nombre_tipo_animal = Tipo)
    Comparar()