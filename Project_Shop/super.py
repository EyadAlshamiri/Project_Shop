from tkinter import * 
from tkinter import messagebox
import webbrowser
import os 
import sys 
import random 

# defind color 
color1 = '#ff9900'
color2 = '#0B2F3A'
color3 = '#3cff00'
TO1 = 'black'
TO2 = 'white'

pro = Tk()


pro.geometry('800x450+280+50')
# delet all move in program 
pro.resizable(False,False)
pro.title('Shop')
# convert icon program 
pro.iconbitmap('D:\\imag\\icon1.ico')

title = Label( pro , text='Shop System', fg='gold',bg='black' , font=('tajawal',16,'bold') )
title.pack(fill=X)

facebook='https://www.facebook.com/profile.php?id=100082105509492&mibextid=ZbWKwL'
whatsapp='https://api.whatsapp.com/send/?phone=967715804671&text&type=phone_number&app_absent=0'
youtube ='http://www.youtube.com/@thestranger8169'

def open1 () :
    webbrowser.open_new(facebook) 
def open2 () : 
    webbrowser.open_new(whatsapp)
def open3 () : 
    webbrowser.open_new(youtube) 
def about1() :
    messagebox.showinfo(  'المطور' , 'إياد الشميري')
def about2() :
    messagebox.showinfo( 'عن البرنامج ' , 'مشروع بقالة في بايثون تيكنتر ')
def log   () : 
    user  = En1.get() 
    passw = En2.get()
    if user == 'Eyad' and passw == '715804671' : 
        messagebox.showinfo('ترحيب' , 'أهلا وسهلا بك' )
    else:
        messagebox.showerror('خطاء ' , 'للاسف البيانات التي ادخلتها خاطئه ')


F1 = Frame(pro,width=300 , height=420 , bg=color1)
F1.place(x=560 , y= 30)

Title1 = Label(F1 , text='مشروع بقالة' , bg= color1 , fg=TO1 ,font=('tajawal', 12 , 'bold') )
Title1.place(x=60,y=10)
title2 = Label(F1,text='المطور إياد فهيم الشميري' , bg=color1 , fg=TO1 ,font=('tajawal', 12 , 'bold') )
title2.place(x=40,y=50)
title3 = Label(F1 ,text='وسائل الاتصال بنا ' ,bg=color1 , fg=TO1 ,font=('tajawal', 12 , 'bold'))
title3.place(x=52 , y=90)

B1 = Button(F1,text='حسابنا على الفيسبوك', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold') , command=open1)
B1.place(x=6,y=130)
B2 = Button(F1,text='رقم الواتساب ', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold'), command=open2)
B2.place(x=6,y=177)
B3 = Button(F1,text='قناتنا على يتيوب', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold'), command=open3)
B3.place(x=6,y=225)
B4 = Button(F1,text='لمحة عن المطور', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold') ,command= about1)
B4.place(x=6,y=272)
B5 = Button(F1,text='لمحة عن المشروع', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold') , command=about2)
B5.place(x=6,y=318)
B6 = Button(F1,text='إغلاق البرنامج', width=23,fg=TO2 ,bg=color2,font=('tajawal' , 11 ,'bold') , command= quit)
B6.place(x=6,y=365)

# path photo 
photo = PhotoImage(file="D:\\imag\\img5.png")
imo = Label(pro , image=photo)
imo.place(x=50, y=30 , width=500 , height=200)

F2 = Frame(pro,width=560 , height=200 , bg= color1 )
F2.place (x=0 ,y= 303 )

photo1 = PhotoImage(file='D:\\imag\\user.png')
imo1 = Label(pro,image=photo1 , bg= color1)
imo1.place(x= 440 , y= 310 , width=110 , height=110 )
L1 = Label(F2 , text= 'اسم المستخدم ' , fg=TO1 , bg= color1 , font=('tajawal' , 12 ,'bold'))
L1.place(x=330, y=25)
L2 = Label(F2 , text= 'كلمة المرور ' , fg=TO1 , bg= color1 , font=('tajawal' , 12 , 'bold'))
L2.place(x=330, y=70)
En1 = Entry(F2 , font = ('tajawal',12))
En1.place (x=130 , y=26)
En2 = Entry(F2 , font = ('tajawal',12))
En2.place (x=130 , y=71)
B = Button(F2 ,text= 'تسجيل الدخول', bg= color2  ,fg= TO2 ,  font=('tajawal' , 12, 'bold' ),width= 11 , height=3 , command= log)
B.place(x= 5 , y=25) 


user = En1
pasword = En2
if user == 'Eyad' and pasword == '715804671':
    from super2 import *



pro.mainloop ()