import os,shutil

os.chdir('C:\\Users\\baozipu\\Desktop\\test')
files = os.listdir('./')
i=0
for file in files:
    if '.' not in file:
        old_name = 'C:\\Users\\baozipu\\Desktop\\test'+ os.sep + files[i]
        new_name = 'C:\\Users\\baozipu\\Desktop\\test' + os.sep + str(i+1) 
        shutil.move(old_name,new_name)     
    else:       
        old_name_split = files[i].split('.')[1]
        old_name = 'C:\\Users\\baozipu\\Desktop\\test'+ os.sep + files[i]
        new_name = 'C:\\Users\\baozipu\\Desktop\\test' + os.sep + str(i+1) + '.'+old_name_split
        shutil.move(old_name,new_name)
    i+=1





