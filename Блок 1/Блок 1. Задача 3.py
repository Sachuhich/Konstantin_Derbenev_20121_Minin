# число при перестановке цифр в 2знач числе

num=int(input())
if len(str(num))==2:print('Число после перестановки цифр:',str(num)[1]+str(num)[0]) # При условии, что число > 0
else:print('Число после перестановки цифр:','-'+str(num)[2]+str(num)[1]) # При условии, что число < 0
