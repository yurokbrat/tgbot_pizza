import json

sp = []
with open('mat.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            sp.append(n)

with open('cenzor.json', 'w', encoding= 'utf-8') as e:
    json.dump(sp,e)