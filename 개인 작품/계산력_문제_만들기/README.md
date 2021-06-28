## Version Alpha
```python
from tkinter.constants import BOTTOM, DISABLED, LEFT, RIGHT, TOP
import pandas as p
import random as ra
import tkinter as t

window = t.Tk()
window.title("계산력 강화")
window.geometry("640x400+100+100")
window.resizable(False, False)

num1_list = []
num2_list = []
question_list = []
ans_list = []

k, n1, n2 = 0, 0, 0
num = []
check_value_1 = t.IntVar()
check_value_2 = t.IntVar()
check_value_3 = t.IntVar()
check_value_4 = t.IntVar()

One_check = t.Checkbutton(window, text = '덧셈', variable = check_value_1)
One_check.pack(side = LEFT, padx = 15)
Two_check = t.Checkbutton(window, text = '뺄셈', variable = check_value_2)
Two_check.pack(side = LEFT, padx = 15)
Three_check = t.Checkbutton(window, text = '나눗셈', variable = check_value_3)
Three_check.pack(side = LEFT, padx = 15)
Four_check = t.Checkbutton(window, text = '곱셈', variable = check_value_4)
Four_check.pack(side = LEFT, padx = 15)

label_name = t.Label(window, text = '학생 이름')
label_name.pack(side = TOP, pady = 10)
name_Entry = t.Entry(window)
name_Entry.pack(side = TOP, pady = 10)

label_k = t.Label(window, text = '만들 문제 수')
label_k.pack(side = TOP, pady = 10)
k_Entry = t.Entry(window)
k_Entry.pack(side = TOP, pady = 10)

label_n1 = t.Label(window, text = '최소 자리 수')
label_n1.pack(side = TOP, pady = 10)
n1_Entry = t.Entry(window)
n1_Entry.pack(side = TOP, pady = 10)

label_n2 = t.Label(window, text = '최대 자리 수')
label_n2.pack(side = TOP, pady = 10)
n2_Entry = t.Entry(window)
n2_Entry.pack(side = TOP, pady = 10)

def get_nums():
    sign_list = []
    sign_list2 = []
    num = [int(check_value_1.get()), int(check_value_2.get()), int(check_value_3.get()), int(check_value_4.get())]
    k = int(str(k_Entry.get()))
    n1 = int(str(n1_Entry.get()))
    n2 = int(str(n2_Entry.get()))
    i = 1

    print(num)

    for i in range(0, 4):
        if num[i] == 1:
            if i == 0:
                sign_list.append('+')
                pass
            elif i == 1:
                sign_list.append('-')
                pass
            elif i == 2:
                sign_list.append('÷')
                pass
            elif i == 3:
                sign_list.append('x')
                pass

    while i < k+1:
        a_list = list(range(-1*10**n2+1, -1*10**(n1-1)+1)) + list(range(10**(n1-1), 10**n2))
        a = ra.choice(a_list)
        b = ra.choice(a_list)
        c = ra.choice(a_list)
        d = ra.choice(a_list)
        e = ra.choice(a_list)

        ra.shuffle(sign_list)

        if sum(num) == 1:
            question_list.append('(' + str(a) + ')' + ' ' + sign_list[0] + ' ' + '(' + str(b) + ')')
        elif sum(num) == 2:
            question_list.append('(' + str(a) + ')' + ' ' + sign_list[0] + ' ' + '(' + str(b) + ')' + ' ' + sign_list[1] + ' ' + '(' + str(c) + ')')
        elif sum(num) == 3:
            question_list.append('(' + str(a) + ')' + ' ' + sign_list[0] + ' ' + '(' + str(b) + ')' + ' ' + sign_list[1] + ' ' + '(' + str(c) + ')' + ' ' + sign_list[2] + ' ' + '(' + str(d) + ')')
        elif sum(num) == 4:
            question_list.append('(' + str(a) + ')' + ' ' + sign_list[0] + ' ' + '(' + str(b) + ')' + ' ' + sign_list[1] + ' ' + '(' + str(c) + ')' + ' ' + sign_list[2] + ' ' + '(' + str(d) + ')' + ' ' + sign_list[3] + ' ' + '(' + str(e) + ')')


        for length in range(len(sign_list)):
                if sign_list[length] == '÷':
                    sign_list2.append('/')
                elif sign_list[length] == 'x':
                    sign_list2.append('*')
                else:
                    sign_list2.append(sign_list[length])

        if sum(num) == 1:
            ans_list.append(round((eval(str(a) + sign_list2[0] + str(b))), 2))
            i += 1
        elif sum(num) == 2:
            ans_list.append(round((eval(str(a) + sign_list2[0] + str(b) + sign_list2[1] + str(c))), 2))
            i += 1
        elif sum(num) == 3:
            ans_list.append(round((eval(str(a) + sign_list2[0] + str(b) + sign_list2[1] + str(c) + sign_list2[2] + str(d))), 2))
            i += 1
        elif sum(num) == 4:
            ans_list.append(round((eval(str(a) + sign_list2[0] + str(b) + sign_list2[1] + str(c) + sign_list2[2] + str(d) + sign_list2[3] + str(e))), 2))
            i += 1
        
    question = {'문제' : question_list}
    ans = {'답' : ans_list}

    question = p.DataFrame(question)
    ans = p.DataFrame(ans)

    question.to_excel(excel_writer=f'[파일 경로]\\계산력문제지_{str(name_Entry.get())}.xlsx')
    ans.to_excel(excel_writer=f'[파일 경로]\\계산력문제_답지_{str(name_Entry.get())}.xlsx')
    sign_list.clear()

make_btn = t.Button(window, text = '만들기', command = get_nums)
make_btn.place(x = 300, y = 350)

window.mainloop()
```

