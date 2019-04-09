# coding:utf-8
#如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?

import time

start_time = time.time()
for a in range(0, 1001):
  for b in range(0, 1001):
    for c in range(0, 1001):
      if a+b+c==1000 and a**2+b**2==c**2:
        print("a=%db=%dc=%d"%(a,b,c))
end_time = time.time()
print("总用时%d"%(end_time-start_time))
