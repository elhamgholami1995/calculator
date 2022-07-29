import tkinter as tk
from tkinter import Frame, font
from tkinter import ttk

window = tk.Tk()


lbl_calc_result = tk.Label(
    master = window,
    text = '0',
    width= 20,
    height= 3,
    font = ('Arial', 14),
    fg = 'white',
    bd = '0',
    bg = '#595954',
    cursor= 'hand2',
    highlightbackground = 'black',
    highlightcolor = 'pink',
    
    )
lbl_calc_result.grid(row=0 , column=0 , columnspan= 4 , sticky= 'nsew')

last_op_index= -1
last_dot_index= -1
def insert_number_in_calc_result(btn_text):
    current = lbl_calc_result['text'] 

    global last_dot_index, last_op_index
    if btn_text in ['+', '-', '*']:
        last_op_index = len (current)
    
        
   
    if btn_text == 'c':
        lbl_calc_result['text'] = '0'
        last_dot_index, last_op_index = 0,0 
        
    elif current== '0' :
        lbl_calc_result['text'] = btn_text
    elif btn_text == '=':
        result = str(eval(current)) 
        lbl_calc_result['text'] = result
        last_op_index = 0
        if '.' in result:
            last_dot_index = len(result)
    else:
        if btn_text=='.' :
            if last_dot_index > last_op_index :
                pass
            elif  current[-1] == '.':
                pass
            else:
                lbl_calc_result['text'] += btn_text
                last_dot_index = len(current)
        elif btn_text in ['+', '-', '*']:
            if current[-1] in ['+', '-', '*']:
                lbl_calc_result['text']  =  current[:-1] + btn_text
            else:
                lbl_calc_result['text'] += btn_text
        else:
            lbl_calc_result['text'] += btn_text 




calc_keys = [
    {
        'text' : '/',
        'command' : lambda : insert_number_in_calc_result ('/'),
    },
    {
        'text' : '%',
        'command' : lambda : insert_number_in_calc_result ('%'),
    },
    {
        'text' : '(',
        'command' : lambda : insert_number_in_calc_result ('('),
    },
    {
        'text' : ')',
        'command' : lambda : insert_number_in_calc_result (')'),
    },
    {
        'text' : '7',
        'command' : lambda : insert_number_in_calc_result ('7'),
    },
    {
        'text' : '8',
        'command' : lambda : insert_number_in_calc_result ('8'),
    },
    {
        'text' : '9',
        'command' : lambda : insert_number_in_calc_result ('9'),
    },
    {
        'text' : '+',
        'command' : lambda : insert_number_in_calc_result ('+'),
    },
    {
        'text' : '4',
        'command' : lambda : insert_number_in_calc_result ('4'),
    },
    {
        'text' : '5',
        'command' : lambda : insert_number_in_calc_result ('5'),
    },
    {
        'text' : '6',
        'command' : lambda : insert_number_in_calc_result ('6'),
    },
    {
        'text' : '-',
        'command' : lambda : insert_number_in_calc_result ('-'),
    },
    {
        'text' : '1',
        'command' : lambda : insert_number_in_calc_result ('1'),
    },
    {
        'text' : '2',
        'command' : lambda : insert_number_in_calc_result ('2'),
    },
    {
        'text' : '3',
        'command' : lambda : insert_number_in_calc_result ('3'),
    },
    {
        'text' : '*',
        'command' : lambda : insert_number_in_calc_result ('*'),
    },
    {
        'text' : '.',
        'command' : lambda : insert_number_in_calc_result ('.'),
    },
    {
        'text' : '0',
        'command' : lambda : insert_number_in_calc_result ('0'),
    },
    {
        'text' : 'c',
        'command' : lambda : insert_number_in_calc_result ('c'),
    },
    {
        'text' : '=',
        'command' : lambda : insert_number_in_calc_result ('='),
    },

]


calc_keys_objs =[]




for calc_key_data in calc_keys :
    btn = tk.Button(
        master = window,
        text = calc_key_data['text'],
        command= calc_key_data['command'],
        height= 2,
        width= 5,
        font= ('Arial', 14),
        fg = 'white',
        bd = '0',
        cursor= 'hand2',
        bg ='#2E2E2B' ,
        highlightbackground = 'black',
        highlightcolor = 'pink',
        relief = 'groove' ,
        
    )
    calc_keys_objs.append(btn)

for i , calc_key_obj in enumerate(calc_keys_objs):
    calc_key_obj.grid(row =( i//4)+1 , column = i%4, sticky='nsew')

# 0, 1, 2, 3 --> //4 =0
# 4, 5, 6, 7--> //4 =1
# 8, 9, 10, 11--> //4=2
#12, 13, 14, 15-->//4=3

window.title ('calculator')


window.mainloop()
