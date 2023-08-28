import pandas as pd
import json

# 读取Excel文件
file_path = '课表.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path, engine='openpyxl')
print(df.json())  # 输出DataFrame
json_data = df.to_json(orient='records')

print(json_data)  # 输出JSON字符串
# 将JSON对象转换为字符串
json_string = json.dumps(json_data, ensure_ascii=False)

# 输出JSON字符串
print(json_string)