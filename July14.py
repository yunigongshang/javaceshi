n=[11,22,33,44,55,66,77,88,99,90]
a={'m':[],'s':[]}
for i in range(len(n)):
    if n[i]>66:
        a['m'].append(n[i])
    else :
        a['s'].append(n[i])
print(a)