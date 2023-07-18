n=[11,22,33,44,55,66,77,88,99,90]
a={'m':[],'s':[]}
for i in range(len(n)):
    if n[i]>66:
        a['m'].append(n[i])
    else :
        a['s'].append(n[i])
print(a)


n=eval(input('请输入值'))
i=0
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=n*3+1
    i=i+1
print('{}次'.format(i))
