data = [
    ['남', '노인', '좌석'],
    ['남', '노인', '입석'],
    ['남', '노인', '좌석'],
    ['여', '노인', '입석'],
    ['여', '노인', '좌석'],
    ['여', '어린이', '입석'],
    ['여', '어린이', '좌석'],
    ['여', '어린이', '입석'],
    ['남', '어린이', '입석'],
    ['남', '노인', '좌석']
]

def func1(X, data):
    all_cnt = 0
    r_cnt = 0
    for row in data:
        if row[2] == X:
            if row[0] == '남':
                r_cnt += 1
            all_cnt += 1 
    print(f'f1 : {r_cnt} / {all_cnt}')
    return r_cnt / all_cnt

def func2(X, data):
    all_cnt = 0
    r_cnt = 0
    for row in data:
        if row[2] == X:
            r_cnt += 1
        all_cnt += 1 
    print(f'f2 : {r_cnt} / {all_cnt}')
    return r_cnt / all_cnt

def func3(data):
    r_cnt = 0
    all_cnt = 0
    for row in data:
        if row[0] == '남' and row[1] == '어린이':
            r_cnt += 1
        all_cnt += 1 
    print(f'f3 : {r_cnt} / {all_cnt}')
    return r_cnt / all_cnt

def doMain(X):
    return (func1(X, data)*func2(X, data) / func3(data))


P1 = doMain('좌석')
print('남자 어린아이기 입석할 확률 :', P1)
P2 = doMain('입석')
print('남자 어린아이기 좌석할 확률 :', P2)

