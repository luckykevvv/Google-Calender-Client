# 导入py2puml
import py2puml

# 导入sys
import sys

# 添加搜索路径
sys.path.append('C:\\Users\\lucky\\Documents\\学习\\计算机')

# 指定要分析的模块或包
domain = 'ia-programme.main'

# 调用py2puml函数，得到PlantUML脚本
plantuml_script = py2puml(domain)

# 打印或保存PlantUML脚本
print(plantuml_script)