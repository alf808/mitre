#!/home/nemo/PycharmProjects/mitre/venv/bin/python3
'''This application will extract information from the pyattck database.
Currently the app only handles Remote Desktop Protocol technique for the actor option.
Usage:  ./app.py -a <ACTOR>
        ./app.py -m <MALWARE>

Sample:
        ./app.py -a Axiom
        ./app.py -m Proton
'''

import argparse
from pyattck import Attck
attack = Attck()


def grab_techniques(actor):
    for technique in attack.techniques:
        if 'Remote Desktop Protocol' == technique.name:
            print(f"Technique name: {technique.name}")
            for mitigation in technique.mitigation:
                print('\t' + mitigation.name)


def grab_actor(act):
    for actor in attack.actors:
        if actor.name == act:
            print('Actor name: ' + actor.name)
            for technique in actor.techniques:
                if technique.name == 'Remote Desktop Protocol':
                    grab_techniques(actor.name)

def grab_malware(mal):
    for mw in attack.malwares:
        if mw.name == mal:
            print(f'Malware: ' + mw.name)
            print('Techniques associated with: ' + mw.name)
            for technique in mw.techniques:
                print('\t' + technique.name)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")
    # group = parser.add_mutually_exclusive_group()
    parser.add_argument('-a', help="actor will return techniques and mitigation")
    parser.add_argument('-m', help="malware will return mitigation")
    args = parser.parse_args()

    if args.actor:
        grab_actor(args.actor)
    else:
        grab_malware(args.mal)
