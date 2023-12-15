from typing import List
from datetime import date

#CLASSE CLIENT
class Client:
    def __init__(self, nif: int, nom: str, cognom:str , email: str, adreca: str, contrasenya: str, telefon:int, comandes, personal, ):
        self._nif = nif
        self._nom = nom
        self._cognom = cognom
        self._adreca = adreca
        self._contrasenya = contrasenya
        self._email = email
        self._comandes=comandes
        self._personal=personal
    
    def nif(self):
        return self._nif 

    def nom(self):
        return self._nom 

    def adreca(self):
        return self._adreca

    def contrasenya(self):
        return self._contrasenya

    def email(self):
        return self._email

    def personal(self):
        return self._personal


#CLASSE PERSONAL
class Personal:
    def __init__(self, nif: int, nom: str, cognom: str, data, contrasenya, email, clients):
        self._nif = id
        self._nom = nom
        self._data=data
        self._contrasenya=contrasenya
        self._email=email
        self._clients=clients
        
    def nif(self):
        return self._nif 

    def nom(self):
        return self._nom 

    def data(self):
        return self._data

    def contrasenya(self):
        return self._contrasenya

    def email(self):
        return self._email

    def clients(self):
        return self._clients


#CLASSE COMANDA
class Comanda:
    def __init__(self, id: int, productes, data: date, preu : int):
        self._id = id
        self._productes = productes
        self._data = data
        self._preu = preu

    def id(self):
        return self._id

    def productes(self):
        return self._productes

    def data(self):
        return self._data

    def preu(self):
        return self._preu
        
    def valorar(self):
        for nom, prod  in self.productes.items():
            be=False
            while not be:
                puntuacio = int(input(f"Introdueix la puntuació per {nom} (de 1 a 5): "))
                if 1<=puntuacio<=5:
                    be=True
                else:
                    print("Puntuació no vàlida, introdueix un valor del 1 al 5")
            ressenya = input("Introdueix un comentari (opcional): ")
            data=datetime.datetime.now()
            valoracio = Valoracio(puntuacio, ressenya, data)
            prod.afegir_valoracio(valoracio)


#CLASSE VALORACIÓ
class Valoracio:
    def __init__(self, puntuacio, ressenya, data)
        self._puntuacio=puntuacio
        self._ressenya=ressenya
        self._data=data

    def puntuacio(self):
        return self._puntuacio
        
    def ressenya(self):
        return self._ressenya
        
    def data(self):
        return self._data
        

#CLASSE PRODUCTE

class Producte:
    def __init__(self, nom: str, marca: Marca, model: Model, seccio: str, subseccio: str,
                 preu: int, disponibilitat: str, descripcio: str, recomanats: Dict[str, "Producte"]):
        self._nom = nom
        self._marca = marca
        self._model = model
        self._seccio = seccio
        self._subseccio = subseccio
        self._preu = preu
        self._disponibilitat = disponibilitat
        self._descripcio = descripcio
        self._recomanats = recomanats
        self._valoracions = []

    def __str__(self):
        return f"Producte: {self.nom}\n" \
               f"Marca: {self.marca.marca()}\n" \
               f"Model: {self.model.model()}\n" \
               f"Secció: {self.seccio}\n" \
               f"Subsecció: {self.subseccio}\n" \
               f"Preu: {self.preu}\n" \
               f"Disponibilitat: {self.disponibilitat}\n" \
               f"Descripció: {self.descripcio}\n" \
               f"Recomendacions: {self.recomanats}\n"

    def nom(self) -> str:
        return self._nom

    def marca(self) -> str:
        return self._marca

    def model(self) -> str:
        return self._model

    def seccio(self) -> str:
        return self._seccio

    def subseccio(self) -> str:
        return self._subseccio

    def preu(self) -> int:
        return self._preu

    def disponibilitat(self) -> str:
        return self._disponibilitat

    def descripcio(self) -> str:
        return self._descripcio

    def recomanacions(self) -> Dict[str, 'Producte']:
        return self._recomanats
                     
    def mitjana_nota(self):
        sum=0
        for val in self._valoracions:
            sum+=val.nota
        return sum/len(self._valoracions)

    def ressenyes(self):
        ressenyes=[]
        for val in self._valoracions:
            ressenyes.append(val.ressenya)
        return ressenyes

    def afegir_valoracio(self, val):
        self._valoracionS.append(val)





if __name__ == "__main__":
    producte_1 = Producte(1, "Producte 1", 10.0, "Descripció del producte 1")
    producte_2 = Producte(2, "Producte 2", 15.0, "Descripció del producte 2")

    item_1 = Item(1, producte_1, 2)
    item_2 = Item(2, producte_2, 1)

    client = Client(1, "Nom Client", "client@example.com", "Adreça Client", "password")
    comanda = client.realitzar_comanda([item_1, item_2])

    print(client.seguir_comanda(comanda))
    comanda.valorar_producte()

    for item in comanda.productes:
        print(f"Detalls del producte: {item.producte.obtenir_detalls()}")
        if item.resenya:
            print(f"Puntuació mitjana del producte: {item.producte.obtenir_puntuacio_mitjana()}")
            print(f"Resenya del producte: Puntuació: {item.resenya.puntuacio}, Comentari: {item.resenya.comentari}")
        else:
            print("Encara no s'ha valorat aquest producte.")
        print("-----")
