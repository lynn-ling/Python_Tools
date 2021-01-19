import shelve,pyperclip,sys

#当用户想要保存一段剪贴板文本时，需要保存在一个shelf文件中。这里的shelf文件即为mcb
mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
if sys.argv[1].lower() == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

#一般剪贴板会用到以下三种语句：
#spam表示给要保存的剪贴板的内容的名字
#py multiple_clipboard.py save spam      将剪贴板的内容取名为spam并保存
#py multiple_clipboard.py spam           复制名为spam对应的剪贴板里的内容
#py multiple_clipboard.py list           列出剪贴板里的关键字都有什么
#如果有bat文件(名为multiple_clipboard.bat)，那么在Win+R执行的时候只需要   multiple_clipboard        save spam/spam/list即可