#! /usr/bin/env python
# -*- coding:utf8 -*-

# Copyright © 2013, naingenieu <nain.genieu@gmail.com>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import os, sys
from chiffre import chiffre
from dechiffre import dechiffre

__version__ = "0.1"
__author__  = "naingenieu"
__mail__    = "nain.genieu@gmail.com"

def effacer():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def mainMenu(prem = 0):
    if prem == 0:
        effacer()
        print "Bienvenue dans CSyD version " + __version__+ " par "+ __author__
        print "Pour tous commentaires, envoyer un mail à " + __mail__
    elif prem == 1:
        effacer()
        print "Choix incorrect, veuillez recommencer"
    print 
    print
    print "Que voulez vous faire?"
    print "[1] Décomposer un secret"
    print "[2] Retrouver un secret"
    print "[0] Quitter"
    try:
        choix = int(raw_input("Votre choix > "))
    except:
        mainMenu(1)
    if choix == 1:
        menuDecomp(False)
    elif choix == 2:
        menuComp(False)
    elif choix == 0:
        print "Au revoir"
        sys.exit()
    else:
        mainMenu(1)



def menuDecomp(fich_secret):
    effacer()
    fichier = None
    if not fich_secret:
        print "Nous allons procéder à la décompostion de votre secret"
        secret = raw_input("Entrez la chaine à décomposer : ")
    degre = 0
    try:
        while True:
            degre = int(raw_input("Combien de clés voulez-vous qu'il soit nécessaire pour recomposer le secret > ")) -1
            if degre > 0:
                break
            print "Le nombre de clés nécessaire à la recomposition du secret doit être supérieur à deux"            
    except:
        effacer()
        print "L'entrée doit être un nombre, veuillez recommencer"
        mainMenu()
    nb_cle = 0
    try:
        while True:
            nb_cle = int(raw_input("Combien de clés voulez-vous générer > "))
            if nb_cle > (degre+1):
                break
            print "Le nombre de clés générées doit être supérieur au nombre nécessaire à la recomposition"            
    except:
        effacer()
        print "L'entrée doit être un nombre, veuillez recommencer"
        mainMenu()
    print "Calcul en cours..."
    print "Les clés générés sont :"
    print "======================================================" 
    keys = chiffre(secret, degre, nb_cle)
    for key in keys:
        print key
    print "======================================================" 
    print "Stockez les précieusement, à plusieurs endroits"


def menuComp(fich_secret):
    effacer()
    fichier = None
    if not fich_secret:
        print "Nous allons procéder à la découverte de votre secret"
    keys = []
    print "Rentrez les clés secrètes, finissez par FIN : "
    key = ""
    k = 0
    while True:
        k += 1
        key=raw_input("Clé "+ str(k)+" > ")
        if key == "FIN":
            break
        else:
            keys.append(key)
    print "Découverte du secret ...."
    print "======================================================" 
    print dechiffre(keys)
    print "======================================================" 

if __name__ == '__main__':
    mainMenu(0)
