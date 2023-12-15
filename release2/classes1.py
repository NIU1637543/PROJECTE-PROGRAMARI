#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:45:49 2023

@author: aina
"""
#CLASSE CATÀLEG
class Cataleg():
    def __init__(self, seccions):
        self._seccions=seccions
    
    def productes_seccio(self, s):
        prod = self.seccions[s].productes_subseccio()
        return prod
        
    def productes_marca(self, m):
        count = 0
        for seccio in self._seccions:
            count += seccio.productes_marca(m)
        return count
            
    def recomanacions(self, p):
        for seccio in self._seccions:
            recom = seccio.recomanacions(p)
        return recom


#CLASSE SECCIÓ
class Seccio():
    def __init__(self, nom, descripcio, subseccions):
        self._nom = nom
        self._descripcio = descripcio
        self._subseccions = subseccions

    def nom(self):
        return self._nom
        
    def descripcio(self):
        return self._descripcio
        
    def productes_seccio(self):
        prod = {}
        for seccio in self._subseccions:
            prod[seccio.nom()] = seccio.productes_subseccio()
        return prod
            
    def productes_marca(self, m):
        count = 0
        for seccio in self._subseccions:
            count += seccio.productes_marca(m)
        return count
        
    def recomanacions(self, p):
        for seccio in self._seccions:
            recom = seccio.recomanacions(p)
        return recom


#CLASSE SUBSECCIÓ
class Subseccio():
    def __init__(self, nom, descripcio, productes):
        self._nom = nom
        self._descripcio = descripcio
        self._productes = productes
    
    def nom(self):
        return self._nom
        
    def descripcio(self):
        return self._descripcio
        
    def productes_subseccio(self):
        return len(self._productes.keys())

    def productes_marca(self, m):
        count = 0
        for prod in self._productes:
            marca = prod.marca()
            if marca.nom() == m
                count += 1
        return count
        
    def recomanacions(self, p):
        for prod in self._productes:
            if prod.nom() == p:
                recom = prod.recomanats()
        return recom


#CLASSE PRODUCTE
class Producte():
    def __init__(self, nom, marca, model, seccio, subseccio, preu, disponibilitat, descripcio, recomanats):
        self._nom = nom
        self._marca = marca
        self._model = model
        self._seccio = seccio
        self._subseccio = subseccio
        self._preu = preu
        self._disponibilitat = disponibilitat
        self._descripcio = descripcio
        self._recomanats = recomanats
    
    def nom(self):
        return self._nom
        
    def marca(self):
        return self._marca
        
    def model(self):
        return self._model
        
    def seccio(self):
        return self._seccio
        
    def subseccio(self):
        return self._subseccio
        
    def preu(self):
        return self._preu
        
    def disponibilitat(self):
        return self._disponibilitat
    
    def descripcio(self):
        return self._descripcio
        
    def recomanats(self):
        return self._recomanats
        

#CLASSE MARCA
class Marca():
    def __init__(self, nom, descripcio):
        self._nom = nom
        self._descripcio = descripcio
    
    def marca(self):
        return self._nom
        
    def descripcio(self):
        return self._descripcio


#CLASSE MODEL
class Model():
    def __init__(self, nom, descripcio):
        self._nom = nom
        self._descripcio = descripcio
    
    def model(self):
        return self._nom
        
    def descripcio(self):
        return self._descripcio

