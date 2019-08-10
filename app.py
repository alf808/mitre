#!/home/nemo/PycharmProjects/mitre/venv/bin/python3
import argparse
from pyattck import Attck
attack = Attck()


def grab_techniques(actor):
    for technique in attack.techniques:
        if 'Remote Desktop Protocol' == technique.name:
            print(f"Technique name: {technique.name}")
            for mitigation in technique.mitigation:
                print(mitigation.name)


def main(act):
    for actor in attack.actors:
        if actor.name == act:
            print('Actor name: ' + actor.name)
            for technique in actor.techniques:
                if technique.name == 'Remote Desktop Protocol':
                    # print(technique.name)
                    grab_techniques(actor.name)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="")

    parser.add_argument('actor', help="mandatory actor")
    args = parser.parse_args()

    main(args.actor)
