import pyperclip,re

#电话号码的正则表达式
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4})
(\s*(ext|x|ext\.)\s*(\d{2,5}))?
)''',re.VERBOSE)

#邮件的正则表达式
emailRegex = re.compile(r'''(
[a-zA-z0-9._%+-]+
@
[a-zA-z0-9._-]+
(\.[a-zA-Z]{2,4})    
)
''',re.VERBOSE)

#复制内容到剪贴板
text = pyperclip.paste()
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join((groups[1],groups[3],groups[5]))
    # join() 方法用于将序列中(元祖或列表)的元素以指定的字符连接生成一个新的字符串
    # 因此上面的代码也可以写作 phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x'+ groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addressed found.')