## Version Beta
```python
from tkinter.constants import BOTTOM, DISABLED, LEFT, RIGHT, TOP
import pandas as p
import random as ra
import fractions as f
import tkinter as t

window = t.Tk()
window.title("계산력 강화")
window.geometry("640x400+100+100")
window.resizable(False, False)

num1_list = []
num2_list = []
question_list = []
ans_list = []

num, k, n1, n2 = 0, 0, 0, 0
r = t.IntVar()

One_radio = t.Radiobutton(window, text = '덧셈', variable = r, value = 1)
One_radio.pack(side = LEFT, padx = 15)
Two_radio = t.Radiobutton(window, text = '뺄셈', variable = r, value = 2)
Two_radio.pack(side = LEFT, padx = 15)
Three_radio = t.Radiobutton(window, text = '나눗셈', variable = r, value = 3)
Three_radio.pack(side = LEFT, padx = 15)
Four_radio = t.Radiobutton(window, text = '곱셈', variable = r, value = 4)
Four_radio.pack(side = LEFT, padx = 15)

label_name = t.Label(window, text = '학생 이름')
label_name.pack(side = TOP, pady = 10)
name_Entry = t.Entry(window)
name_Entry.pack(side = TOP, pady = 10)

label_k = t.Label(window, text = '만들 문제 수')
label_k.pack(side = TOP, pady = 10)
k_Entry = t.Entry(window)
k_Entry.pack(side = TOP, pady = 10)

label_n1 = t.Label(window, text = '최소 자리 수')
label_n1.pack(side = TOP, pady = 10)
n1_Entry = t.Entry(window)
n1_Entry.pack(side = TOP, pady = 10)

label_n2 = t.Label(window, text = '최대 자리 수')
label_n2.pack(side = TOP, pady = 10)
n2_Entry = t.Entry(window)
n2_Entry.pack(side = TOP, pady = 10)

def get_nums():
    num = r.get()
    k = int(str(k_Entry.get()))
    n1 = int(str(n1_Entry.get()))
    n2 = int(str(n2_Entry.get()))
    i = 1

    while i < k+1:
        a = ra.randint(10**(n1-1), 10**n2-1)
        b = ra.randint(10**(n1-1), 10**n2-1)
        if a not in num1_list and b not in num2_list:
            if num == 1:
                num1_list.append(a)
                num2_list.append(b)
                ans_list.append(a+b)
                question_list.append(str(a)+' '+'+'+' '+str(b)+' '+'=')
                i += 1
            elif num == 2:
                num1_list.append(a)
                num2_list.append(b)
                ans_list.append(a-b)
                question_list.append(str(a)+' '+'-'+' '+str(b)+' '+'=')
                i += 1
            elif num == 3:
                num1_list.append(a)
                num2_list.append(b)
                question_list.append(str(a)+' '+'÷'+' '+str(b)+' '+'=')
                if type(a/b) != int:
                    ans_list.append(f.Fraction(a, b))
                else:
                    ans_list.append(a/b)
                i += 1
            elif num == 4:
                num1_list.append(a)
                num2_list.append(b)
                ans_list.append(a*b)
                question_list.append(str(a)+' '+'x'+' '+str(b)+' '+'=')
                i += 1

    question = {'문제' : question_list}
    ans = {'답' : ans_list}

    question = p.DataFrame(question)
    ans = p.DataFrame(ans)

    question.to_excel(excel_writer=f'[파일 경로]\\계산력문제지_{str(name_Entry.get())}.xlsx')
    ans.to_excel(excel_writer=f'[파일 경로]\\계산력문제_답지_{str(name_Entry.get())}.xlsx')

make_btn = t.Button(window, text = '만들기', command = get_nums)
make_btn.place(x = 300, y = 350)

window.mainloop()

```

