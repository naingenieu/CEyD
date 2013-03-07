#! /usr/bin/env python
# -*- coding:utf8 -*-

# Copyright © 2013, naingenieu <nain.genieu@gmail.com>
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details.

import copy
from fractions import Fraction

class Polynome:
    def __init__(self, coeffs = [0]):
        self.coeffs = []
        for coeff in coeffs:
            self.coeffs.append(Fraction(coeff))

    def degre(self):
        return len(self.coeffs)

    def __add__(self, B):
        C = []
        if B.degre() > self.degre():
            degre, pol = self.degre(), copy.deepcopy(B)
        else:
            degre, pol = B.degre(), copy.deepcopy(self)
        k = 0
        while k < degre:
            C.append(self.coeffs[k] + B.coeffs[k])
            k+=1
        while k < pol.degre():
            C.append(pol.coeffs[k])
            k+=1
        return Polynome(C)

    def multX(self):
        self.coeffs.insert(0,0.) 

    def __mul__(self, B):
        A = copy.deepcopy(self)
        C = []
        D = Polynome()
        if not isinstance(B, Polynome):
            for coeff in self.coeffs:
                C.append(coeff* B)
            return Polynome(C)
        else:
            for k in range(len(B.coeffs)):
                D = D + (A * B.coeffs[k]) 
                A.multX()
            return D

    def __div__(self, c):
        A = []
        for coeff in self.coeffs:
            A.append(coeff / c)
        return Polynome(A)

    def __str__(self):  
        return str(self.coeffs)

    def eval(self,X):
        value = 0
        for coeff in self.coeffs[::-1]:
            value = value * X + coeff
        return value


def combine(uid, chaine):
    pc, resul = 0, ""
    chaine = str(chaine)
    for pu in range(len(uid)):
        resul += chr( ord(uid[pu]) ^ ord(chaine[pc]) )
        pc = (pc + 1) % len(chaine) 
    return resul


if __name__ == '__main__':
    p = Polynome([1,2,1])
    print p.eval(1.5)