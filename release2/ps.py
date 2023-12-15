from typing import List
from datetime import date

#CLASSE PRODUCTE
class Producte:
    def __init__(self, nom: str, preu: float, descripcio: str):
        self.nom = nom
        self.preu = preu
        self.descripcio = descripcio
        self._valoracions = []

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
        self._valoracion.append(val)



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
            puntuacio = int(input(f"Introdueix la puntuació per {nom} (de 1 a 5): "))
            ressenya = input("Introdueix un comentari (opcional): ")
            data=datetime.datetime.now()
            valoracio = Valoracio(puntuacio, ressenya, data)
            prod.afegir_valoracio(valoracio)


#CLASSE VALORACIÓ
class Valoracio:
    def __init__(self, puntuacio, ressenya, data)
        self._puntuacio=puntuacio
        self._ressenya=ressenya
        self._data=sata

    def puntuacio(self):
        return self._puntuacio
        
    def ressenya(self):
        return self._ressenya
        
    def data(self):
        return self._data
        

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
