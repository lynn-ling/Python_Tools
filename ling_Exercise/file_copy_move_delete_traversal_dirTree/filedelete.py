import shutil,os

#删除
#1. 删除相应路径下的文件file1.txt
os.unlink('C:\\Users\\baozipu\\Desktop\\folder1\\file1.txt')

#2. 删除一个空的文件夹
os.rmdir('C:\\Users\\baozipu\\Desktop\\folder3')

#3. 删除路径下的所有文件和文件夹(包括父文件夹folder2)，永久删除
shutil.rmtree('C:\\Users\\baozipu\\Desktop\\folder2')

#4. 例子  切换到路径下，将路径文件夹中以.xlsx结尾的文件都删除
#为了防止因写错后缀名而误删掉不想删掉的文件，可以先将 os.unlink(filename) 先注释掉，先打印出要打印的文件的名称
#然后再删掉print代码，执行删除代码
os.chdir('C:\\Users\\baozipu\\Desktop\\folder1')
for filename in os.listdir():
    if filename.endswith('.xlsx'):
        os.unlink(filename)
        print(filename)

#5. 用send2trash模块安全删除，删除数据可以从垃圾箱恢复
import send2trash
send2trash.send2trash('C:\\Users\\baozipu\\Desktop\\folder1\\file2.txt')