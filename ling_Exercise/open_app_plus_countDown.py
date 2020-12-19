import time,subprocess,os
import xlwings

#倒计时，timeLeft单位为秒
timeLeft = 5
while timeLeft > 0:
    print(timeLeft,'\t',end="")
    time.sleep(1)
    timeLeft = timeLeft-1
#倒计时到时间了以后执行文件或程序

#打开应用程序的时候不能在debug环境下执行，需要在命令行模式下执行
#在.py文件上右键→Open In Intergrated Terminal。在Terminal中打python <文件名>

####用subprocess.Popen：###
#打开网页（start必须有，shell=True必须有）
subprocess.Popen(['start','http://www.baidu.com'],shell=True)
#打开音乐格式文件（当文件在在执行目录中时，start必须有，shell=True必须有）
subprocess.Popen(['start','录音.mp3'],shell=True)
#打开音乐格式文件（当文件为绝对路径时，绝对路径前后要加上<r''>，shell=True必须有）
subprocess.Popen(r'"C://Users//baozipu//Documents//录音//录音 (2).m4a"',shell=True)
#打开应用程序（有的路径前后需要加上r''，有的不需要，试试看哪个好用用哪个）
subprocess.Popen("C://Program Files (x86)//Tencent//QQ//Bin//QQScLauncher.exe")
subprocess.Popen(r'"C://Program Files (x86)//Netease//CloudMusic//cloudmusic.exe"')
subprocess.Popen("C://Program Files (x86)//Tencent//WeChat//WeChat.exe")

###用xlwings.Book
#打开excel文件（当文件在在执行目录中时）
xlwings.Book("sum.xlsx")
#打开excel文件（当文件为绝对路径时）
xlwings.Book("C://Users//baozipu//Desktop//sum.xlsx")


####用os.system：####
#打开excel文件（当文件在在执行目录中时）
os.system("start sum.xlsx")
#打开excel文件（当文件为绝对路径时）
os.system("C://Users//baozipu//Desktop//sum.xlsx")
#打开txt文件
os.chdir("C://Users//baozipu//Desktop//")
os.system("notepad.exe 消息.txt")
#打开exe文件（方法1）
os.startfile('C://Program Files (x86)//Tencent//QQ//Bin//QQScLauncher.exe')
#打开exe文件（方法2）
os.chdir("C://Program Files (x86)//Tencent//QQ//Bin//")
os.system("QQScLauncher.exe")


