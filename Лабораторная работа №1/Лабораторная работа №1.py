def expression(nums,target_sum,cur_i=0,cur_expression="",cur_val=0):

    if cur_i==len(nums): # Базовый случай: если все числа обработаны
        if cur_val==target_sum: return cur_expression
        else: return None

    cur_num=nums[cur_i] # Текущее число

    result_plus=expression(nums,target_sum,cur_i+1,cur_expression+(f'+{cur_num}' if cur_i>0 else f'{cur_num}'), cur_val+cur_num) # Проверяем вариант с '+' перед текущим числом
    result_minus=expression(nums,target_sum,cur_i+1,cur_expression+(f'-{cur_num}' if cur_i>0 else f'{cur_num}'), cur_val-cur_num) # Проверяем вариант с '-' перед текущим числом

    # Если нашли решение с '+' или '-', возвращаем его
    if result_plus: return result_plus
    if result_minus: return result_minus

with open('input.txt','r') as file: data=list(map(int,file.read().strip().split())) # Чтение данных из файла

N=data[0] # Количество слагаемых+вычитаемых
nums=data[1:N+1] # Cлагаемые+вычитаемые
target_sum=data[N+1] # Итоговое значение

expression=expression(nums,target_sum) # Ищем выражение

with open('output.txt','w') as file: # Запись результата в файл
    if expression: file.write(f'{expression}={target_sum}')
    else: file.write('no solution')
