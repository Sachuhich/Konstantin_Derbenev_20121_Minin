# 3знач число по цифрам через ,

num=int(input())
if len(str(num))==3:print(str(num)[0],str(num)[1],str(num)[2],sep=(',')) # При условии, что число > 0
else:print('-'+str(num)[1],str(num)[2],str(num)[3],sep=(',')) # При условии, что число < 0
