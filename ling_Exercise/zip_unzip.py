import os,zipfile

#压缩文件及文件夹

#将delicious文件夹里的文件get_token.jmx压缩成名为new.zip的文件
os.chdir('C:\\Users\\baozipu\\Desktop\\delicious')
newZip = zipfile.ZipFile('new.zip','w')
newZip.write('get_token.jmx',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


#将文件夹里的所有文件夹及文件压缩成zip文件

def dfs_get_zip_file(input_path,result):
    #os.listdir：返回指定的文件夹包含的文件或文件夹的名字的列表
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'\\'+file):
            dfs_get_zip_file(input_path+'\\'+file,result)
        else:
            result.append(input_path+'\\'+file)

def zip_path(input_path,output_path,output_name):
    os.chdir('C:\\Users\\baozipu\\Desktop')
    f = zipfile.ZipFile(output_path+'\\'+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file)
    f.close()
    

zip_path("delicious",'C:\\Users\\baozipu\\Desktop','work.zip')


#查看压缩文件内容

os.chdir('C:\\Users\\baozipu\\Desktop\\')
zip_read = zipfile.ZipFile('newzip.zip')
print(zip_read.namelist())
#namelist()方法返回ZIP文件中包含的所有文件和文件夹的字符串的列表
info = zip_read.getinfo('delicious/cats/zophie.jpg')
#getinfo()方法返回一个关于特定文件的ZipInfo对象，有表示字节数的file_size(原来文件大小)和compress_size(压缩后文件大小)属性
print(info.file_size)

#解压

os.chdir('C:\\Users\\baozipu\\Desktop')
unzip_file = zipfile.ZipFile('newzip.zip')
#extractall：解压该文件夹里所有的文件和文件夹，extract：解压某个文件或文件夹
#如果括号里不写任何内容，那么会解压到当前目录下，即C:\\Users\\baozipu\\Desktop里
#如果传递给extractall()方法的文件夹不存在，它会被创建
unzip_file.extractall('C:\\Users\\baozipu\\Desktop\\delicious')
unzip_file.close()







