# По координатам точки, не лежащим на осях координат определяет номер координатной четверти, в которой она находится

numX,numY=float(input()),float(input())
if str(numX)[-1]=='0':numX=int(numX)
if str(numY)[-1]=='0':numY=int(numY)
if numX>0 and numY>0:print('Точка с координатами (',numX,';',numY,') находится в Первой четверти',sep='')
elif numX<0 and numY>0:print('Точка с координатами (',numX,';',numY,') находится во Второй четверти',sep='')
elif numX<0 and numY<0:print('Точка с координатами (',numX,';',numY,') находится в Третьей четверти',sep='')
else:print('Точка с координатами (',numX,';',numY,') находится в Четвёртой четверти',sep='')