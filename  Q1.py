# -*- coding: utf-8 -*-

# Q1.py
from DB import DB
from SCMachine import SCMachine

DEBUG = 0
NORMAL = 1

db = DB([
    {"id":1, "items":['빵', '우유']},
    {"id":2, "items":['빵', '기저귀', '맥주', '달걀']},
    {"id":3, "items":['우유', '기저귀', '맥주', '콜라']},
    {"id":4, "items":['빵', '우유', '기저귀', '맥주']},
    {"id":5, "items":['빵', '우유', '기저귀', '콜라']},
])


svmuchine = SCMachine(db, mode=DEBUG)
supportValue = svmuchine.getSupportValue(["우유", "기저귀"], ["맥주"], "items")
print('support값 : ', supportValue)
confidenceValue = svmuchine.getConfidencetValue(["우유", "기저귀"], ["맥주"], "items")
print('confidence값 : ', confidenceValue)