import re

#r：表示字符串将被视为原始字符串，这意味着将忽略所有转义代码
#'\n'将被视为换行字符，而r'\n'将被视为字符\，后跟n。

#查找出字符串里所有的电话号码
""" text = 'My phone number is 245-233-5678.And the phone number of my office is 146-555-8888'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
text_group = []
for i in range(len(text)):    
    text_chunk = text[i:i+12]
    mo = phoneNumRegex.search(text_chunk)
    if mo != None:    
        text_group.append(mo.group())
for item in range(len(text_group)):
    print('能取到的第'+str(item+1)+'个电话号码为：'+text_group[item]) """


 #找出字符串中的电话号码
""" text = 'My phone number is 245-233-5678.'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search(text)
print(mo.group())  """


#找出括号分组内容
""" text = 'My phone number is 245-233-5678.'
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search(text)
#参数写0或者不写，会将匹配结果全显示出来
print(mo.group(0))
#参数写1，会匹配第一个括号内的内容
print(mo.group(1))
#参数写2，会匹配第二个括号内的内容
print(mo.group(2))
#以此类推 """

#括号转义，因为括号在正则表达式当中有特殊含义，为了匹配括号，需要用转义符来进行转义
""" text = 'My phone number is (245)-233-5678.'
phoneNumRegex = re.compile(r'(\(\d{3}\))-(\d{3}-\d{4})')
mo = phoneNumRegex.search(text)
print(mo.group(1))
#显示为(245) """

#管道|，匹配许多表达式中的一个时使用，先匹配到哪个就显示哪个
# 注意管道符左右不要有空格
""" heroRegex = re.compile(r'Tom|Lily')
text1 = 'Lily and Tom'
mo1 = heroRegex.search(text1)
print(mo1.group())
#结果是Lily
text2 = 'Tom and Lily'
mo2 = heroRegex.search(text2)
print(mo2.group())
#结果是Tom """

""" batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
#结果为Batmobile
print(mo.group(1))
#结果为mobile """

#?表示它前面的分组匹配零次或一次
""" batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#结果为Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#结果为Batwoman """

#*表示它前面的分组匹配零次或多次
""" batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#结果为Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#结果为Batwoman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
#结果为Batwowowowoman
mo4 = batRegex.search('The Adventures of Batwowowman')
print(mo4.group())
#报错，因为没有匹配的分组 """


#+表示它前面的分组匹配一次或多次
""" batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#报错，因为wo必须至少出现一次
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#结果为Batwoman
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
#结果为Batwowowowoman """



#用花括号匹配特定次数
#(Ha){3}:匹配HaHaHa
#(Ha){3,5}：匹配HaHaHa   HaHaHaHa   HaHaHaHaHa
#(Ha){3,}：匹配3次或更多次
#(Ha){,5}：匹配0次到5次
""" haRegex1 = re.compile(r'(Ha){3}')
mo1 = haRegex1.search('HaHaHa')
print(mo1.group())
#结果为HaHaHa
mo2 = haRegex1.search('Ha')
print(mo2.group())
#报错，结果为None """

""" haRegex2 = re.compile(r'(Ha){3,5}')
mo3 = haRegex2.search('HaHaHa river HaHaHaHa flower HaHa')
print(mo3.group())
#结果为HaHaHa
#可以匹配3次到5次，先匹配到多少次的就会显示多少次的 """

#贪心匹配
""" haRegex3 = re.compile(r'(Ha){3,5}')
mo4 = haRegex3.search('HaHaHaHaHa')
print(mo4.group())
#结果为HaHaHaHaHa """

#非贪心匹配
""" haRegex4 = re.compile(r'(Ha){3,5}?')
mo5 = haRegex4.search('HaHaHaHaHa')
print(mo5.group())
#结果为HaHaHa """

#findall ：返回被查找字符串中的所有匹配

#调用在一个没有分组的正则表达式上
""" text = 'My phone number is 245-233-5678.And the phone number of my office is 146-555-8888'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall(text)
print(mo)
#结果为：['245-233-5678', '146-555-8888'] """

#调用在一个有分组的正则表达式上
""" text = 'My phone number is 245-233-5678.And the phone number of my office is 146-555-8888'
phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.findall(text)
print(mo)
#结果为：[('245', '233', '5678'), ('146', '555', '8888')] """


#\d ：0到9的任何数字
#\D ：除0到9的数字以外的任何字符
#\w ：任何字母，数字或下划线字符
#\W ：除字母，数字或下划线以外的任何字符
#\s ：空格，制表符或换行符
#\S ：除空格，制表符或换行符以外的任何字符

