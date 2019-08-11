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
attack = Attck()

def grab_techniques(att):
    '''this will grab techniques used by threat actors'''
    for technique in attack.techniques:
        if technique.name == att:
            print(f"Attack technique name: {technique.name}")
            print("These are mitigations: ")
            for mitigation in technique.mitigation:
                print('\t' + mitigation.name)


def grab_actor(act):
    '''find if actor exists in database then invoke techniques'''
    for actor in attack.actors:
        if actor.name == act:
            print('Actor name: ' + actor.name)
            print('Techniques used:')
            for technique in actor.techniques:
                print('\t' + technique.name)

                    
def grab_malware(mal):
    '''grab malware and attack techniques'''
    for mw in attack.malwares:
        if mw.name == mal:
            print(f'Malware: ' + mw.name)
            print('Attack techniques associated with: ' + mw.name)
            for technique in mw.techniques:
                print('\t' + technique.name)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-actor', help="actor will return techniques")
    group.add_argument('-mal', help="malware will return attack technique")
    group.add_argument('-attack', help="attack will return mitigation techniques")

    args = parser.parse_args()

    if args.actor:
        grab_actor(args.actor)
    elif args.attack:
        grab_techniques(args.attack)
    else:
        grab_malware(args.mal)
