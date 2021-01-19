import os

#遍历目录树，将一个文件夹里所有的文件夹和文件都遍历一遍
#os.walk在循环的每次迭代中，返回3个值：当前文件夹名称的字符串，当前文件夹中子文件夹的列表，当前文件夹中文件的列表
#文件夹delicious，里面有↓
#1，文件夹cats，内部有文件catnames.txt，zophie.jpg
#2，文件夹walnut，内部有文件夹waffles(内部有文件夹butter.txt)
#3，文件spam.txt

for folderName,subfolders,filenames in os.walk('C:\\Users\\baozipu\\Desktop\\delicious'):
    print('The current folder is : '+folderName)

    for subfolder in subfolders:
        print('subfolder of '+folderName+' : '+subfolder)
    for filename in filenames:
        print('file inside '+folderName+' : '+filename)
    print('')