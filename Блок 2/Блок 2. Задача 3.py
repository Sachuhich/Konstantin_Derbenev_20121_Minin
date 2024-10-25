# Считывает 3 числа и подсчит кол-во чёт цифр

num1,num2,num3,d,c=int(input()),int(input()),int(input()),['0','2','4','6','8'],0
num0=str(num1)+str(num2)+str(num3)
for i in range(len(num0)):
    if num0[i]in d:c+=1
print(c)