## Version 1.3
```python
import pandas as p
import random as r
import fractions as f
import tkinter as t

window = t.Tk()
window.title("계산력 강화")
window.geometry("640x400+100+100")
window.resizable(False, False)

num1_list = []
num2_list = []
question_list = []
ans_list = []

sign = ''
i = 1
k, n1, n2 = 0, 0, 0

# num = int(input('1. 덧셈\n2. 뺄셈\n3. 나눗셈\n4. 곱셈\n\n'))

label_k = t.Label(window, text = '만들 문제 수')
label_k.pack()
k_Entry = t.Entry(window)
k_Entry.pack()

label_n1 = t.Label(window, text = '최소 자리 수')
label_n1.pack()
n1_Entry = t.Entry(window)
n1_Entry.pack()

label_n2 = t.Label(window, text = '최대 자리 수')
label_n2.pack()
n2_Entry = t.Entry(window)
n2_Entry.pack()

def get_nums():
    k = k_Entry.get()
    n1 = n1_Entry.get()
    n2 = n2_Entry.get()
    print(k, n1, n2)

make_btn = t.Button(window, text = '만들기', command = get_nums)
make_btn.pack()

window.mainloop()

# def making_Q():
#     if num == 1:
#         sign = '+'
#     elif num == 2:
#         sign = '-'
#     elif num == 3:
#         sign = '÷'
#     elif num == '4':
#         sign = 'x'

#     while i < k+1:
#         a = r.randint(10**(n1-1), 10**n2-1)
#         b = r.randint(10**(n1-1), 10**n2-1)
#         if a not in num1_list and b not in num2_list:
#             if num == 1:
#                 num1_list.append(a)
#                 num2_list.append(b)
#                 ans_list.append(a+b)
#                 question_list.append(str(a)+' '+'+'+' '+str(b)+' '+'=')
#                 i += 1
#             elif num == 2:
#                 num1_list.append(a)
#                 num2_list.append(b)
#                 ans_list.append(a-b)
#                 question_list.append(str(a)+' '+'-'+' '+str(b)+' '+'=')
#                 i += 1
#             elif num == 3:
#                 num1_list.append(a)
#                 num2_list.append(b)
#                 question_list.append(str(a)+' '+'÷'+' '+str(b)+' '+'=')
#                 if type(a/b) != int:
#                     ans_list.append(f.Fraction(a, b))
#                 else:
#                     ans_list.append(a/b)
#                 i += 1
#             elif num == 4:
#                 num1_list.append(a)
#                 num2_list.append(b)
#                 ans_list.append(a*b)
#                 question_list.append(str(a)+' '+'x'+' '+str(b)+' '+'=')
#                 i += 1

#     question = {'문제' : question_list}
#     ans = {'답' : ans_list}

#     question = p.DataFrame(question)
#     ans = p.DataFrame(ans)

#     question.to_excel(excel_writer='C:\\Users\\Blue\\Desktop\\계산력\\문제지.xlsx')
#     ans.to_excel(excel_writer='C:\\Users\\Blue\\Desktop\\계산력\\문제_답지.xlsx')
```

## Version 1.0

```python

import pandas as p
import random as r
import fractions as f

sign = ''
i = 1

num = int(input('1. 덧셈\n2. 뺄셈\n3. 나눗셈\n4. 곱셈\n\n'))
k = int(input('만들 문제 수: '))
n1, n2 = int(input('최소 자리 수: ')), int(input('최대 자리 수: '))


if num == 1:
    sign = '+'
elif num == 2:
    sign = '-'
elif num == 3:
    sign = '÷'
elif num == '4':
    sign = 'x'

num1_list = []
num2_list = []
question_list = []
ans_list = []

while i < k+1:
    a = r.randint(10**(n1-1), 10**n2-1)
    b = r.randint(10**(n1-1), 10**n2-1)
    if a not in num1_list and b not in num2_list:
        if num == 1:
            num1_list.append(a)
            num2_list.append(b)
            ans_list.append(a+b)
            question_list.append(str(a)+' '+'+'+' '+str(b)+' '+'=')
            i += 1
        elif num == 2:
            num1_list.append(a)
            num2_list.append(b)
            ans_list.append(a-b)
            question_list.append(str(a)+' '+'-'+' '+str(b)+' '+'=')
            i += 1
        elif num == 3:
            num1_list.append(a)
            num2_list.append(b)
            question_list.append(str(a)+' '+'÷'+' '+str(b)+' '+'=')
            if type(a/b) != int:
                ans_list.append(f.Fraction(a, b))
            else:
                ans_list.append(a/b)
            i += 1
        elif num == 4:
            num1_list.append(a)
            num2_list.append(b)
            ans_list.append(a*b)
            question_list.append(str(a)+' '+'x'+' '+str(b)+' '+'=')
            i += 1

question = {'문제' : question_list}
ans = {'답' : ans_list}

question = p.DataFrame(question)
ans = p.DataFrame(ans)

question.to_excel(excel_writer='C:\\Users\\Blue\\Desktop\\계산력\\문제지.xlsx')
ans.to_excel(excel_writer='C:\\Users\\Blue\\Desktop\\계산력\\문제_답지.xlsx')


```
