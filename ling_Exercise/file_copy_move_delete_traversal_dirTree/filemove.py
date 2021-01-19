import shutil

#移动
#shutil.move 将文件从源文件夹移动到目的文件夹
#1. 将对应路径里的1.txt文件移动到对应路径下
shutil.move('C:\\Users\\baozipu\\Desktop\\python\\1.txt','C:\\Users\\baozipu\\Desktop\\egg')

#2. 将对应路径里的1.txt文件移动到对应路径下，并将文件名改为2.txt
shutil.move('C:\\Users\\baozipu\\Desktop\\python\\1.txt','C:\\Users\\baozipu\\Desktop\\egg\\2.txt')

#3. 将对应路径里的1.txt文件移动到一个不存在的文件夹里，这时文件1.txt被移动到C:\\Users\\baozipu\\Desktop路径下，文件名为egg，并且没有后缀名
shutil.move('C:\\Users\\baozipu\\Desktop\\python\\1.txt','C:\\Users\\baozipu\\Desktop\\egg') 

#4. 因为没有egg这个文件夹，因此↓会报错，无法执行
shutil.move('C:\\Users\\baozipu\\Desktop\\python\\1.txt','C:\\Users\\baozipu\\Desktop\\egg\\2.txt')