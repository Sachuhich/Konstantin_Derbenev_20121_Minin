num=int(input())
if len(str(num))==2:print('Кол-во десятков: ',int(str(num)[0]),'\n','Кол-во единиц: ',int(str(num)[1]),sep=(''))
else:print('Кол-во десятков: ',int(str(num)[1]),'\n','Кол-во единиц: ',int(str(num)[2]),sep=(''))
