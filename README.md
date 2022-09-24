# Sudoku 基于python实现的数独小游戏
简单的python小游戏，可作为大学本科python课程的课程设计
环境：python 3.9
所需的包：tkinter/pygame等，详见requirement.txt文件

主体包括：游戏矩阵基于选择难度的随机生成，GUI绘制的游戏界面，游戏规则的判定逻辑，输入设备与图形用户界面的交互。
存在一些粗糙的bug没有完善，例如
（1）选择难度后需要关闭选择界面，游戏界面才会出现
（2）偶发的键盘数字区输入没办法处理，需要使用字母区上面的数字才能输入
（3）tkinter的界面冲突
（4）选择大师难度后极偶发的游戏无解状况

A simple python game that can be used as a course design for undergraduate python courses
Environment: python 3.9
Required packages: tkinter/pygame, etc., see requirement.txt file for details

The main body includes: the random generation of the game matrix based on the selected difficulty, the game interface drawn by the GUI, the decision logic of the game rules, and the interaction between the input device and the graphical user interface.
There are some rough bugs that are not perfected, such as
(1) After selecting the difficulty, you need to close the selection interface, and the game interface will appear
(2) The occasional input in the numeric area of the keyboard cannot be handled, and you need to use the numbers on the alphabet area to enter
(3) tkinter interface conflict
(4) The very occasional game unsolvable situation after selecting the master difficulty
