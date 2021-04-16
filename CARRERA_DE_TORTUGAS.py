# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:15:31 2020

@author: Nicolás
"""

from turtle import *
from random import randint
import turtle
import time

#Esta parte del código lo saque de este vídeo: https://www.youtube.com/watch?v=tXH-cY7N5bg&t=2s

def statudes():
    ##-------- SCREEN SETUP --------##
    setup(600, 500)
    title("Turtle Race")
    bgcolor("forest green")
    speed(0)
    
    # HEADING
    penup()
    goto(-180, 205)
    color("white")
    
    write("CARRERA DE TORTUGAS", font=("Arial", 20, "bold"))
    
    # DIRT
    goto(-250, 200)
    pendown()
    color("rosy brown")
    begin_fill()
    for i in range(2):
        forward(500)
        right(90)
        forward(400)
        right(90)
    end_fill()
    
    # FINISH LINE 1
    gap_size = 20
    shape("square")
    penup()
    
    # WHITE SQUARES ROW 1
    color("white")
    for i in range(10):
        goto(240, (170 - (i * gap_size * 2)))
        stamp()
    
    # WHITE SQUARES ROW 2
    for i in range(10):
        goto(240 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        stamp()
    
    # BLACK SQUARES ROW 1
    color("black")
    for i in range(10):
        goto(240, (190 - (i * gap_size * 2)))
        stamp()
    
    # BLACK SQUARES ROW 2
    for i in range(10):
        goto(240 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        stamp()
        
    # FINISH LINE 2
    gap_size = 20
    shape("square")
    penup()
    
    # WHITE SQUARES ROW 1
    color("white")
    for i in range(10):
        goto(-270, (170 - (i * gap_size * 2)))
        stamp()
    
    # WHITE SQUARES ROW 2
    for i in range(10):
        goto(-270 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
        stamp()
    
    # BLACK SQUARES ROW 1
    color("black")
    for i in range(10):
        goto(-270, (190 - (i * gap_size * 2)))
        stamp()
    
    # BLACK SQUARES ROW 2
    for i in range(10):
        goto(-270 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
        stamp()
        


##.............FUNCIONES.............##

def posicionarTortuga(t,i):
    TURTLE_SIZE = 1.5
    turtle.penup()
    turtle.goto(-250,i*50-150)
    turtle.showturtle

def texto(texto):
    t = Turtle()
    t.color("white")
    style = ("Courier",24,"italic")
    t.write(texto, font=style, align="center")
    t.hideturtle()
    
def preguntar_numero(texto):
    """Pide un valor numerico y retorna dicho valor como int"""
    while True:
        numero = input(texto)
        if not es_numero(numero):
            print("\nIntente de nuevo, valor inválido ")
            continue
        break
    
    return int(numero)

def es_numero(num):
    """Verifica si num es int"""
    try:
        int(num)
    except ValueError:
        return False
        
    return True

def buscarTortugaGanadora(lista):
    mayor = 0
    indice = -1
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            indice = i
    return indice

def mostrar_colores(colores):
    
    s = "["
    
    for c in colores:
        s += c + ","
    s += "]"
    return s

def run():
    fin_carrera = False
    while True:
        
        if fin_carrera == True:
            break
        
        else:
            for i in range(CANTIDAD_COMPETIDORES):
                if turtles[i].xcor() < longi_pista/2:
                    paso = randint(0,15)
                    desplazamiento[i] += paso
                    global cant_pasos
                    cant_pasos +=1
                    desplazamiento_total[i] += paso
                    turtles[i].forward(paso)
                    if turtles[i].xcor() <= -longi_pista/2:
                        fin_carrera = True
                        global cant_carreras
                        cant_carreras += 1
                        break
                elif turtles[i].xcor() >= longi_pista/2:
                    turtles[i].left(180)
                    turtles[i].forward(15)
    
    
def apostar():
    while True:

        monto_apuesta = preguntar_numero("\nIngrese cuanto quiere apostar, recuerde que no puede superar el 50% de su saldo disponible, además si su saldo es mayor a 1856 deberá elegir un monto mayor a dicho valor: ")
        if monto_total > 1856:
            if 1856 <= monto_apuesta <= monto_total/2:
                break
        elif monto_total <= 1856:
            if monto_apuesta <= monto_total/2:
                break
    return monto_apuesta

# CANTIDAD DE COMPETIDORES INPUT

while True:
    
    CANTIDAD_COMPETIDORES = preguntar_numero("\nIngrese una cantidad de competidores [ 2 min / 7 max] ")
    
    if 2 <= CANTIDAD_COMPETIDORES <= 7:
        
        break

# LONGITUD DE LA PISTA

longi_pista = 500
    
# RESULTADOS (LISTAS PARALELAS)

primeros = [0,0,0,0,0,0,0]

desplazamiento_total = []

# Colores

colores = ["cyan","light green","blue","purple","red","yellow","silver"]

colores_disponibles = colores[0:CANTIDAD_COMPETIDORES]

cant_pasos = 0

cant_gano = 0

cant_carreras = 0

cant_mas4000 = 0

monto_inicial = 28228

monto_total = 28228

monto_total_ganado = 0


for i in range(CANTIDAD_COMPETIDORES):
    desplazamiento_total.append(0)
    
menor_carrera_lenta = 999999999999

numero_carrera = 0

#CICLO DEL JUEGO 

while True:

    statudes()

    ##........LISTAS........##
    
    turtles = []
    
    desplazamiento = []
    
    monto_apuesta = 0
    
    desplazamiento_tortugas = 0

    # TORTUGAS
    
    for i in range(CANTIDAD_COMPETIDORES):
        
        turtle = Turtle()
        
        turtle.shape("turtle")
        
        turtle.color(colores[i])
        
        turtles.append(turtle)
        
        desplazamiento.append(0)
        
        posicionarTortuga(turtle,i)
    
    # VALIDACIÓN COLOR DE LA TORTUGA AL APOSTAR
    
    while True:
      select_color = input(""" Ingrese el color de la tortuga para apostar %s """%(mostrar_colores(colores_disponibles))).lower()
      
      if select_color == "cyan":
        break
      elif select_color == "light green":
        break
      elif select_color == "blue":
        break
      elif select_color == "purple":
        break
      elif select_color == "red":
        break
      elif select_color == "yellow":
        break
      elif select_color == "silver":
        break
      else:
        print("""\nIngrese un color válido dentro de las opciones %s """%(mostrar_colores(colores_disponibles)))
        
    monto_apuesta = apostar()
    
    if monto_apuesta > 4000:
        cant_mas4000 += 1
    
    # PAUSA 1 SEG ANTES DE LA CARRERA
    time.sleep(1)

    # CARRERA DE LAS TORTUGAS ////(EN CONSTRUCCION)////

    run()
    
    
    
    for i in range(CANTIDAD_COMPETIDORES):
            desplazamiento_tortugas += desplazamiento[i]
            
    velocidad_carrera  = desplazamiento_tortugas/cant_pasos
    
    if velocidad_carrera < menor_carrera_lenta:
        menor_carrera_lenta = velocidad_carrera
        numero_carrera = cant_carreras
    
    # GANADOR
    
    indice_ganador = buscarTortugaGanadora(desplazamiento)
    
    color_ganador = colores_disponibles[indice_ganador]
    
    primeros[indice_ganador] += 1
    
    texto("GANÓ LA TORTUGA %s"%(colores_disponibles[indice_ganador]).upper())
    print("\nGANÓ LA TORTUGA %s"%(colores_disponibles[indice_ganador]))
    
    if select_color == color_ganador:
        monto_total += (monto_apuesta*3)
        gano_perdio = "ganó"
        cant_gano += 1
        monto_total_ganado += (monto_apuesta*3)
        print("su saldo actual es de",monto_total)
    else:
        monto_total = monto_total - monto_apuesta
        gano_perdio = "perdió"
        print("su saldo actual es de",monto_total)
    
    #ARCHIVO
    archivo = open("archivo.txt", "a")
    archivo.write("\n%s,%s,%s"%(color_ganador,monto_apuesta,gano_perdio))
    archivo.close()
    # RESET
    
    while True:
        fin_juego = input("¿Desea seguir jugando? ")
        if fin_juego == "no":
            break
        elif fin_juego == "si":
            break
    if fin_juego == "no":
            break
    elif fin_juego == "si":
        clear()
        for i in range(CANTIDAD_COMPETIDORES):
            turtles[i].clear()
        
#Porcentaje de veces que el usuario ganó.

p_gano = cant_gano/cant_carreras*100

print("El porcentaje de veces que el usuario ganó es:",round(p_gano,2))
6
#Distancia total recorrida por todas las tortugas en todas las carreras

distancia_total_carreras = 0

for i in range(CANTIDAD_COMPETIDORES):
    
    distancia_total_carreras += desplazamiento_total[i]
print("La distancia total recorrida por todas las tortugas en todas las carreras es:",distancia_total_carreras)

#Monto total de dinero ganado por el jugador (considerar sólo las veces que ganó)

print("El monto total de dinero ganado por el jugador es:", monto_total_ganado)

#Cantidad de veces en que el jugador apostó más de 4000.

print("La cantidad de veces en que el jugador apostó más de 4000 es,",cant_mas4000)

#Color de la tortuga que más ganó

indice_mayor_color_ganador = buscarTortugaGanadora(primeros)

print("El color de la tortuga que más ganó es",colores_disponibles[indice_mayor_color_ganador])

#Número de la carrera más lenta. Considere la carrera más lenta aquella que tuvo el promedio de velocidades menor.

print("El número de la carrera más lenta es:",numero_carrera)

exitonclick()