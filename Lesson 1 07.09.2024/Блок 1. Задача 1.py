# число десятков и единиц в 2значном числе

def main():
  num=int(input())
  if len(str(num))==2:print('Кол-во десятков: ',int(str(num)[0]),'\n','Кол-во единиц: ',int(str(num)[1]),sep=(''))
  else:print('Кол-во десятков: ',int(str(num)[1]),'\n','Кол-во единиц: ',int(str(num)[2]),sep=(''))
if __name__ == '__main__':
    main()
