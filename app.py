#!/home/nemo/PycharmProjects/mitre/venv/bin/python3
'''This application will extract information from the pyattck database.

Usage:
                ./app.py
Upon invoking app, follow menu options. Once you select an option, a list of possible names will be shown. You will then be prompted to pick one of those names.

If you choose an invalid menu option, you will get an error message and be returned to the menu.
'''
import argparse
from pyattck import Attck
import sys
import random

# global variables
attack = Attck()
error_list = ["You Chose Poorly", "Jen says: Are you fricking serious!", "Smooth move exlax!", "Hey lolo make mo bettah choice!"]


def grab_techniques(att):
    '''this will grab techniques used by threat actors'''
    for technique in attack.techniques:
        if technique.name.lower() == att.lower():
            print("Attack technique name: " + technique.name)
            print("Description: " + technique.description)
            print("These are mitigations: ")
            for mitigation in technique.mitigation:
                print('\t' + mitigation.name)


def grab_tactics(tac):
    for tactic in attack.tactics:
        if tac.lower() == tactic.name.lower():
            for tec in tactic.techniques:
                print('\t' + tec.name)


def grab_actor(act):
    '''find if actor exists in database then invoke techniques'''
    for actor in attack.actors:
        if actor.name.lower() == act.lower():
            print('Actor name: ' + actor.name)
            print('Description: ' + actor.description)
            print('Techniques used:')
            for technique in actor.techniques:
                print('\t' + technique.name)

                    
def grab_malware(mal):
    '''grab malware and attack techniques'''
    for mw in attack.malwares:
        if mw.name.lower() == mal.lower():
            print('Malware: ' + mw.name)
            print('Description: ' + mw.description)
            print("Actors: " + mw.name)
            for actors in mw.actors:
                print('\t' + actors.name)
            print('Attack techniques associated with: ' + mw.name)
            for technique in mw.techniques:
                print('\t' + technique.name)

def grab_tools(tol):
    for tools in attack.tools:
        if tools.name.lower() == tol.lower():
            print('Tool: ' + tools.name)
            print('Desription: ' + tools.description)
            print('Actors: ' + tools.name)
            for actors in tools.actors:
                print('\t' + actors.name)
            print('Techniques associated with: ' + tools.name)
            for tech in tools.techniques:
                print('\t' + tech.name)

def print_actors():
    actor_list = [act.name for act in attack.actors]
    print("Here is a sample list of actors.")
    print(*actor_list, sep = "\t")


def print_malwares():
    print("Here is a sample list of malware.")
    malware_list = [mal.name for mal in attack.malwares]
    print(*malware_list, sep = "\t")


def print_attacks():
    print("Here is a sample list of attack techniques.")
    attack_list = [att.name for att in attack.techniques]
    print(*attack_list, sep = "\t")


def print_tactics():
    print("Here is a sample list of tactics.")
    tactics_list = [att.name for att in attack.tactics]
    print(*tactics_list, sep = "\t")

def print_tools():
    print("List of tools.")
    tools_list = [tol.name for tol in attack.tools]
    print(*tools_list, sep ='\t')
    

def main():
    choice = "0"
    while True:
        print("\nMenu Choices:")
        print("(1) Threat Actor\t(2) Malware\t(3) Attack to Mitigate\t(4) Tactics\t(5) Tools\t(x) Exit")

        choice = input("Enter your choice:  ")

        if choice == "1":
            print_actors()
            type = input("Input Actor: ")
            grab_actor(type)
        elif choice == "2":
            print_malwares()
            type = input("Input Malware: ")
            grab_malware(type)
        elif choice == "3":
            print_attacks()
            type = input("Attack to mitigate: ")
            grab_techniques(type)
        elif choice == "4":
            print_tactics()
            type = input("Tactic techniques: ")
            grab_tactics(type)
        elif choice == "5":
            print_tools()
            type = input("Enter Tool: ")
            grab_tools(type)
        elif choice == "x":
            sys.exit("Thanks for wasting our time")
        else:
            msg = random.choice(error_list)
            print("\n" + msg)
            

if __name__ == "__main__":
    main()
    

    

    