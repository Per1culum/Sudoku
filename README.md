# Sudoku 基于python实现的数独小游戏
简单的python小游戏，可作为大学本科python课程的课程设计  
环境：python 3.9+  
所需的包：pygame（tkinter 为标准库无需安装），详见 requirements.txt  

主体包括：游戏矩阵基于选择难度的随机生成，GUI绘制的游戏界面，游戏规则的判定逻辑，输入设备与图形用户界面的交互。  

## 已修复的问题
1. ~~选择难度后需要关闭选择界面，游戏界面才会出现~~ — 选择难度后窗口自动关闭
2. ~~偶发的键盘数字区输入没办法处理~~ — 支持主键盘和小键盘数字输入
3. ~~tkinter的界面冲突~~ — 修复 tkinter 阻塞问题
4. ~~大师难度极偶发的游戏无解状况~~ — 大师难度空格数从 64 调整为 55，降低无解概率
5. ~~鼠标点击底部信息栏导致数组越界崩溃~~ — 添加边界检查
6. ~~requirements.txt 内容错误~~ — 修正为正确的 pip 包格式

## 难度说明
| 难度 | 空格数 |
|------|--------|
| 简单 | 10 |
| 一般 | 25 |
| 困难 | 35 |
| 大师 | 55 |

## 运行方式
```bash
pip install -r requirements.txt
python SHUDU.py
```

---

A simple python game that can be used as a course design for undergraduate python courses  
Environment: python 3.9+  
Required packages: pygame (tkinter is part of the standard library), see requirements.txt  

The main body includes: the random generation of the game matrix based on the selected difficulty, the game interface drawn by the GUI, the decision logic of the game rules, and the interaction between the input device and the graphical user interface.  
