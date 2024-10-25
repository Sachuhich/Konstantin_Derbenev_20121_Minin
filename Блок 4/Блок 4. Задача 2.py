'''
Задание 2. С клавиатуры поступает строка.
  Необходимо вывести строку, где порядок слов в противоположном направлении.
  Первое слово с заглавной буквы, остальные с маленькой. МЕЖДУ словами только ОДИН пробел.
Input: “hello world”
Output: "Hello world"
Input: it was cool وو
Output: "Cool was it"
Input: "good"
Output: "Good"
'''

a=str(input()).lower()
a=a.split()
a.reverse()
a[0] = a[0][0].upper()
print(' '.join(a))
