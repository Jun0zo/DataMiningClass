# -*- coding: utf-8 -*-
# Q3.py

from DB.DB import DB
from Engines.DistanceMachine import DistanceMachine


peopleDB = DB([
    {"name":"김영희", "age": 23, "residence_year":2, "house_type": 2},
    {"name":"배철수", "age": 40, "residence_year":10, "house_type": 1},
], pk_name="name")

person1 = "김영희"
person2 = "배철수"

distanceMachine = DistanceMachine(db=peopleDB)

norm2 = distanceMachine.getL2Norm(person1, person2)
print(f'{person1}과 {person2}의 유클리드 거리 : {norm2}')

norm1 = distanceMachine.getL1Norm(person1, person2)
print(f'{person1}과 {person2}의 맨허튼 거리 : {norm1}')