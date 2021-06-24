#### Version 1.0

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
