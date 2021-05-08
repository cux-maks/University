#### Check_Today_Version 1.0
```python
from tkinter import *
from tkinter import ttk
from datetime import datetime
import time as t
import pandas as p
import os
import numpy
import os.path

date = datetime.today().strftime("%Y-%m-%d")
#print(date)

Names = []
passwd = 'admin'

name = ['', '', '', '', '', '', '']

time_1 = ['', '', '', '', '', '', '']
time_1_1 = numpy.arange(28).reshape(7, 4)
time_1_1_1 = [0, 0, 0, 0, 0, 0, 0]

time_2 = ['', '', '', '', '', '', '']
time_2_2 = numpy.arange(28).reshape(7, 4)
time_2_2_2 = [0, 0, 0, 0, 0, 0, 0]

work = ['', '', '', '', '', '', '']
work_1 = [0, 0, 0, 0, 0, 0, 0]

monthTime = [0, 0, 0, 0, 0, 0, 0]
monthTime_1 = ['', '', '', '', '', '', '']

temp_1 = [0, 0, 0, 0, 0, 0, 0]
temp_2 = [0, 0, 0, 0, 0, 0, 0]

window = Tk()

user_id, password, temp = StringVar(), StringVar(), StringVar()

num = 0
who = 0

def text_changer():
    lb_0.configure(text = "time checker", foreground = 'black')
    lb_0.place(x = 130, y = 10)

def check_data_1():

        for i in range(0, 6):
            if user_id.get() == Names[i]:
                num = i + 1
                break
            else:
                num = -1
        
        if num == -1 or password.get() != 'admin':
            lb_0.configure(text = "Who are you??")
            lb_0.place(x = 125, y = 10)

        if user_id.get() == Names[num-1] and password.get() == passwd and time_1[num] != '':
            if float(temp.get()) <= 37.5:  
                lb_0.configure(text = "check out {}˚".format(temp.get()), foreground = 'green')
                lb_0.place(x = 140, y = 10)
            else:
                lb_0.configure(text = "check out {}˚".format(temp.get()), foreground = 'red')
                lb_0.place(x = 140, y = 10)

            time_2[num] = datetime.today().strftime("%H:%M:%S")

            time_2_2[num][1] = int(datetime.today().strftime("%H"))
            time_2_2[num][2] = int(datetime.today().strftime("%M"))
            time_2_2[num][3] = int(datetime.today().strftime("%S"))

            time_2_2_2[num] = int(str(time_2_2[num][1])+str(time_2_2[num][2])+str(time_2_2[num][3]))

            temp_2[num] = temp.get()

            t1 = time_2_2[num][1] - time_1_1[num][1]
            t2 = time_2_2[num][2] - time_1_1[num][2]
            t3 = time_2_2[num][3] - time_1_1[num][3]

            if t2 < 0:
                t1 = t1 - 1
                t2 = t2 + 60

            if t3 < 0:
                t2 = t2 - 1
                t3 = t3 + 60

            work[num] = '{}:{}:{}'.format(str(t1).zfill(2), str(t2).zfill(2), str(t3).zfill(2))
            work_1[num] = int('{}{}{}'.format(str(t1).zfill(2), str(t2).zfill(2), str(t3).zfill(2)))

            #print(time_2)
            #print(work)

        if user_id.get() == Names[num-1] and password.get() == passwd and time_1[num] == '':

            if float(temp.get()) <= 37.0:  
                lb_0.configure(text = "check in {}˚".format(temp.get()), foreground = 'green')
                lb_0.place(x = 140, y = 10)
            elif float(temp.get()) >= 37.0 or float(temp.get()) <= 37.5:
                lb_0.configure(text = "check in {}˚".format(temp.get()), foreground = 'orange')
                lb_0.place(x = 140, y = 10)
            elif float(temp.get()) >= 37.5:
                lb_0.configure(text = "check in {}˚".format(temp.get()), foreground = 'red')
                lb_0.place(x = 140, y = 10)

            name[num] = user_id.get()
            time_1[num] = datetime.today().strftime("%H:%M:%S")

            time_1_1[num][1] = int(datetime.today().strftime("%H"))
            time_1_1[num][2] = int(datetime.today().strftime("%M"))
            time_1_1[num][3] = int(datetime.today().strftime("%S"))

            time_1_1_1[num] = int(str(time_1_1[num][1])+str(time_1_1[num][2])+str(time_1_1[num][3]))

            temp_1[num] = temp.get()

            #print(time_1)
            #print(time_1_1)
            #print(name)
            #t.sleep(2)

        et_1.delete(0, "end")
        et_2.delete(0, "end")
        et_3.delete(0, "end")

        window.after(1000, text_changer)
    

def check_data_2():
            value = {'이름' : name,
                     '출근 시간' : time_1,
                     '출근 체온' : temp_1,
                     '퇴근 시간' : time_2,
                     '퇴근 체온' : temp_2,
                     '근무 시간' : work,
                     '근무 시간2': work_1}
    
            value = p.DataFrame(value)
            os.makedirs('c:/check_today/{}'.format(datetime.today().strftime("%m")), exist_ok=True)
            place = 'c:/check_today/{}/{}.xlsx'.format(datetime.today().strftime("%m"), date)
            value.to_excel(excel_writer = place)

            lb_0.configure(text = "Today's file has been created")
            lb_0.place(x = 90, y = 10)
            window.after(1000, text_changer)


def check_data_3(event):
            for i in range(1, 7):
                name[i] = Names[i-1]
            
            m = datetime.today().strftime("%m")

            if m == '01' or m == '03' or m == '05' or m == '07' or m == '08' or m == '10' or m == '12':
                k = 32
            else:
                k = 31

            for m in range(1, k):
                    M = str(m).zfill(2)
                    location = 'c:/check_today/{}'.format(datetime.today().strftime("%m"))
                    file = '{}.xlsx'.format(datetime.today().strftime("%Y-%m-"+M))
                    if os.path.exists('c:\\check_today\\{}\\{}'.format(datetime.today().strftime("%m"), datetime.today().strftime("%Y-%m-"+M)+'.xlsx')):
                        data_pd = p.read_excel('{}/{}'.format(location, file), header = None, index_col = None, names = None)
                        data_np = p.DataFrame.to_numpy(data_pd)
                        print(data_np)
                        # print(data_np)
                        for k in range(2, 8):
                            monthTime[k-1] = monthTime[k-1] + data_np[k, 7]
                            print(monthTime[k-1])
                            t3 = monthTime[k-1]%100
                            # print(t3)
                            time = int(monthTime[k-1]//100)
                            print(time)
                            t2 = time%100
                            # print(t2)
                            time = int(time//100)
                            # print(time)
                            t1 = time%100
                            # print(t1)

                            if t3 >= 60:
                                t3 -= 60
                                t2 += 1
                            
                            if t2 >= 60:
                                t2 -= 60
                                t1 += 1

                            monthTime_1[k-1] = '{}:{}:{}'.format(str(t1).zfill(2), str(t2).zfill(2), str(t3).zfill(2))
                            # print(monthTime_1[k-1])
            month_T = {'이름' : name,
                        '이번달 총 근무 시간' : monthTime_1}
            # print(month_T)
            month_T = p.DataFrame(month_T)
            month_T.to_excel(excel_writer = 'c:/check_today/{}/{}.xlsx'.format(datetime.today().strftime("%m"), '이번달 총 결산'))
            for i in range(0, 7):
                monthTime[i] = 0
                monthTime_1[i] = ''

            lb_0.configure(text = "This month's settlement file has been created")
            lb_0.place(x = 40, y = 10)
            window.after(1000, text_changer)

def check_data_1_1(event):
    check_data_1()

def check_data_2_2(event):
    check_data_2()

# if datetime.today().strftime("%d") == '1':
#         check_data_3or4

window.title('login {}'.format(date))
window.geometry("330x170+100+100")
window.resizable(False, False)

window.bind("<Return>", check_data_1_1)
window.bind("<F5>", check_data_2_2)
window.bind("<F6>", check_data_3)

lb_0 = Label(window, text = "time checker")
lb_0.place(x = 130, y = 10)

lb_1 = Label(window, text = "Username : ")
lb_1.place(x = 20, y = 40)

lb_2 = Label(window, text = "Password : ")
lb_2.place(x = 20, y = 60)

lb_3 = Label(window, text = "Temperature : ")
lb_3.place(x = 20, y = 80)

et_1 = Entry(window, textvariable = user_id)
et_1.place(x = 110, y = 40)

et_2 = Entry(window, textvariable = password, show="*")
et_2.place(x = 110, y = 60)

et_3 = Entry(window, textvariable = temp)
et_3.place(x = 110, y = 80)

btn_1 = Button(window, text = "login", command = check_data_1)
btn_1.place(x = 100, y = 120)

btn_2 = Button(window, text = "Today", command = check_data_2)
btn_2.place(x = 200, y = 120)

if os.path.exists('c:\\check_today\\names.xlsx'):
    location_2 = 'c:\check_today'
    file_2 = 'names.xlsx'
    data_pd = p.read_excel('{}/{}'.format(location_2, file_2), header = None, index_col = None, names = None)
    data_np = p.DataFrame.to_numpy(data_pd)

    for i in range(0, len(data_np)):
        Names.insert(0, data_np[i, 0])

    # print(Names)
else:
    lb_0.configure(text = "There is no list. Please make list first.")
    lb_0.place(x = 80, y = 10)

window.mainloop()
```
