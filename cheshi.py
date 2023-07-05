import random
import turtle
import math 
import time
aaaaaaaaaaaaaaaaaaa
def sum():#求和   1
    sum=0
    for i in range(100):
        sum +=i+1
    print("1到100的求和结果是：",sum)

xuexishiyon
def jiu():#九九乘法表  2
    for i in range(1,10) :
        for j in range(1,i+1):
            print("{}*{}={}".format(i,j,i*j),end=' ')
        print()
        
xuexishiyon
def www():#九九乘法表  2
    for i in range(1,10) :
        for j in range(1,i+1):
            print("{}*{}={}".format(i,j,i*j),end=' ')
        print()

def jie():#阶乘    3
    sum=0;tmp=1
    for i in range(1,21):
        tmp*=i
        sum+=tmp
    print("阶乘的结果是：{}".format(sum))

def tr():#绘制三角形   4
    turtle.left(180-180/3)
    turtle.forward(150)
    turtle.left(180-180/3)
    turtle.forward(150)
    turtle.left(180-180/3)
    turtle.forward(150)

def yuan():#计算圆面积  5
    radius=eval(input("请输入半径:"))
    circumference=2*math.pi*radius
    area=math.pi*radius*radius
    print("圆的周长是:%.2f"% circumference)
    print("圆的面积是:%.2f"% area)


def rgb():#三原色   6
    color = input("请选择蓝色，黄色其中一种颜色")
    color1 = input("请选择红色，黄色其中的一种颜色")
    if color == '蓝色' and color1 == '红色':
        print('蓝色+红色=紫色')
    elif color == '蓝色' and color1 =='黄色':
        print('蓝色+黄色=绿色')
    elif color == '黄色' and color1 =='红色':
            print('蓝色+红色=橙色')
    elif color == '黄色' and color1 =='黄色':
        print('黄色')
    else:
        print('输入错误，请重新输入')
def prn():
    print("...........................")
    print("单号:DH16516551651")
    print("时间:2014-09-23 08:56:14")
    print("名称      数量  单价   金额 ")
    print("金士顿U盘  1   40.00  40.00")
    print("8G")
    print("胜创16GTF  1   50.00  50.00")
    print("卡")
    print("读卡器     1    8.00  8.00")
    print("网线2米    1    5.00  5.00")
    print("..........................")
    print("总数:4       总额:103.00")
    print("折后总额:103.00")
    print("实收:103.00  找零:0.00")
    print("收银:管理员")



    print("              谢谢你            ")
    print("你于2019年11月3日申请种植的梭梭树,")
    print("已被中国扶贫基金会认领,将种植到武威")
    print("地区。")
    print("             树苗编号           ")
    print("         NO.HFK20308960305      ")

def weidu():
    a=eval(input("输入摄氏温度"))
    print("绝对温标为{}".format(a+273.15))

def bmi():
    height=eval(input("输入你的身高(m)"))
    wig=eval(input("输入体重(kg)"))
    bmi=wig/(height*height)
    print("BMI值为{}".format(bmi))

#============================2023年6月30日=====================================

def caishu():  #猜数
    a=random.randint(0, 100)
    while True:
        b=eval(input("请输入数"))
        if b<a:
            print("很遗憾，你猜小了")
        if b>a:
            print("很遗憾，你猜大了")
        if b==a:
            print("恭喜，猜数成功")
            break


def jieshuqi():  #计算器
    first=float(input("请输入第一个数："))
    second=float(input("请输入第二个数："))
    operator=input("请选择运算符：+-*/：")
    if operator =='+':
        print(first+second)
    elif operator == '-':
        print(first-second)
    elif operator == '*':
        print(first*second)
    elif operator == '/':
        if second ==0:
            print("除数不能为0")
        else:
            print(first/second)


def chengji():    #学生评语
    score =input("请输入学生的成绩：")
    score =int(score)
    if score >=90:
        print("Very good")
    elif score >=80:
        print("Good")
    elif score >=60:
        print("Passed")
    else:
        print("Failed")


def daze(): #优惠折扣       
    money=input("请输入购买的款数：")
    money =int(money)
    if money >=2000:
        money =(1 -0.15)* money 
    elif money >=1000:
        money =(1-0.10)* money 
    elif money >=500:
        money =(1-0.075)* money 
    elif money >=250:
        money =(1 -0.05)* money
    print("实际付款数为：{:.1f}".format(money))


def zhengchu(): #判断能否被7整除        
    m= input("请输入一个数")
    m=int(m)
    if(m%7==0):
        print("YES")
    else:
        print("NO")


