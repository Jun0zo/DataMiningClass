# -*- coding: utf-8 -*-

# Q1.py
from DB.DB import DB
from Engines.SCMachine import SCMachine

DEBUG = 0
NORMAL = 1

db = DB([
    {"id":1, "items":['빵', '우유']},
    {"id":2, "items":['빵', '기저귀', '맥주', '달걀']},
    {"id":3, "items":['우유', '기저귀', '맥주', '콜라']},
    {"id":4, "items":['빵', '우유', '기저귀', '맥주']},
    {"id":5, "items":['빵', '우유', '기저귀', '콜라']},
])


scmachine = SCMachine(db, mode=DEBUG)

# support({우유, 기저귀}, {맥주}) : 우유, 기저귀, 맥주를 모두 포함한 거래 수
supportValue = scmachine.getSupportValue(["우유", "기저귀"], ["맥주"], "items")
print('support값 : ', supportValue)

# confidence({우유, 기저귀}, {맥주}) : 우유와 기저귀가 있는 거래내역 중 맥주도 함께 포함한 거래 수
confidenceValue = scmachine.getConfidencetValue(["우유", "기저귀"], ["맥주"], "items")
print('confidence값 : ', confidenceValue)