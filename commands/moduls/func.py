import numpy as np
import random

def get_random_list(cols, rows = 0):
    if rows == 0:
        m_list = np.random.randint(0, 100, size=cols)
    else:
        m_list = np.random.randint(0, 100, size=(cols, rows))
    return m_list        

def list_to_string(m_list):  
    
    m_string = ''
    
    if type(m_list) == list or (hasattr(m_list, 'shape') and m_list.shape == (m_list.size, )):
        for number in m_list:
            m_string += str(number) + ' '
    else:
        for row in range(len(m_list)):
            for col in range(len(m_list)):
                    m_string += str(m_list[row][col]) + ' '        
            m_string += '\n'

    return m_string  

def get_max_number(m_list):
    m_max = 0
    if m_list.shape == (m_list.size, ): 
        for number in m_list:
            if number > m_max:
                m_max = number
    else:
        for row in range(len(m_list)):
            for col in range(len(m_list)):
                if m_list[row][col] > m_max:
                    m_max = m_list[row][col]       
    return m_max

def get_min_number(m_list):
    m_min = 100
    if m_list.shape == (m_list.size, ):
        for number in m_list:
            if number < m_min:
                m_min = number
    else:
        for row in range(len(m_list)):
            for col in range(len(m_list)):
                if m_list[row][col] < m_min:
                    m_min = m_list[row][col]     
    return m_min        

def get_entry_count(m_list, search_number):
    entry = 0
    for col in range(len(m_list)):
        for row in range(len(m_list)):
            if m_list[col][row] == search_number:
                entry += 1
    return entry

def get_entry_coutn_of_str(input_str, search_str):
    entry_coutn = 0
    end = False
    while not end:
        str_index = input_str.find(search_str)
        if str_index != -1:
            entry_coutn += 1
            input_str = input_str.replace(search_str, '', 1)
        else:
            end = True
    return entry_coutn         

def get_cut_list(input_str, count_number):
    m_list = input_str.split(' ')
    if count_number == 1:
        return_list = m_list
    else:            
        return_list = []
        for index in range(len(m_list)):
            if index != len(m_list):
                if (index + 1) % count_number != 0:
                    return_list.append(m_list[index]) 
    return return_list

def get_common_symbol(input_str):
    max = 0
    common_symbol = ''
    for index in range(len(input_str)):
        symbol = input_str[index].lower()
        symbol_count = len(input_str) - len(input_str.replace(symbol, '')) 
        if symbol_count > max:
            max = symbol_count + 1
            common_symbol = symbol
    
    return common_symbol    

def quicksort(m_list):
    if len(m_list) <= 1:
       return m_list
    else:
       q = random.choice(m_list)

    l_list = [n for n in m_list if n < q]
 
    e_list = [q] * m_list.count(q)
    h_list = [n for n in m_list if n > q]
    
    return quicksort(l_list) + e_list + quicksort(h_list)    



