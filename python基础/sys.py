# import sys

# def A(num):
#     print(num)

# def B(num):
#     print(num)
#     A(100)

# print(sys.argv)

# a = [(x,y) for x in range(10) if x%2 == 0 for y in range(0,10) if y%2 !=0]

def myReplace(pstr, oldstr, newstr):
    while True:
        position = pstr.find(oldstr)
        if position == -1:
          break
        pstr = pstr[:position] + newstr + pstr[position + len(oldstr):]
    return pstr


a = 'hellow world world'
print(myReplace(a, 'world', 'william'))