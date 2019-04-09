# # try:
# #     # num  = 10
# #     print(num)
# # except IOError as result:
# #     print(result)
# # else:
# #     print('这里没有错误')
# # finally:
# #     print('我就是要执行')
 
# class ShortInputException(Exception):
#     def __init__(self, length, atlast):
#         self.length = length
#         self.atlast = atlast
    
#     def __str__(self):
#         return '字符长度不符合'

# try:
#     a = input('请输入')
#     if len(a) < 3:
#         raise ShortInputException(len(a), 3)
# except ShortInputException as result:
#     print(result)

class Test(object):
    def __init__(self, switch):
        self.switch = switch #开关
    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下:")
                print(result)
            else:
                #重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理
                raise

a = Test(True)
a.calc(11,0)

print("----------------------华丽的分割线----------------")

a.switch = False
a.calc(11,0)