a,long,cur,s=[],'','',input('')
s1,s2,s3=[],[],[]
for i in s:
  if i=='(' or i=='{' or i=='[':
    if i=='(':s1.append(i)
    elif i=='{':s2.append(i)
    else:s3.append(i)
    a.append(i)
    cur+=i
  elif i==')' and s1 and s1[-1]=='('and a:
    a.pop()
    s1.pop()
    cur+=i
    if len(cur)>len(long):long=cur
  elif i=='}' and s2 and s2[-1]=='{'and a:
    a.pop()
    s2.pop()
    cur+=i
    if len(cur)>len(long):long=cur
  elif i==']' and s3 and s3[-1]=='['and a:
    a.pop()
    s3.pop()
    cur+=i
    if len(cur)>len(long):long=cur
  else:
    cur=''
    if a:a.pop()
  if i==s[0] and i==')' or i=='}' or i==']':
    a.append(')')

if len(long)%2!=0:long=long[1::]
if len(long)==len(s):a=[]
if a:
  if long:print(long)
  else:print(False)
else:
  if long:print(True)
  else:print(False)
