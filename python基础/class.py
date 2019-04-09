class Cat:
	a = '12'
	def __init__(self, **args):
		# print(type(args))
		
		for key,value in args.items():
			# self[key] = value
			self.key = value
			# print(type(key))
			print(key, '---', value)
		# self
		print('zaiiiiiiii', args)
	
	def __str__(self):
		return 'haha'
	def go(self,a):
		print(self)
		print('gooooooinnnnngggggg', '===', a)

	def stop(self):

		print('stop----')

mao = Cat(m=1,n=2)
mao.go('我就是走')
mao.stop()
print(mao.a)
