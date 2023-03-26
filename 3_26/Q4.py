# -*- coding: utf-8 -*-

# Q4.py

import re

from DB.DB import DB
from Engines.SimilarityMachine import SimilarityMachine

DEBUG = 0
NORMAL = 1
    
scientistDB = DB([
    {"name":"Jeff Ulman", "docs": [
        re.split(r', |\s', "Jeff Ullman, Jennifer Widom, XML Security, VLDB04"),
        re.split(r', |\s', "Jeff Ullman, Hector Garcia-Molina, Hashing, VLDB04"),
        re.split(r', |\s', "Jeff Ullman, XML Query, VLDB04"),
        re.split(r', |\s', "Jeff Ullman, XML, VLDB06"),
    ]},
    {"name":"Jenifer Widom", "docs": [
        re.split(r', |\s', "Hector Garcia-Molina, Jennifer Widom, Jeff Ullman, Ranking, VLDB04")
    ]}
], pk_name="name")

actorDB = DB([
    {"name":"Tom Cruise", "movies": [
        "Collateral 04".split(' '),
        "Last Samurai 03".split(' '),
        "Minority Report 02".split(' '),
        "Vanilla Sky 02".split(' '),
    ]},
    {"name":"T. Cruise", "movies": [
        'Vanilla Sky'.split(' '),
        'The Last Samurai'.split(' '),
        'Mission Impossible'.split(' '),
        'Minority Report'.split(' '),
    ]}
], pk_name="name")

documentDB = DB([
    {"id": "1", "docs": [[
        *["monetary" for i in range(2)], 
        *["performance" for i in range(7)], 
        *["transition" for i in range(3)]
    ]]},
    {"id": "2", "docs": [[
        *["monetary" for i in range(0)], 
        *["performance" for i in range(2)], 
        *["transition" for i in range(3)]
    ]]}
])

key1 = "Jeff Ulman"
key2 = "Jenifer Widom"
jaccardMachine = SimilarityMachine(db=scientistDB, mode=DEBUG)
jaccardSimilarity = jaccardMachine.getJaccard(key1, key2)
print(f'{key1}과 {key2}의 자카드 유사도 : {jaccardSimilarity}\n')

key1 = "Tom Cruise"
key2 = "T. Cruise"
cosineMachine = SimilarityMachine(db=actorDB, mode=DEBUG)
cosineDistance = cosineMachine.getCosine(key1, key2)
print(f'{key1}과 {key2}의 코사인 유사도 : {cosineDistance}\n')

key1 = "1"
key2 = "2"
cosineMachine2 = SimilarityMachine(db=documentDB, mode=DEBUG)
cosineDistance2 = cosineMachine2.getCosine(key1, key2)
print(f'document {key1}과 document {key2}의 코사인 유사도 : {cosineDistance2}')