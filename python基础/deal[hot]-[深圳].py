#/usr/bind/python3
#coding = 'utf-8'
import os 
list_name = os.listdir()
for name in list_name:
    index = name.rfind('.')
    newName = name[:index] + '[hot]-[深圳]' + name[index:]
    os.rename(name, newName)
