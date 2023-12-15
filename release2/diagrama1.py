#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:08:59 2023

@author: marioamadorhurtado
"""

from typing import Dict

#CLASSE CATÀLEG
class Cataleg:
    def __init__(self, seccions: Dict[str, 'Seccio']):
        self.seccions = seccions

    def productes_seccio(self, s: str) -> Dict[str, int]:
        return self.seccions[s].productes_subseccio()

    def productes_marca(self, m: str) -> int:
        count = 0
        for seccio in self._seccions:
            count += seccio.productes_marca(m)
        return count
        
    def recomanacions(self, p: str) -> Dict[str, 'Producte']:
        for seccio in self._seccions:
            recom = seccio.recomanacions(p)
        return recom
    
    def mostrar_recomanacions(self):
        for seccio_nom, seccio in self.seccions.items():
            for subseccio_nom, subseccio in seccio.subseccions.items():
                for producte_nom, producte in subseccio.productes.items():
                    print(f"=== Recomanacions per {producte_nom} ===")
                    recomanacions = producte.recomanats
                    for recom_nom, recom in recomanacions.items():
                        print(f"  - {recom_nom}")
                    print()


#CLASSE SECCIÓ
class Seccio:
    def __init__(self, nom: str, descripcio: str, subseccions: Dict[str, 'Subseccio']):
        self.nom = nom
        self.descripcio = descripcio
        self.subseccions = subseccions

    def nom(self) -> str:
        return self.nom

    def descripcio(self) -> str:
        return self.descripcio

    def productes_seccio(self) -> Dict[str, int]:
        prod = {}
        for seccio in self._subseccions:
            prod[seccio.nom()] = seccio.productes_subseccio()
        return prod

    def productes_marca(self, m: str) -> int:
        count = 0
        for seccio in self._subseccions:
            count += seccio.productes_marca(m)
        return count
        
    def recomanacions(self, p: str) -> Dict[str, 'Producte']:
        for seccio in self._seccions:
            recom = seccio.recomanacions(p)
        return recom


#CLASSE SUBSECCIÓ
class Subseccio:
    def __init__(self, nom: str, descripcio: str, productes: Dict[str, 'Producte']):
        self.nom = nom
        self.descripcio = descripcio
        self.productes = productes

    def nom(self) -> str:
        return self.nom

    def descripcio(self) -> str:
        return self.descripcio

    def productes_subseccio(self) -> Dict[str, int]:
        return len(self._productes.keys())

    def productes_marca(self, m: str) -> int:
        count = 0
        for prod in self._productes:
            marca = prod.marca()
            if marca.nom() == m:
                count += 1
        return count
        
    def recomanacions(self, p: str) -> Dict[str, 'Producte']:
        for prod in self._productes:
            if prod.nom() == p:
                recom = prod.recomanats()
        return recom
        
        
#CLASSE PRODUCTE
class Producte:
    def __init__(self, nom: str, marca: 'Marca', model: 'Model', seccio: str, subseccio: str,
                 preu: int, disponibilitat: str, descripcio: str, recomanats: Dict[str, 'Producte']):
        self.nom = nom
        self.marca = marca
        self.model = model
        self.seccio = seccio
        self.subseccio = subseccio
        self.preu = preu
        self.disponibilitat = disponibilitat
        self.descripcio = descripcio
        self.recomanats = {}
                     
    def __str__(self):
        return f"Producte: {self.nom}\n" \
               f"Marca: {self.marca.marca()}\n" \
               f"Model: {self.model.model()}\n" \
               f"Secció: {self.seccio}\n" \
               f"Subsecció: {self.subseccio}\n" \
               f"Preu: {self.preu}\n" \
               f"Disponibilitat: {self.disponibilitat}\n" \
               f"Descripció: {self.descripcio}\n" \
               f"Recomanacions: {list(self.recomanats.keys())}\n"


    def nom(self) -> str:
        return self.nom

    def marca(self) -> str:
        return self.marca.marca()

    def model(self) -> str:
        return self.model.model()

    def seccio(self) -> str:
        return self.seccio

    def subseccio(self) -> str:
        return self.subseccio

    def preu(self) -> int:
        return self.preu

    def disponibilitat(self) -> str:
        return self.disponibilitat

    def descripcio(self) -> str:
        return self.descripcio

    def recomanacions(self) -> Dict[str, 'Producte']:
        return self.recomanats
    
    def incluir_recom(self, dic):
        self.recomanats = dic


#CLASSE MARCA
class Marca:
    def __init__(self, nom: str, descripcio: str):
        self.nom = nom
        self.descripcio = descripcio

    def marca(self) -> str:
        return self.nom

    def descripcio(self) -> str:
        return self.descripcio


#CLASSE MODEL
class Model:
    def __init__(self, nom: str, descripcio: str):
        self.nom = nom
        self.descripcio = descripcio

    def model(self) -> str:
        return self.nom

    def descripcio(self) -> str:
        return self.descripcio




def mostrar_informacio(catalog):
    for seccio_nom, seccio in catalog.seccions.items():
        print(f"=== Secció: {seccio_nom} ===")
        print(f"Descripció: {seccio.descripcio}")
        print("Subseccions:")
        for subseccio_nom, subseccio in seccio.subseccions.items():
            print(f"  - Subsecció: {subseccio_nom}")
            print(f"    Descripció: {subseccio.descripcio}")
            print("    Productes:")
            for producte_nom, producte in subseccio.productes.items():
                print(f"      - {producte}")
            print()
        print()
        

nike = Marca("Nike", "Nike és una reconeguda marca global de roba, calçat i accessoris esportius. Fundada el 1964, l'empresa estatunidenca és coneguda pel seu distintiu logotip Swoosh i el seu compromís amb la innovació en el disseny i la tecnologia en productes esportius. Nike és àmpliament associada amb atletes d'elit i és una de les marques líders en la indústria de l'esport i la moda casual. El seu lema, Just Do It, reflecteix el seu enfocament motivacional i la seva presència en una varietat d'esports i estils de vida.")
adidas = Marca("Adidas", "Adidas és una reconeguda marca de roba, calçat i accessoris esportius d'origen alemany. Fundada el 1949 per Adolf Dassler, la marca s'ha destacat per la seva innovació en el disseny i tecnologia de productes esportius. Adidas és coneguda pel seu distintiu logotip de les tres ratlles i ha aconseguit una gran influència en la cultura urbana i la moda casual, fusionant funcionalitat i estil en els seus productes. La marca patrocina nombrosos atletes i equips esportius a nivell mundial.")
reebok = Marca("Reebok", "Reebok és una marca global de roba i calçat esportiu amb un enfocament en la forma física i l'estil de vida actiu. Fundada el 1958, Reebok ha estat coneguda per les seves innovacions en calçat esportiu i col·laboracions amb atletes i celebritats.")

airforce1 = Model("Air Force 1", "Les sabatilles Nike Air Force 1 són un icònic model de calçat esportiu introduït per Nike el 1982. Conegudes pel seu disseny versàtil i atemporal, presenten una part superior de pell i una sola gruixuda amb tecnologia d'amortiment Air, proporcionant comoditat i suport. Les Air Force 1 han perdurat com a clàssic de la moda urbana i són apreciades tant pel seu estil elegant com pel seu rendiment durador.")
yeezy = Model("Yeezy", "Les sabatilles Yeezy són una línia de calçat esportiu dissenyada en col·laboració entre el raper i dissenyador de moda Kanye West i la marca Adidas. Conegudes pel seu estil modern i avantguardista, les Yeezy han guanyat popularitat pel seu disseny distintiu, materials d'alta qualitat i la seva associació amb la cultura de la moda urbana. Cada llançament de Yeezy sovint genera una gran expectació entre els aficionats a la moda i els entusiastes del calçat, convertint-les en una de les línies de sabatilles més buscades i col·leccionables.")
classic_leather = Model("Classic Leather", "Les sabatilles Reebok Classic Leather són un model atemporal que ha perdurat en la moda des del seu llançament el 1983. Amb un disseny simple i elegant, aquestes sabatilles són conegudes per la seva comoditat i versatilitat.")
ultraboost = Model("Ultra Boost", "Les sabatilles Adidas Ultra Boost són conegudes per la seva tecnologia d'amortiment Boost, que proporciona una sensació de comoditat i retorn d'energia. Aquest model combina rendiment i estil, sent popular tant per a activitats esportives com per a l'ús casual.")
nano_x = Model("Nano X", "Reebok Nano X és un model dissenyat específicament per a entrenament creuat. Ofereix estabilitat i durabilitat, sent una elecció popular entre els entusiastes del fitness.")


airforce1white = Producte("Air Force 1 Blanques", nike, airforce1, "Casual", "Casual Esportiu", 100, "Disponible", "Les sabatilles Air Force 1 blanques són un icònic model de calçat esportiu dissenyat per Nike. Introduïdes el 1982, aquestes sabatilles han perdurat en la moda urbana degut al seu estil atemporal i versatilitat. Caracteritzades pel seu distintiu disseny de tall baix, sola gruixuda i part superior de pell blanca, les Air Force 1 blanques són conegudes per la seva comoditat i capacitat per complementar una varietat d'estils casuals. El seu estatus com a clàssic de la moda urbana les ha convertit en un element bàsic a la cultura sneaker.", 
                          {})
yeezywhite = Producte("Yeezy Blanques", adidas, yeezy, "Sabatilles", "Sabatilles Còmodes", 150, "Esgotat", "Les sabatilles Yeezy blanques són un icònic model de calçat dissenyat en col·laboració entre el raper Kanye West i la marca Adidas. Amb un estil minimalista i modern, aquestes sabatilles solen presentar una part superior de teixit Primeknit en to blanc, proporcionant comoditat i una aparença elegant. La línia Yeezy, coneguda per la seva exclusivitat i demanda, ha contribuït a establir les sabatilles blanques Yeezy com un símbol d'estil urbà i contemporani.", 
                      {})
classic_white = Producte("Classic Blanques", reebok, classic_leather, "Casual", "Casual Clàssic", 80, "Disponible", "Les sabatilles Reebok Classic Blanques són un icona d'estil casual. Amb la seva part superior de pell blanca i disseny clàssic, aquestes sabatilles ofereixen comoditat i versatilitat per a diverses ocasions.", 
                         {})
ultraboost_black = Producte("Ultra Boost Negres", adidas, ultraboost, "Sneakers", "Sneakers Còmodes", 130, "Disponible", "Les sabatilles Adidas Ultra Boost negres són ideals per a aquells que busquen comoditat i estil. El seu disseny versàtil les fa aptes tant per a l'ús diari com per a activitats esportives.", 
                            {})
nano_x_blue = Producte("Nano X Blaves", reebok, nano_x, "Entrenament", "Entrenament Creuat", 110, "Disponible", "Les sabatilles Reebok Nano X blaves són una opció popular per a entrenaments creuats. Ofereixen estabilitat i suport durant activitats físiques intenses.", 
                       {})
air_max = Producte("Air Max", nike, airforce1, "Casual", "Casual Esportiu", 120, "Disponible", "Les sabatilles Nike Air Max són conegudes per la seva icònica unitat Air Max a la sola, proporcionant amortiment i comoditat. Aquest model és adequat per a un estil casual i esportiu.", 
                   {})

dic = {"Air Force 1 Blanques": airforce1white, "Yeezy Blanques": yeezywhite, "Classic Blanques": classic_white, "Ultra Boost Negres": ultraboost_black, "Nano X Blaves": nano_x_blue, "Air Max": air_max}
airforce1white.incluir_recom(dic)
yeezywhite.incluir_recom(dic)
classic_white.incluir_recom(dic)
ultraboost_black.incluir_recom(dic)
nano_x_blue.incluir_recom(dic)
air_max.incluir_recom(dic)

casualdeportivo = Subseccio("Casual Esportiu", "La secció de Sabatilles Casual Esportiu ofereix calçat versàtil dissenyat per combinar comoditat i estil en situacions informals i esportives. Aquestes sabatilles estan dissenyades per proporcionar un aspecte modern i relaxat, ideal per a l'ús diari, alhora que incorporen característiques esportives per oferir confort durant activitats físiques lleugeres. Amb una fusió de moda i funcionalitat, les sabatilles casual esportives són una elecció popular per a aquells que busquen un calçat que s'adapti a diverses ocasions.", 
                            {"Air Force 1 Blanques": airforce1white, "Classic Blanques": classic_white})
casualclasico = Subseccio("Casual Clàssic", "La secció de Sabatilles Casual Clàssic ofereix calçat versàtil dissenyat per combinar comoditat i estil en situacions informals i esportives. Aquestes sabatilles estan dissenyades per proporcionar un aspecte modern i relaxat, ideal per a l'ús diari, alhora que incorporen característiques esportives per oferir confort durant activitats físiques lleugeres. Amb una fusió de moda i funcionalitat, les sabatilles casual esportives són una elecció popular per a aquells que busquen un calçat que s'adapti a diverses ocasions.", 
                          {"Air Force 1 Blanques": classic_white, "Ultra Boost Negres": ultraboost_black, "Air Max": air_max})
sneakerscomodas = Subseccio("Sabatilles Còmodes", "La secció de sabatilles sneakers còmodes en aquest catàleg ofereix una selecció de calçat informal i modern, dissenyat per oferir comoditat sense sacrificar l'estil. Inclou diverses marques i models que combinen funcionalitat i moda, ideal per a aquells que busquen un calçat versàtil i còmode en el seu dia a dia.", 
                            {"Yeezy Blanques": yeezywhite, "Nano X Blaves": nano_x_blue})

casual = Seccio("Casual", "Les sabatilles casuals són un tipus de calçat versàtil dissenyat principalment per a l'ús diari i situacions informals. Es caracteritzen per la seva comoditat, estil i adaptabilitat a diversos vestits. Generalment, les sabatilles casuals combinen disseny modern amb materials lleugers, oferint una opció còmoda i a la moda per a activitats quotidianes. La seva popularitat radica en la seva capacitat per oferir un equilibri entre estil relaxat i funcionalitat.", 
                {"Casual Esportiu": casualdeportivo, "Casual Clàssic": casualclasico})
sneakers = Seccio("Sabatilles", "Les sabatilles sneakers són un tipus de calçat esportiu dissenyat per oferir comoditat i suport durant activitats físiques. Conegudes pel seu estil casual i versatilitat, les sneakers han evolucionat més enllà de la seva funció original de calçat esportiu per convertir-se en una elecció popular de moda urbana. Es caracteritzen pel seu disseny lleuger, sola amortiguada i una àmplia varietat d'estils, colors i materials que s'adapten tant a l'activitat física com a l'ús diari.", 
                  {"Sabatilles Còmodes": sneakerscomodas})

cataleg = Cataleg({"Casual": casual, "Sabatilles": sneakers})

mostrar_informacio(cataleg)
cataleg.mostrar_recomanacions()
