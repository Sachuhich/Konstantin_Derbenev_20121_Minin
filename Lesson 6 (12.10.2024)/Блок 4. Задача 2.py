a=str(input()).lower()
a=a.split()
a.reverse()
a[0] = a[0][0].upper() a[0][1:] 
print(' '.join(a))
