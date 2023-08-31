#--------------------------------------------------------7.2
fa=open("text.txt","rt",encoding='utf8')
print(fa.readline())
fa.close()


#--------------------------------------------------------7.3
fa=open("text.txt","wb")
print("Name of the file:",fa.name)
print("Closed or not:",fa.closed)
print("Opening mode:",fa.mode)
fa.close()


#--------------------------------------------------------7.4
fa=open("write.txt","w",encoding='utf8')
fa.write('Python is a baby.\nPython 是一门简洁的语言。')
fa.close()


#--------------------------------------------------------7.5
fa=open("write.txt",'r+',encoding='utf8')
print("Reasd String is:",fa.read(16))
fa.close()


#--------------------------------------------------------7.6
fa=open("write.txt",'r+',encoding='utf8')
print("Reasd String is:",fa.read(16))
position=fa.tell()
print("Current fiule position:",position)
position=fa.seek(0,0)
print("Again read String is:",fa.read(16))
fa.close()


#--------------------------------------------------------7.7
import os
os.rename("write.txt","writel.txt")


#--------------------------------------------------------7.8
import os
os.mkdir("test/home")


import os
#--------------------------------------------------------7.9
import os
os.chdir("test/home")


#--------------------------------------------------------7.10
import os
os.rmdir("test/home")


#--------------------------------------------------------7.11
try:
    fh =open("write", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
    
    
#--------------------------------------------------------7.12
assert 3==6
assert len([a,b,c,d])>5


#--------------------------------------------------------7.13
s_age=input("请输入你的年龄")
age=int(s_age)
assert 19<age<45
print("您输入的age在19和45之间")


