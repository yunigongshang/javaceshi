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
            