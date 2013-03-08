#! /usr/bin/env python
# -*- coding:utf8 -*-

# Copyright © 2013, naingenieu <nain.genieu@gmail.com>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import polynome, sys
from base64 import  b64encode
from string import ascii_letters, digits
from random import choice

def genPoly(nombre, degre):
    pol = [nombre]
    rnd_max=256**4
    while rnd_max < nombre:
        rnd_max*=2
    while degre > 0:
        pol.append(random.randint(0,rnd_max))
        degre -= 1
    return polynome.Polynome(pol)

def string2Int(string):
    return sum([ord(c)*256**k for k,c in enumerate(string)])

def genListe(nb_cle):
    return [random.randint(1,100*nb_cle) for k in range(nb_cle)]

def genKeys(pol, liste_val):
    return [(val,pol.eval(val)) for val in liste_val]


def chiffre(chaine, degre, nb_cle):
    pol = genPoly(string2Int(chaine), degre)
    keys = genKeys(pol, genListe(nb_cle))
    randpool = ascii_letters + digits
    uid = "".join([choice(randpool) for k in range(degre+1)])
    return [b64encode(polynome.combine(uid,y)+":"+str(x)+":"+str(y)) for x,y in keys]

