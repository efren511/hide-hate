#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored
import subprocess
import os

intro = """
    Fsocity
██╗░░██╗██╗░░██╗
██║░░██║██║░░██║
███████║███████║
██╔══██║██╔══██║
██║░░██║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝
    Hide Hate
Oculata La Información
Dentro De Imagenes
Guarda Tu Odio
En Ellas 7w7
"""
opciones = """1) Ocultar
2) Descubrir
3) Salir
"""

def ocultar():
    msg_list = []
    line_input = input(colored("\nIngrese la información a ocultar:(Enter para terminar)\n", "blue"))
    msg_list.append(line_input)
    while line_input != "":
        line_input = input(colored("\nIngrese la información a ocultar:\n", "blue"))
        msg_list.append(line_input)
    img = input(colored("Ingrese la imagen donde quiere ocultar la información:\n", "blue"))
    with open("msg.txt", "w") as info:
        for line in msg_list:
            info.write(line)
            if(line != msg_list[-1]):
                info.write("\n")
    command_zip = subprocess.run(["zip", "-r", "msg.zip", "msg.txt"])
    command_cat = subprocess.run("cat msg.zip >> {}".format(img), shell=True)
    command_rm = subprocess.run(["rm", "msg.txt", "msg.zip"])
    print(colored("\nInformación ocultada en {}\n".format(img), "green"))

def descubrir():
    img_input = input(colored("\nIngrese la imagen de donde obtener información:\n", "blue"))
    if os.path.exists(img_input):
        command_unzip = subprocess.run(["unzip", img_input], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if command_unzip.returncode == 1:
            command_cat = subprocess.run("cat msg.txt", shell=True, stdout=subprocess.PIPE)
            print(colored("\nInformación encontrada!", "green"))
            print("\n"+command_cat.stdout.decode())
            command_rm = subprocess.run(["rm", "msg.txt"])
        else:
            print(colored("\nNo se encontro información oculta!\n", "red"))
    else:
        print(colored("\nNo se encontro la imagen!\n", "red"))

def main():
    print(intro)
    while True:
        print(colored(opciones, "yellow"))
        selected = input(colored("Ingrese una opcion: ","blue"))
        if selected == "1":
            ocultar()
        elif selected == "2":
            descubrir()
        elif selected == "3":
            exit()
        else:
            print(colored("Comando desconocido", "red"))
if __name__ == '__main__':
    main()
