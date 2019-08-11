# Threat Actor and Malware Enumeration

This application will extract information from the pyattck database.

Don't run flags concurrently.
    -actor flag will return an actor with RDP as a technique with recommended mitigation
    -mal flag will return entered malware with associated attack techniques
    -attack flag will return the mitigation techniques against the attack


## Usage:
        ./app.py -actor <ACTOR>
        ./app.py -mal <MALWARE>
        ./app.py -attack <ATTACK>

## Sample:
        ./app.py -actor Axiom
        ./app.py -mal Proton
        ./app.py -attack Scripting



