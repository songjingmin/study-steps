for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j," ",end='')
    print(end='\n')   

# 打印[9 9乘法表] #




x=raw_input('Please input a number:\n')
try:
    x=int(x)
    print [i for i in range(1,x+1) if x%i==0]
except Exception,e:
    print e

# 输入一个正整数，输出这个正整数的所有因数 #