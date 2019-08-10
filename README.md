# Threat Actor and Malware Enumeration

This application will extract information from the pyattck database.
Currently the app only handles Remote Desktop Protocol technique for the actor option.

Don't run both flags concurrently.
    -a flag will return an actor with RDP as a technique with recommended mitigation
    -m flag will return entered malware with mitigation for that malware

## Usage:
        ./app.py -actor <ACTOR>
        ./app.py -mal <MALWARE>

## Sample:
        ./app.py -actor Axiom
        ./app.py -mal Proton



