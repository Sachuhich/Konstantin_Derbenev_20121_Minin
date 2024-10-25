a = str(input())
used,s,lst,end= '','',[],''
for i in range(len(a)):
  if a[i] not in used:
      used+=a[i]
      s+=a[i]
  else:
      lst.append([s, len(s)])
      s,used=a[i],a[i]
if len(lst)>1:
  for i in range(len(lst)-1):
    if lst[i][1]>lst[i+1][1]:
      end=lst[i][0]
    else:
      end=lst[i+1][0]
  print(end)
else:print(lst[0][0])