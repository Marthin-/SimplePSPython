#!/usr/bin/env python
import configparser
import time
import math
import random

def help():
    print("-- Pathfinder feuille de perso interactive --")
    print(" Taper une des commandes suivantes pour voir")
    print("   les informations du perso dans fp.txt :")
    print("       Taper 'help' pour revoir ce texte")
    print("             ou 'exit' pour quitter")
    print("---------------------------------------------")
    print("general  -  carac  -  saves  -  res  -  pv")
    print("    attaque  -  armes  -   def   -  comp")
    print("---------------------------------------------")
    print(" Pour changer une valeur taper ")
    print(" set <catégorie> <nom> <valeur>")
    print(" (ex. : set pv actuels 16)")
    print("---------------------------------------------")
    print("   Pour calculer le bonus total à une ")
    print("          compétence taper calc <comp>")
    print("   les noms de compétences n'ont pas d'accent")
    print("---------------------------------------------")
    print("    \nPour effectuer un test de compétence")
    print("             taper test\n")
    print("  Taper save pour sauvegarder la fiche /!\\")

def get_mod(config, car):
    return (math.floor((int(config['carac'][car]) - 10) / 2 ))

def set_value(config, section, key, value=""):
    config[section][key] = value

def calc_bonus(config, comp):
    if comp in ['escalade', 'natation']:
        return int(get_mod(config, 'for')) + int(config['comp'][comp])
    elif comp in ['acrobatie', 'discretion', 'equitation', 'escamotage', 'evasion', 'sabotage', 'vol']:
        return int(get_mod(config, 'dex')) + int(config['comp'][comp])
    elif comp in ['adm', 'artisanat', 'exploration', 'folklore', 'geo', 'histoire', 'ingenierie', 'mysteres', 'nature', 'noblesse', 'plans', 'religion', 'estimation', 'linguistique']:
        return int(get_mod(config, 'int')) + int(config['comp'][comp])
    elif comp in ['perception', 'secours', 'profession', 'psychologie', 'survie']:
        return int(get_mod(config, 'sag')) + int(config['comp'][comp])
    elif comp in ['bluff', 'deguisement', 'diplomatie', 'dressage', 'intimidation', 'representation', 'uom']:
        return int(get_mod(config, 'cha')) + int(config['comp'][comp])

def test_comp(config,comp):
    dice = random.randint(1,20)
    total = dice + int(calc_bonus(config, comp))
    print("Bonus..." + str(calc_bonus(config, comp)))
    time.sleep(1)
    print("Roule roule roule...")
    time.sleep(1)
    print("Dé......" + str(dice))
    print("Total..." + str(total))

def menu():
    config = configparser.ConfigParser()
    config.read('fp.txt')
    help()
    while 1:
        rawcom = str(input("______________\n|> "))
        com = rawcom.split(" ")[0]
        if com != 'set' and com != 'exit' and com != 'help' and com != 'save' and com != 'calc' and com != 'test':
            print("==== " + com.upper() + " ====")
            for key in config[com]:
                print(key + ": " + config[com][key])
        elif com == 'exit':
            break
        elif com == 'help':
            help()
        elif com == 'set':
            toto = ""
            try:
                toto = rawcom.split(" ")[3]
            except IndexError:
                toto = ""
            set_value(config, rawcom.split(" ")[1], rawcom.split(" ")[2], toto)
        elif com == 'save':
            with open('fp.txt', 'w') as configfile:
                config.write(configfile)
        elif com == 'calc':
            print("bonus en " + rawcom.split(" ")[1] + " : " + str(calc_bonus(config, rawcom.split(" ")[1])))
        elif com == 'test':
            test_comp(config, rawcom.split(" ")[1])

if __name__ == "__main__":
    menu()
