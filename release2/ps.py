from typing import List
from datetime import date

class Producte:
    def __init__(self, id: int, nom: str, preu: float, descripcio: str):
        self.id = id
        self.nom = nom
        self.preu = preu
        self.descripcio = descripcio
        self.resenyes = []

    def obtenir_detalls(self):
        return f"{self.nom}: {self.descripcio}, Preu: {self.preu}€"

    def obtenir_puntuacio_mitjana(self):
        if not self.resenyes:
            return 0
        return sum(resenya.puntuacio for resenya in self.resenyes) / len(self.resenyes)


class Item:
    def __init__(self, id: int, producte: Producte, quantitat: int):
        self.id = id
        self.producte = producte
        self.quantitat = quantitat
        self.resenya = None

    def calcular_subtotal(self):
        return self.quantitat * self.producte.preu


class Resenya:
    def __init__(self, puntuacio: int, comentari: str):
        self.puntuacio = puntuacio
        self.comentari = comentari


class Comanda:
    def __init__(self, id: int, data: date, estat: str):
        self.id = id
        self.data = data
        self.estat = estat
        self.productes = []

    def calcular_total(self):
        total = 0
        for item in self.productes:
            total += item.calcular_subtotal()
        return total

    def afegir_productes(self, productes: List[Item]):
        self.productes.extend(productes)

    def valorar_producte(self):
        for item in self.productes:
            puntuacio = int(input(f"Introdueix la puntuació per {item.producte.nom} (de 1 a 5): "))
            comentari = input("Introdueix un comentari (opcional): ")
            item.resenya = Resenya(puntuacio, comentari)
            item.producte.resenyes.append(item.resenya)


class PersonalShopper:
    def __init__(self, id: int, nom: str, especialitat: str):
        self.id = id
        self.nom = nom
        self.especialitat = especialitat

    def recomanar_productes(self):
        pass

    def crear_llista_compra(self, preferencies: List[str]):
        pass


class Client:
    def __init__(self, id: int, nom: str, correu: str, adreca: str, contrasenya: str):
        self.id = id
        self.nom = nom
        self.correu = correu
        self.adreca = adreca
        self.contrasenya = contrasenya

    def realitzar_comanda(self, productes: List[Item]):
        comanda = Comanda(1, date.today(), "Pendent")
        comanda.afegir_productes(productes)
        return comanda

    def seguir_comanda(self, comanda: Comanda):
        return f"Comanda {comanda.id}: Estat - {comanda.estat}, Total - {comanda.calcular_total()}€"


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
