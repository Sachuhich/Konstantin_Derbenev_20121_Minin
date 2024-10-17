num=int(input())
if num>=0:
    mun=int(str(num)[::-1])
    print(mun)if mun<128 else print('no solution')
else:
    num=str(num)[1::]
    mun=int((num)[::-1])
    print('-',mun,sep='')if mun<129 else print('no solution')