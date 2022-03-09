#! /usr/bin/env python
# -*- coding: utf-8 -*-


#钱
t = [100, 50, 20, 5]

# t = [100, 50, 20, 5]
# m = [1,3,6,7] #意思就是100元找1张,50元找3张

#如果n是零找开了，n不是零没有找开 

def change(t, n):
	#m是张数
    m = [0 for _ in range(len(t))]
    #print(m) #[0, 0, 0, 0]
    for i, money in enumerate(t):
        #print(i) #0 1 2 3
        #print(money)
    	#i是当前的编号  举个例子 n是376 money是100
        m[i] = n // money  #商3
        #n还剩多少取余
        n = n % money  #取余76 76不够100的
        print(m)
        print(n)
    return m, n

print(change(t, 376))
