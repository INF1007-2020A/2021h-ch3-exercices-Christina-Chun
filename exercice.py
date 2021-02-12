#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:              #a est nb a virg flottante (float) et reponse aussi
    return math.sqrt(a)                          #peut aussi: racine_carree = math.sqrt(a)
                                                 #                   return racine_carree

def square(a: float) -> float:
    return a ** 2                                #ou pow(a,2)


def average(a: float, b: float, c: float) -> float:
    moyenne = (a,b,c)
    return sum(moyenne)/len(moyenne)                #can i do that?      #ou return sum([a,b,c])/3  crochets c une liste


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return math.radians(angle_degs + angle_mins/60 + angle_secs/3600)       #One minute is equal to 1/60 degrees, One second is equal to 1/3600 degrees


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    min = (degrees - math.floor(degrees)) * 60    #on veut les decimales pour les min et sec, floor:rounds a number DOWN to the nearest integer VS ceil
    sec = (min - math.floor(min)) * 60
    return math.floor(degrees), math.floor(min), sec


def to_celsius(temperature: float) -> float:           #(°F – 32) x 5/9 = °C
    return (temperature - 32)*(5/9)


def to_farenheit(temperature: float) -> float:
    return temperature/(5/9) + 32


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
