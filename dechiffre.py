#! /usr/bin/env python
# -*- coding:utf8 -*-

# Copyright © 2013, naingenieu <nain.genieu@gmail.com>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import polynome
import sys
from base64 import  b64decode

def lagrange(X, Y):
    L = polynome.Polynome()
    for k in range(len(X)):
        Lk = polynome.Polynome([1])
        for j in range(len(X)):
            if j == k : continue
            else:
                Lk *= (polynome.Polynome([-X[j],1])) / (X[k] - X[j])
        L += Lk * Y[k]
    return L

def dechiffre(keys):
    X, Y = [], []
    for ind, key in enumerate(keys):
        key = b64decode(key)
        uidxor, x ,y = key.split(":")
        uid = polynome.combine(uidxor, y) 
        if ind == 0:
            uidsuite = uid
            need = len(uid) - 1
            X.append(int(x))
            Y.append(int(y))
        else:
            if uid == uidsuite :
                if need > 0:
                    X.append(int(x))
                    Y.append(int(y))
                    need-=1
                else:
                    break
            else:
                print "La clé numéro " + str(ind+1) +" ne correspond pas"
                sys.exit()
    if need > 0:
        print "Nombre de clés insuffisant"
        sys.exit()
    pol = lagrange(X, Y)
    return int2String(int(pol.eval(0)))

def int2String(nombre):
    s = ""
    while nombre > 0:
        s += chr(nombre % 256)
        nombre = nombre / 256
    return s

if __name__ == '__main__':
    L = polynome.Polynome([2,2,1,2,3,4])
    X = [2,1,4,3,-1,-6]
    Y = [L.eval(x) for x in X]
    P = lagrange(X,Y)
    print P.eval(0) == L.eval(0)
    string = "test"
    test = sum([ord(c)*256**k for k,c in enumerate(string)])
    print string == int2String(test)