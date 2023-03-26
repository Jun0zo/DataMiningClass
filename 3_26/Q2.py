# -*- coding: utf-8 -*-

# Q2.py
import random

from Engines.Perceptron import Perceptron

DEBUG = 0
NORMAL = 1

# {isClear: 0 | 1, isTogether: 0 | 1, isClose: 0 | 1}
# isClear : 날씨 (0: 흐림, 1: 맑음)
# isTogether : 여자친구의 동행 여부 (0: 혼자간다, 1: 같이 간다)
# isClose : 콘서트장의 위치 (0: 전철역과 멀리 떨어짐, 1: 전철역 주변)

# 환경 (isClear, isTogether, isClose)를 랜덤으로 초기화
environmentNameDict = {'isClear':'날씨', 'isTogether':'여자친구 동행여부', 'isClose':'콘서트장 위치'}
environmentDict = {f"{environmentName}":random.randrange(0,1+1) for environmentName in environmentNameDict.keys()}
weightsDict = {f"{environmentName}":round(random.random(), 2) for environmentName in environmentNameDict.keys()}

print('현재 날씨가 맑고' if environmentDict['isClear'] else '날씨가 흐리고', end=', ')
print('여자친구와 함께갈 수 있고' if environmentDict['isTogether'] else '여자친구 없이 혼자 가야되고', end=', ')
print('콘서트장이 전철역 주변이다.' if environmentDict['isClose'] else '콘서트장이 전철역과 멀리 떨어져있다.')

sortedWeightsDict = dict(sorted(weightsDict.items(), key=lambda item: item[1], reverse=True))
print('현재 나에게 중요도는 ', end='')
for environmentName, weight in sortedWeightsDict.items():
    print(f'{environmentNameDict[environmentName]} ({weight})', end=', ')
print('순이다.')

perceptron  = Perceptron(weights=weightsDict.values(), mode=DEBUG)
y = perceptron.forward(environmentDict.values())
print('이 상황이면 콘서트에 가야겠다.' if y else '이 상황이면 안 가야겠다.')
