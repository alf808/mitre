#!/home/nemo/PycharmProjects/mitre/venv/bin/python3
'''This application will extract information from the pyattck database.
Currently the app only handles Remote Desktop Protocol technique for the actor option.
Usage:  ./app.py -actor <ACTOR>
        ./app.py -mal <MALWARE>
        ./app.py -attack <ATTACK>

Sample:
        ./app.py -actor Axiom
        ./app.py -mal Proton
        ./app.py -attack Scripting
'''
import argparse
from pyattck import Attck
import sys
attack = Attck()

def grab_techniques(att):
    '''this will grab techniques used by threat actors'''
    for technique in attack.techniques:
        if technique.name == att:
            print(f"Attack technique name:   {technique.name}")
            print("Description: " + technique.description)
            print("These are mitigations: ")
            for mitigation in technique.mitigation:
                print('\t' + mitigation.name)


def grab_actor(act):
    '''find if actor exists in database then invoke techniques'''
    for actor in attack.actors:
        if actor.name == act:
            print('Actor name: ' + actor.name)
            print('Description: ' + actor.description)
            print('Techniques used:')
            for technique in actor.techniques:
                print('\t' + technique.name)

                    
def grab_malware(mal):
    '''grab malware and attack techniques'''
    for mw in attack.malwares:
        if mw.name == mal:
            print('Malware: ' + mw.name)
            print('Description: ' + mw.description)
            print('Attack techniques associated with: ' + mw.name)
            for technique in mw.techniques:
                print('\t' + technique.name)
def main():
    choice = "0"
    while True:
        print("Main Choice: Choose 1 of 3 choices")
        print("Choose 1 for Threat Actor")
        print("Choose 2 for Type of Malware")
        print("Choose 3 for Technique Mitigation")
        print("Choose 4 to exit")

        choice = input("Enter your choice:  ")

        if choice == "1":
            type = input("Input Actor: ")
            grab_actor(type)
        elif choice == "2":
            type = input("Input Malware: ")
            grab_malware(type)
        elif choice == "3":
            type = input("Attack to mitigate: ")
            grab_techniques(type)
        elif choice == "4":
            sys.exit("Thanks for wasting our time")
        else:
            print("Read this is Jens voice: Are you fricking serious!")
            
            

if __name__ == "__main__":
    main()
    

    

    