from .DB.DB import DB
from Engines.DistanceMachine import DistanceMachine


peopleDB = DB([
    {"name":"김영희", "age": 23, "residence_year":2, "house_type": 2},
    {"name":"배철수", "age": 40, "residence_year":10, "house_type": 1},
], pk_name="name")
distanceMachine = DistanceMachine(db=peopleDB)
res1 = distanceMachine.getL1Norm("김영희", "배철수")
print(1, res1)
res2 = distanceMachine.getL2Norm("김영희", "배철수")
print(2, res2)