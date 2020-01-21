import traceback
from commands.moduls import func

def complete_task(task, count_number = '', search_number = '', input_str = '', search_str = ''):
    
    try:   
        
        if task == 'task 1' and count_number != '':
            result = task_1(int(count_number))

        elif task == 'task 2' and count_number != '':
             result = task_2(int(count_number))

        elif task == 'task 3' and count_number != '':
             result = task_3(int(count_number))

        elif task == 'task 4' and count_number != '':
            result = task_4(int(count_number))
        
        elif task == 'task 5' and count_number != '' and search_number != '':
             result = task_5(int(count_number), int(search_number))
        
        elif task == 'task 6' and count_number != '':
             result = task_6(int(count_number))
        
        elif task == 'task 7' and input_str != '' and search_str != '':
            result = task_7(input_str, search_str)
        
        elif task == 'task 8' and input_str != '' and count_number != '':
            result = task_8(input_str, int(count_number))

        elif task == 'task 9' and input_str != '':
            result = task_9(input_str)

        else:
            result = f'error in {task}: could not find arguments'

    except Exception:
        result = f'error in {task}: {traceback.format_exc()}'

    return result    

def task_1(count_number):

    if type(count_number) == int:
        m_list = func.get_random_list(count_number)
        return func.list_to_string(m_list)  
    else:
        return 'error: count number is not integer type'

def task_2(count_number):

    if type(count_number) == int:
        m_list = func.get_random_list(count_number)
        return f'{func.list_to_string(m_list)}\nmin: {func.get_min_number(m_list)} max: {func.get_max_number(m_list)}'   
    else:
        return 'error: count number is not integer type'        

def task_3(count_number):
    
    if type(count_number) == int:
        m_list = func.get_random_list(count_number, count_number)
        return func.list_to_string(m_list)
    else:
        return 'error: count number is not integer type' 

def task_4(count_number):
    
    if type(count_number) == int:
        m_list = func.get_random_list(count_number, count_number)
        return f'{func.list_to_string(m_list)}\nmin: {func.get_min_number(m_list)} max: {func.get_max_number(m_list)}'
    else:
        return 'error: count number is not integer type'

def task_5(count_number, search_number):
    
    if type(count_number) == int and type(search_number) == int:
        m_list = func.get_random_list(count_number, count_number) 
        entry_count = func.get_entry_count(m_list, search_number) 
        return f'{func.list_to_string(m_list)}\nentry count : {str(entry_count)}'
    else:
        return 'error: wrong type in count_number, search_number'

def task_6(count_number):
    
    if type(count_number) == int:
        m_list = func.get_random_list(count_number) 
        sort_list = func.quicksort(m_list.tolist()) 
        return f'{func.list_to_string(m_list)}\n{func.list_to_string(sort_list)}'
    else:
        return 'error: wrong type in count_number, search_number'

def task_7(input_str, search_str):
     
    if type(input_str) == str and type(search_str) == str:
        entry_count = func.get_entry_coutn_of_str(input_str, search_str)
        return f'entry count : {str(entry_count)}'
    else:
        return 'error: wrong type in input_str, search_str'

def task_8(input_str, count_number):

    if type(input_str) == str and type(count_number) == int:
        output_list = func.get_cut_list(input_str, count_number)
        return func.list_to_string(output_list)
    else:
        return 'error: wrong type in input_str, count_number'

def task_9(input_str):

    if type(input_str) == str:
        symbol = func.get_common_symbol(input_str)
        return symbol
    else:
        return 'error: wrong type in input_str, count_number'

if __name__ == '__main__':
    pass
    #result = complete_task('task1', count_number=10)
    #result = complete_task('task2', count_number=10)
    #result = complete_task('task3', count_number=10)
    #result = complete_task('task4', count_number=10)
    #result = complete_task('task5', count_number=10, search_number=45)
    #result = complete_task('task6', input_str='aa bb cc dd ff dd gh aa ss dd sa', search_str='aa')
    #result = complete_task('task7', input_str='aaa bbb ccc dd ff gg hh jj kk ll rr ee eeww fds erwer', count_number=2)
    result = complete_task('task 8',input_str='Extremity direction existence as dashwoods do up')
    
    print(result)