#！python3

Passwords = {'email':'123456','blog':'abcdef'}

#pyperclip模块有copy()和paste()函数，可以向计算机的剪贴板发送文本，或从它接收文本
import sys,pyperclip

#命令行参数将存储在变量sys.argv中，列表中的第一项总是一个字符，它包含程序的文件名
#第二项是第一个命令行参数

#当用户忘记填参数的时候
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

#将用户填的第一个参数值赋给account变量
account = sys.argv[1]

#如果用户填的第一个参数在Passwords里，那么就将键对应的值复制出来
if account in Passwords:
    pyperclip.copy(Passwords[account])
    print('password for '+account+'copied to clipboard.')
else:
    print('There is no account named'+account)



'''
pw.py文件放在什么位置都可以，双击即可执行，如果想在Win+R处输入文件名执行.py文件，需要写<文件名+.py>全名
如果想只写文件名就执行python文件，可以创建批处理bat文件(双击即可执行python文件)，并配置系统环境变量
将bat文件存放的绝对路径添加到系统环境变量的Path里，这样就可以找到bat文件并执行它了
注意：bat文件里写的python文件的位置也要写绝对路径，不然找不到文件或者报错或者无执行结果

这里在查找密码的时候只需要在Win+R处  pw email，就会弹出密码已复制的消息，直接粘到想要粘贴的位置即可
'''













