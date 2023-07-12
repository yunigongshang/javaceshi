# ------------------------青春有你---------------------------
print("输入quit表示录入完毕:")
dict={}
for i in range(1,50):
    key=input("请输入选手的姓名：\n")
    if key=="quit":
       break
    value=int(input("请输入选手的票数：\n"))
    dict[key]=value

result = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(result)
for i in range(0,len(result)):
    print("第{}名:".format(i+1), result[i][0], "成绩为:", result[i][1], "分",)


#--------------------------------------------------------6.4.1
d={'a':1,'b':2,'c':3}
test=[('name','Sakura'),('age',20)]
d=dict(test)
d
d=dict(name='Sakura',age=20)
d
a=dict()
a


#--------------------------------------------------------6.4.2
week={'Mon':1,'Tue':2,'Wen':3,'Thu':4}
print("initial week:",week)
week['Fri']=5
print("after week[Fri]=5:",week)
del week['Fri']
print("after del week[Fri]:",week)
week.update({'Fri':5})
print("after week.update({'Fri':5}):",week)
week.pop('Fri')
print("after week.pop('Fri'):",week)

test={'Mon':1}
'Fri' in test
test.get('Fri')
test.get('Fri',-1)

x={'a':1,'b':[2,3,4]}
y=x.copy()
y['a']=5
y['b'].remove(3)
y
x

d={'one':1,'two':2,'three':3,'four':4}
print(d)
d.clear()
print(d)

d={}
dd=d
d['one']=1
d['two']=2
print(dd)
print(d)
d.clear()
print(d)
print(dd)

d=dict.fromkeys(['three','two','one'])
print(d)
d=dict.fromkeys(['three','two','one'],'unknow')
print(d)

d={'three':3,'two':2,'one':1}
print(d)
list=d.items()
for key,value in list:
    print(key,':',value)

d={'one':1,'two':2,'three':3}
print(d)
list=d.keys()
print(list)
d={'one':1,'two':2,'three':3}
print(d)
print(d.setdefault('one',1))
print(d.setdefault('four',4))
print(d)

d={
    'one':123,
    'two':2,
    'three':3,
    'test':2
    }
d.values()


#--------------------------------------------------------6.5.1
set('123456')
set('aabbecddee')


#--------------------------------------------------------6.5.2
test=set([1,2,3])
test
test.add(3)
test
test.add(6)
test
test.remove(3)
test

a=set('I Love')
a.add('python')
a

a=set('I Love')
a.update('python')
a

a=set('I Love')
a.remove('python')
a

x=set('spam')
y=set(['h','a','m'])
x,y
x&y
x|y
x-y