#例:
""" text = '1 little,2 dog 3,4  a,5cat,  6  *,  7 _'
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(text)
print(mo)
#结果为：['1 little', '2 dog', '7 _'] """


#[] 匹配方括号内的任意字符，[^XXXX]表示匹配方括号里以外字符
""" text = 'There\'s one apple here'
textRegex1 = re.compile(r'[a-z0-9]')
mo1 = textRegex1.findall(text)
print(mo1)
#结果为：['h', 'e', 'r', 'e', 's', 'o', 'n', 'e', 'a', 'p', 'p', 'l', 'e', 'h', 'e', 'r', 'e']
textRegex2 = re.compile(r'[^a-z0-9]')
mo2 = textRegex2.findall(text)
print(mo2)
#结果为：['T', "'", ' ', ' ', ' '] """


#在正则表达式开始处使用^，表明匹配必须发生在被查找文本开始处
""" beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1.group())
#结果为：Hello """

#在正则表达式的末尾加上$，表明该字符串必须以这个正则表达式的模式结束
""" endsWithNum = re.compile(r'\d\.$')
mo2 = endsWithNum.search('Your number is 42.')
print(mo2.group())
#结果为：2.
endsWithNum = re.compile(r'\d$')
mo2 = endsWithNum.search('Your number is 42')
print(mo2.group())
#结果为：2 """

#同时使用^和$，表明整个字符串必须完全匹配该模式
""" wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1334355553')
print(mo3.group())
#结果为：1334355553
wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('133abc5553')
print(mo3.group())
#结果为：None """

#句点. : 通配符，匹配除了换行之外的所有字符
#注意：句点字符只匹配一个字符
""" atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)
#结果为：['cat', 'hat', 'sat', 'lat', 'mat'] """

# .* ：贪心模式，表示任意文本(除换行符)
""" nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo = nameRegex.search('First Name:A1 Last Name:Sweigart')
print(mo.group(1))
print(mo.group(2))
#结果为：A1    Sweigart

greedyRegex = re.compile(r'<.*>')
mo1 = greedyRegex.search('<To serve man> for dinner.>')
print(mo1.group())
#结果为：<To serve man> for dinner.> """

# .*? : 非贪心模式，表示任意文本(除换行符)
""" greedyRegex1 = re.compile(r'<.*?>')
mo2 = greedyRegex1.search('<To serve man> for dinner.>')
print(mo2.group())
#结果为：<To serve man> """

#用.*匹配所有字符，传入re.DOTALL参数
""" noNewlineRegex = re.compile(r'.*')
mo1 = noNewlineRegex.search('My name is A.\nHow about you?')
print(mo1.group())
#结果为：My name is A.
noNewlineRegex2 = re.compile(r'.*',re.DOTALL)
mo2 = noNewlineRegex2.search('My name is A.\nHow about you?')
print(mo2.group())
#结果为：
#My name is A.
#How about you? """

#使正则表达式不区分大小写，传入re.I或者re.IGNORECASE参数
""" robocop = re.compile(r'robocop',re.I)
mo1 = robocop.search('Robocop is a good guy')
mo2 = robocop.search('ROBOCOP is here,where is roboCop?')
mo3 = robocop.search('Are you talking about robocop?')
print(mo1.group())
print(mo2.group())
print(mo3.group())
#三个结果分别为：
#Robocop
#ROBOCOP
#robocop """

#sub：替换字符串。第一个参数：用于取代发现的匹配；第二个参数：用正则表达式匹配的内容
""" #下面的r'Agent \w+'，中间的空格必须有
namesRegex = re.compile(r'Agent \w+')
mo1 = namesRegex.sub('Alice','Agent Bob gave the secret documents to Agent Lily.')
print(mo1)
#结果为：Alice gave the secret documents to Alice. """
#使用匹配的文本本身作为替换的一部分时↓
#sub()第一个参数中可以输入\1,\2,\3...表示替代输入分组1,2,3...的文本
""" #↓例子中传入r'\1****'作为sub()第一个参数，字符串中的\1将由分组1匹配的文本所替代，也就是正则表达式的(\w)分组
agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo2 = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo2)
#结果为：A**** told C**** that E**** knew B**** was a double agent. """


#忽略正则表达式字符串中的空白符和注释，传入re.VERBOSE参数
""" phoneRegex = re.compile(r'''(
(\d{3}|\(d{3}\))?                      #area code
(\s|-|\.)?                             #separator
(\s*(ext|x|ext.)\s*\d{2,5})?           # extension
)''',re.VERBOSE) """










