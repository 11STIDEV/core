import json

with open('turmas.json', 'r') as arqv:
    turmas = json.load(arqv)
    print(turmas)