def sanjiao():  #求三角形面积       
    a,b,c=input("请输入三角形的三条边长:").split(" ")
    a,b,c=int(a),int(b),int(c)
    if(a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("面积为{0:.2f}".format(area))
    else:
        print("不能构成三角形")


def eryue():    #输出该年份二月的天数     
    year=int(input("请输入年份:"))
    day=28
    if(year%4==0 and year%100!=0) or year%400==0:
        day=29
    print("{0}年二月有{1}天".format(year,day))

#===============================================2023年7月3日==========================

def sev(): #逢7拍手
    a=0
    for i in range(1,100):
        if i%7==0 or i%10==7 or i//10==7:
            a=a+1
            print(i,end=' ')
    print("总共{}个数".format(a))

    
#-------------------------------------------------------4.11
n=1
while(n<=6):
    score=input("请输入一个学生的成绩:")
    score=float(score)
    if score>=60.0:
        print("passed")
    else:
        print("failed")
    n=n+1

     
#-------------------------------------------------------4.12
sign=1
t=1.0
n=1.0
pi=0.0
while (abs(t)>=1e-6):
    pi=pi+t
    n=n+2
    sign=-sign
    t=sign/n
pi=pi*4
print("pi=%10.6f "%pi)


#-------------------------------------------------------4.13
n=input("请输入一个大于三的整数:")
n=int(n)
flag=1
i=2
while (i<=n**0.5 and flag):
    if(n%i==0):
        flag=0
    else:
        i+=1
if flag:
    print("%d is prime numbie."%n)
else:
    print("%d is not prime numbie."%n)

    
    
#-------------------------------------------------------4.14    
n= int(input('请输入一个整数：'))
s=1
for i in range(1,n+1):
    s=s*i
print('{0}!={1}'.format(n,s))


#-------------------------------------------------------4.15
sum = 0
for i in range(1,101):
    sum+=i
print("1+2+3+...+100=",sum)
    
    
#-------------------------------------------------------4.16
x=eval(input('请输入第一个整数：'))
max=x
min=x
for i in range(2,6,1):
    x=eval(input('请输入下一个整数；'))
    if (x>max):
        max=x
    elif (x<min):
        min=x
print('最大值为；{},最小值为：{}'.format(max,min))


#--------------------------------------------------------4.17
a_tuple=('crazyit','fkit','Charlie')
for ele in a_tuple:
    print('当前元素是:',ele)
            


#==========================================================2023年7月5日=============

scale = 50
print("开始下载".center(scale,'='))
for i in range(scale+1):
    a ='*'*i
    b = '·'*(scale-i)
    c = (i/scale)*100
    print("\r{:^3.0f}%[{}{}]".format(c,a,b),end='')
    time.sleep(0.1)
print("\n"+"下载完成".center(scale,'='))


# ------------------------------------------------------------17
print('这是"单行字符串"')
print("这是'单行字符串'")
print("""这是'多行字符串'的第一行
这是'多行字符串'的第二行""")
print('''这是"多行字符串"的第一行
这是"多行字符串"的第二行''')

# ------------------------------------------------------------18
print("这是\n有一个换行")
print("这是\\有一个反斜杠")
print("既需要'单引号'又需要\"双引号\"")
print("这里\t有一个制表符")

# ------------------------------------------------------------19
a=15
if(a>10 and a<100) or \
(a<-10 and a>-100):
    print("BINGO")
# ------------------------------------------------------------20
"青青子衿，悠悠我心。"[-5]
s="青青子衿，悠悠我心。"
s[5]

# ------------------------------------------------------------21
"青青子衿，悠悠我心。"[2:4]
"青青子衿，悠悠我心。"[8:4]
"青青子衿，悠悠我心。"[:4]
"青青子衿，悠悠我心。"[5:]

# ------------------------------------------------------------22
"{}曰:学而时习之，不亦说乎。".format("孔子")


# ------------------------------------------------------------23
"{}曰:学而时习之，不亦{}。".format("孔子","说乎")


# ------------------------------------------------------------24
"{0}曰:学而时习之，不亦{1}。".format("孔子","说乎")


# ------------------------------------------------------------25
"《论语》是{}弟子所著。{}曰:学而时习之，不亦说乎。".format("孔子")
"《论语》是{0}弟子所著。{0}曰:学而时习之，不亦说乎。".format("孔子")

# ------------------------------------------------------------26
"{1}曰:{{学而时习之，不亦说乎{0}}}。".format("说乎","孔子")


# ------------------------------------------------------------26
s="等级考试"
"{:25}".format(s)
"{:1}".format(s)
"{:^25}".format(s)
"{:>25}".format(s)
"{:*^25}".format(s)
"{:+^25}".format(s)
"{:+^25}".format(s)
"{:^1}".format(s)

#--------------------------------------------------------3.28
s = '等级考试'
y = '-'
z = '-'
print("{0:{1}^25}".format(s,y))
print("{0:{1}^{2}}".format(s,y,25))
print("{0:{1}{3}{2}}".format(s,y,25,z))


#--------------------------------------------------------3.29
print("{:-^25}".format(1234567890))
print("{0:-^25}".format(1234567890))


#--------------------------------------------------------3.30
print("{:.2f}".format(12345.67890))
print("{:.>25.3f}".format(12345.67890))
print("{:.5}".format('全国计算机等级考试'))
print("{:.15}".format('全国计算机等级考试'))


#--------------------------------------------------------3.31
print("{:b}".format(425))
print("{:c}".format(425))
print("{:d}".format(425))
print("{:o}".format(425))
print("{:x}".format(425))
print("{:X}".format(425))

#--------------------------------------------------------3.32
print("{:e},{:E},{:f},{:%}".format(3.14,3.14,3.14,3.14))
print("{2e},{:2E},{:f},{:%}".format(3.14,3.14,3.14,3.14))


#--------------------------------------------------------3.33
print("{:.2f}".format(3.1415926))
print("{:x}".format(1010))
print("{:.5}".format('这是一个很长的字符串'))
print("{:-^10}".format('PYTHON'))

