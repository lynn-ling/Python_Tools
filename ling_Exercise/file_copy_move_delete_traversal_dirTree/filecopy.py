import shutil,os

#复制
#1. 将对应路径里的1.txt文件复制到对应路径下
os.chdir('C:\\Users\\baozipu\\Desktop\\python')
shutil.copy('1.txt','C:\\Users\\baozipu\\Desktop\\')

#2. 将对应路径里的1.txt文件复制到对应路径下，并将文件名改为2.txt
os.chdir('C:\\Users\\baozipu\\Desktop\\python')
shutil.copy('1.txt','C:\\Users\\baozipu\\Desktop\\2.txt')

#3. shutil.copytree创建了一个新文件夹名为python_backup，将python文件夹里的所有文件和文件夹(不包括python这个父文件夹)备份到python_backup中
#因为已经进入到C:\\Users\\baozipu\\Desktop\\路径中，因此C:\\Users\\baozipu\\Desktop\\python里的C:\\Users\\baozipu\\Desktop\\可以不用写
os.chdir('C:\\Users\\baozipu\\Desktop\\')
shutil.copytree('C:\\Users\\baozipu\\Desktop\\python','C:\\Users\\baozipu\\Desktop\\python_backup')













