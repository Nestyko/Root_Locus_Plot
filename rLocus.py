"""
    Author: Nestor Luis Tobón
    E-mail: nltobon@gmail.com, nltobon@hotmail.com
    Donations in Paypal at: nltobon@hotmail
"""
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial as poly
import numpy
import operator
import sys
import functools
from languages import language
from user_input import input_float, input_int


max_k = 100
density = 0.01

def get_x_y(polynom):
    x = []
    y = []
    for i in polynom:
        x.append(numpy.real(i))
        y1 = str(numpy.imag(i))
        y1 = y1[:-2]
        y.append(float(y1))
    return x,y

def get_x_y_from_g_h(g, h, range_of_k=100, density=0.01):
    k = 0.0
    x_final = []
    y_final = []
    for i in range(int(range_of_k*(1/density))):
        pc = (k*g)+h
        x,y = get_x_y(pc.roots())
        x_final.append(x)
        y_final.append(y)
        k+=density
        sys.stdout.write("\rCargando... " + str(round(((k*100)/range_of_k),2)) + "%")
        sys.stdout.flush()
    return x_final, y_final

def str_constants(lang):
    if lang == 'es':
        return 'Maximo valor de K = ' + str(max_k) + '\nDensidad = ' + str(density) + '\nSi desea cambiarlas ingrese -1'
    elif lang == 'en':
        return 'Max value of K = ' + str(max_k) + '\nDensity = ' + str(density) + '\nIf you want to change them, insert -1'




def prompt_constants(lang):
    lan = language[lang]
    print(lan['prompt_constants'])


def input_poly(lang):
    lan = language[lang]

    pgrade = input_int(lan['input_poly'], lang)

    p = [0]*(pgrade+1)
    for i in range(pgrade+1):
        p[i] = input_float("x^" + str(i) + ": ", lang)
    return poly(p)

def main(lang):
    max_k = 100
    density = 0.01
    lan = language[lang]
    print("\n"*80) #Clear Screen
    print(str_constants(lang))#Display constants
    print('*'*40)
    g_num = -1
    while(g_num == -1):
        print()
        print(lan['g'])
        g_num = input_int(lan['g_num'],lang)
        if g_num == -1:
            print()
            max_k = input_int(lan['max_k'], lang)
            print()
            density = input_float(lan['prompt_density'], lang)
    g = [None]*g_num
    for i in range(g_num):
        g[i] = input_poly(lang)
    print(lan['h'])
    h_num = input_int(lan['h_num'],lang)
    h = [None]*h_num
    for i in range(h_num):
        h[i] = input_poly(lang)

    g_poly = functools.reduce(operator.mul, g, 1)

    h_poly = functools.reduce(operator.mul, h, 1)

    x_final, y_final = get_x_y_from_g_h(g_poly,h_poly, max_k, density)

    plt.plot(x_final,y_final)
    plt.xlabel(lan['real_axis'])
    plt.ylabel(lan['img_axis'])
    plt.title(lan['graph_title'])
    plt.show()

def welcome():
    print("\n"*80) #Clear Screen
    print("************Root Locus Plot************")
    print("***************************************")
    print("Please select the language:")
    print("Por favor seleccione el idioma:")
    print("1.- English")
    print("2.- Español")
    print("0.- Exit/Salir")
    return input_int("")

while(True):
    sel = welcome()
    if sel == 1:
        main('en')
    elif sel == 2:
        main('es')
    elif sel == 0:
        break






