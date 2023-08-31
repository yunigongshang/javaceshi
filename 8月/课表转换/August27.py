
import openpyxl 
import re
import json
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Font, Color
from openpyxl.formatting import Rule
from openpyxl.utils import get_column_letter
#处理周次和课节的数据
def jiejc(a):
    pattern =r'\d+'
    find=re.findall(pattern,a)
    find_numbers=list(map(int,find))#str转为int
    if a[-1]=="周":
        c=[]
        if len(find_numbers)==1:
            return find_numbers
        else:
            for i in range(find_numbers[0],find_numbers[1]+1):
                c.append(i)
            return c
    else:
        b=[]
        for i in range(find_numbers[0],find_numbers[1]+1,2):
            b.append(f'{i}-{i+1}节')
        return b
    
with open('2022.json', 'r',encoding='utf-8') as file:
   res = json.load(file)
r=res["kbList"]

# 创建
# workbook = openpyxl.Workbook()
workbook=openpyxl.load_workbook('ke.xlsx')
worksheet = workbook.active

laoshi=[]
for i in range(len(r)):
    
    for k in jiejc(r[i]["zcd"]):
        a1=worksheet[1]
        for row in a1:
            if row.value == f'第{k}周':
                zcd=row.column_letter
        for j in jiejc(r[i]["jc"]):
            b=0
            for row in worksheet.iter_rows():
                for cell in row:
                    if cell.value == j:
                        b=b+1
                        if (b==int(r[i]["xqj"])):
                            xqj=cell.row
                            dan=f'{zcd}{xqj}'
                            data=f'课名：{r[i]["kcmc"]},老师：{r[i]["xm"]},地点：{r[i]["cdmc"]}'
                            laoshi.append(r[i]["xm"])
                            print(data)
                            cell = worksheet[dan]#选择单元格
                            cell.value = data  #进行写入
                            
#单元格规制写入
color=["FFFFCC","CCFFFF","FFCCCC","99CCCC","FFCC99","FFFF99","CCCCFF","FF6666","666666","003399"]
myList = list(set(laoshi))
for ad in range(len(myList)):
    red_text = Font(color="000000")
    red_fill = PatternFill(bgColor=color[ad])
    dxf = DifferentialStyle(fill=red_fill)
    rule = Rule(type="containsText", operator="containsText", text=myList[ad], dxf=dxf)
    rule.formula = [f'NOT(ISERROR(SEARCH("{myList[ad]}",A1)))']
    worksheet.conditional_formatting.add('A1:X40', rule)
#设置宽高
for i in range(2, worksheet.max_row+1):
    worksheet.row_dimensions[i].height = 50
for i in range(4, worksheet.max_column+1):
    worksheet.column_dimensions[get_column_letter(i)].width = 17
workbook.save('ke2.xlsx')
# 关闭Excel文件
workbook.close()
print("导出成功")
