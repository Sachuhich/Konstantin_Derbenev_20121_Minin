num=int(input())
mun=str(num)[int(len(str(num)))//2::1]
if len(str(num))%2==0:print('True')if int(str(num)[0:int(len(str(num)))//2])==int(mun[::-1]) else print('False')
else:print('True')if int(str(num)[0:int(len(str(num)))//2+1])==int(mun[::-1])else print('False')
