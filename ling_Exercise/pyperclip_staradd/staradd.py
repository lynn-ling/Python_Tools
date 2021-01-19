
#可以将复制到剪贴板上的内容每一行前面加上*，即先复制想要复制的内容，然后执行该文件，再粘贴就是每行前面加*的效果

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*'+lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)