n={'z':'12123',
    'c': '2313'}
while True:
    n1=list(n.keys())
    print('联系人列表')
    for i in range(0,len(n1)):
        print('{}.{}'.format(i+1,n1[i]))
    print('\n\n')
    print('1.添加   2.查看   3.修改   4.删除   0.退出')
    su=eval(input('请输入你要服务'))
    match su:
        case 1:
            a=str(input('请输入你要添加的姓名'))
            if n.get(a)==None:
                b=str(input('请输入手机号'))
                n[a]=b
            else:
                print('你输入的联系人已存在')
        case 2:
            a=str(input('请输入你要查询的姓名'))
            b=n.get(a)
            if b!=None:
                print('{}的手机号为{}'.format(a,b))
                input('\n回车进行下一步......')
            else:
                print('不存在此联系人')
        case 3:
            a=str(input('请输入你要修改的姓名'))
            if n.get(a)!=None:
                b=str(input('请输入修改后的手机号'))
                n[a]=b
            else :
                print('该联系人不存在')
        case 4:
            a=str(input('请输入你要删除的姓名'))
            if n.get!=None:
                del n[a]
                print('删除成功')
            else:
                print('不存在此联系人')
        case 0 :
            break
            
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


#--------------------------------------------------------5.1
def show_hello():
    '''定义一个函数,输出Hello World'''
    print('Hello World')
show_hello()
print(show_hello.__doc__)


#--------------------------------------------------------5.2
def fid(n):
    '''打印斐波那契列前n列'''
    a,b=1,2
    flag=1
    while flag<=n:
        print(a,end=' ')
        a,b=b,a+b
        flag+=1
fid(10)


#--------------------------------------------------------5.3
def printHello():
    print('Hello Python')
for i in range(1,4,1):
    printHello()


#--------------------------------------------------------5.4
mark=eval(input("请输入学生成绩:"))
def grade(mark):
    if mark>=90:
        return "优秀"
    elif mark>=80:
        return "良好"
    elif mark>=70:
        return "中等"
    elif mark>=60:
        return "及格"
    else:
        return "不及格"
print(grade(mark))