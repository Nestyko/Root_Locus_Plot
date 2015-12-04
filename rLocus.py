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
import os

max_k = 100
density = 0.01

def debug_file(x_final, y_final, range_of_k=100, density=0.01):
    print("\nGenerating debug File\n")
    try:
        dir_fd = os.open('debug', os.O_RDONLY)
        def opener(path, flags):
            return os.open(path, flags, dir_fd=dir_fd)
        k = 0
        with open('debug.html', 'w', opener=opener) as f:
            for x,y in zip(x_final,y_final):
                print ("For k=" + str(k) + ": \n<ul><li>X: " + str(x) + "</li>\n<li>Y: " + str(y) + "</li></ul>", file=f)
                sys.stdout.write("\rCargando... " + str(round(((k*100)/range_of_k),2)) + "%")
                sys.stdout.flush()
                k+=density
    except Exception:
        print("Error Opening File")
    else:
        pass
    finally:
        os.close(dir_fd)



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


spanish = {
    'g' : "Por favor, ingrese G(s) ('Ceros')",
    'g_num' : "¿Cuantos Polinomios? : ",
    'h' : "Por favor, ingrese H(s) ('Polos')",
    'h_num' : "¿Cuantos Polinomios? : ",
    'input_poly' : "Por favor, ingrese el grado del polinomio: ",
    'real_axis' : 'Eje Real',
    'img_axis' : "Eje Imaginario",
    'graph_title' : 'Gráfica del Lugar de las Raices Reales',
    'max_k' : 'Por favor ingrese el maximo valor de K\nDefecto = 100\nK = ',
    'prompt_density' : 'Por favor ingrese la densidad (el tamaño de paso de k para cada iteración):\nDefecto = 0.01\nDensidad = ',
    'prompt_constants' : "Ingrese las constantes\nMientras mas grande sea k mas tiempo tomará en terminar la gráfica"

}

english = {
    'g' : "Please insert the G(s) ('Zeros')",
    'g_num' : "How many polynoms?",
    'input_poly' : "Please insert the polynom grade: ",
    'h' : "Please insert the H(s) ('Poles')",
    'h_num' : "How many polynoms?",
    'real_axis' : 'Real Axis',
    'img_axis' : "Imaginary Axis",
    'graph_title' : 'Root Locus Plot',
    'max_k' : 'Please insert the maximun value of k\nDefault: 100\nK = ',
    'prompt_density' : 'Please insert the density (the step of k for each iteration):\nDefault: 0.01\nDensity =  ',
    'prompt_constants' : "Insert the constants\n The greater the k the greater the time consumed by the graphic"
}

languages = {
    'es' : spanish,
    'en' : english,
}

def prompt_constants(lang):
    lan = languages[lang]
    print(lan['prompt_constants'])


def input_poly(lang):
    lan = languages[lang]

    pgrade = int(input(lan['input_poly']))

    p = [0]*(pgrade+1)
    for i in range(pgrade+1):
        p[i] = int(input("x^" + str(i) + ": "))
    return poly(p)

def main(language):
    max_k = 100
    density = 0.01
    lan = languages[language]
    print("\n"*80) #Clear Screen
    print(str_constants(language))#Display constants
    print('*'*40)
    g_num = -1
    while(g_num == -1):
        print()
        print(lan['g'])
        g_num = int(input(lan['g_num']))
        if g_num == -1:
            print()
            max_k = int(input(lan['max_k']))
            print()
            density = float(input(lan['prompt_density']))
    g = [None]*g_num
    for i in range(g_num):
        g[i] = input_poly(language)
    print(lan['h'])
    h_num = int(input(lan['h_num']))
    h = [None]*h_num
    for i in range(h_num):
        h[i] = input_poly(language)

    g_poly = functools.reduce(operator.mul, g, 1)

    h_poly = functools.reduce(operator.mul, h, 1)

    x_final, y_final = get_x_y_from_g_h(g_poly,h_poly, max_k, density)
    debug_file(x_final,y_final, max_k, density)

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
    return int(input())

while(True):
    sel = welcome()
    if sel == 1:
        main('en')
    elif sel == 2:
        main('es')
    elif sel == 0:
        break






