from tkinter import * 
import math , random , os 
from tkinter import messagebox 
import time
from datetime import * 

color1 = '#0B2F3A'
color2 = '#0B4C5F'
color3 = 'tomato'
color4 = '#DBA901'
class shop : 
    t1 = 0 
    t2 = 0 
    t3 = 0 
    t4 = 0 

    def __init__(self , root ) :
        self.root = root 
        self.root.geometry('1300x700+30+10')
        self.root.title('shop : بقالة ')
        self.root.resizable(False,False)
        self.root.iconbitmap('') # path icon  
        title = Label(self.root ,text= 'ادارة المشاريع : بقالة ' , fg='white' , bg=color1 , font = ('tajawal' , 15 ) )
        title.pack(fill=X)
        

        self.time = datetime.now()
        # ==== varible mshtryat ====
        self.q1 = DoubleVar()
        self.q2 = DoubleVar()
        self.q3 = DoubleVar()
        self.q4 = DoubleVar()
        self.q5 = DoubleVar()
        self.q6 = DoubleVar()
        self.q7 = DoubleVar()
        self.q8 = DoubleVar()
        self.q9 = DoubleVar()
        self.q10 = DoubleVar()
        self.q11= DoubleVar()
        self.q12= DoubleVar()
        self.q13= DoubleVar()
        self.q14= DoubleVar()
        self.q15= DoubleVar()
        self.q16= DoubleVar()
        self.q17= DoubleVar()
        self.q18= DoubleVar()
        self.q19= DoubleVar()
        self.q20= DoubleVar()
        
        
        self.qq1 = DoubleVar()
        self.qq2 = DoubleVar()
        self.qq3 = DoubleVar()
        self.qq4 = DoubleVar()
        self.qq5 = DoubleVar()
        self.qq6 = DoubleVar()
        self.qq7 = DoubleVar()
        self.qq8 = DoubleVar()
        self.qq9 = DoubleVar()
        self.qq10= DoubleVar()
        self.qq11= DoubleVar()
        self.qq12= DoubleVar()
        self.qq13= DoubleVar()
        self.qq14= DoubleVar()
        self.qq15= DoubleVar()
        self.qq16= DoubleVar()
        self.qq17= DoubleVar()
        self.qq18= DoubleVar()
        self.qq19= DoubleVar()
        self.qq20= DoubleVar()
        

        self.qqq1 = DoubleVar()
        self.qqq2 = DoubleVar()
        self.qqq3 = DoubleVar()
        self.qqq4 = DoubleVar()
        self.qqq5 = DoubleVar()
        self.qqq6 = DoubleVar()
        self.qqq7 = DoubleVar()
        self.qqq8 = DoubleVar()
        self.qqq9 = DoubleVar()
        self.qqq10= DoubleVar()
        self.qqq11= DoubleVar()
        self.qqq12= DoubleVar()
        self.qqq13= DoubleVar()
        self.qqq14= DoubleVar()
        self.qqq15= DoubleVar()
        self.qqq16= DoubleVar()
        


        # ==== name  ======
        self.namo  = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        x = random.randint(1000 , 9999)
        self.fatora.set(str(x))

        # ======= varible hesab alkoly ====== 
        self.ada  = StringVar() 
        self.ahra = StringVar()
        self.hdar = StringVar() 
        #====== customer data =========
        F1 = Frame(root, bd=2 , width=338 , height=170 , bg= color2  )
        F1.place(x=961 , y= 30)
        tit = Label(F1 ,text= ': بيانات المشتري  ' , font=('tajawal' ,13 , 'bold') , bg = color2 , fg= color3 )
        tit.place(x=190 , y= 0)
        his_name = Label(F1 , text=' اسم المشتري ' , font=('tajawal' , 10 ) , bg= color2 , fg='white')
        his_name.place(x = 230 , y = 40 )
        his_phone = Label(F1 , text=' رقم المشتري ' , font=('tajawal' , 10 ) , bg= color2 , fg='white')
        his_phone.place(x = 230 , y = 70 )
        bill_num = Label(F1 , text=' رقم الفاتورة ' , font=('tajawal' , 10 ) , bg= color2 , fg='white')
        bill_num.place(x = 235 , y = 100 )

        Ent_name = Entry(F1 , textvariable=self.namo ,justify='center')
        Ent_name.place(x=90 , y= 42)
        Ent_phone = Entry(F1 , textvariable= self.phono, justify='center')
        Ent_phone.place(x= 90, y= 72)
        Ent_bill = Entry(F1, textvariable=self.fatora ,  justify='center')
        Ent_bill.place(x=90 , y= 102)

        btn_costomer = Button(F1 , text= 'بحث' , font=('tajawal',10 ) , width=8 , height=4 , bg= color4 , command= self.Serch ) 
        btn_costomer.place(x=10 , y= 45 )
        #====== fatora : bill ====
        titdd = Label(F1 , text='[الفواتير]' , font = ('tajawal' , 13 , 'bold') , bg=color2 , fg='gold')
        titdd.place(x=140 , y=135)
        F3 = Frame(root , bd=2 , width=388 , height=399 , bg= 'white')
        F3.place(x=961 , y=200)
        SCROLL_y = Scrollbar(F3 , orient= 'vertical')
        self.textarea = Text(F3 , yscrollcommand= SCROLL_y.set)
        SCROLL_y.pack(side=LEFT , fill= Y)
        SCROLL_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH , expand=1)
        # ======= price  ==========
        F4 = Frame(root , bd= 2 , width=657 , height=112 , bg= color2 )
        F4.place(x=641 , y=587)
        hesab = Button(F4 , text='الحساب' , width=12 , height=1 , font='tajawal' , bg= color4 , command=self.total )
        hesab.place(x=520 ,y= 15)
        fatora = Button (F4 , text='تصدير الفاتورة' , width=12 , height=1 , font='tajawal' , bg= color4 , command= self.savee) 
        fatora.place(x=520 , y=60)
        clear = Button(F4 , text='إفراغ الحقول' , width=12 , height=1 , font='tajawal' , bg=color4 , command=self.clear) 
        clear.place(x= 380 , y=15)
        exit = Button(F4 , text='إغلاق البرنامج ' , width=12 , height=1 , font='tajawal' , bg=color4 , command= self.close) 
        exit.place(x= 380 , y=60)
        dain = Button(F4 ,text='دين' , width=3 , height=3 , font='tajawal' , bg=color4 , command=self.din)
        dain.place(x=330 , y=19)

        labol1 = Label (F4 , text= 'حساب المواد الغذائية' , font = ('tajawal' , 10 , 'bold') , bg= color2  , fg='gold')
        labol1.place(x=190 , y= 10 )
        labol2 = Label (F4 , text= ' حساب المواد الاخرى حساب  ' , font = ('tajawal' , 10 , 'bold') , bg= color2  , fg='gold')
        labol2.place(x=190 , y= 40 )
        labol3 = Label (F4 , text= ' الخضروات والفواكة' , font = ('tajawal' , 10 , 'bold') , bg= color2  , fg='gold')
        labol3.place(x=190 , y= 70 )

        ento1 = Entry(F4 , textvariable= self.ada, width=24) 
        ento1.place(x=40 , y=12)
        ento2 = Entry(F4 , textvariable=self.ahra, width=24) 
        ento2.place(x=40 , y=42)
        ento3 = Entry(F4 , textvariable = self.hdar, width=24) 
        ento3.place(x=40 , y=72)

        #====== items[1] ========
        FF1 = Frame(root , bd = 2 , width=318 , height=668 , bg=color2)
        FF1.place(x=1 , y=30)
        
        t = Label(FF1 ,text='المواد الغذائية' , font = ('tajawal ' , 13 , 'bold' ) , bg=color2 , fg='gold')
        t.place(x=110,y=0)

        m1 = Label(FF1 , text= 'دقيق ابيض' , font=('tajawal',11) , bg=color2 , fg='white' )
        m1.place(x=230,y=50)

        m2 = Label(FF1 , text= 'دقيق احمر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m2.place(x=230,y=80)

        m3 = Label(FF1 , text= 'رز' , font=('tajawal',11) , bg=color2 , fg='white' )
        m3.place(x=256,y=110)

        m4 = Label(FF1 , text= 'سكر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m4.place(x=250,y=140)

        m5 = Label(FF1 , text= 'هند' , font=('tajawal',11) , bg=color2 , fg='white' )
        m5.place(x=255,y=170)

        m6 = Label(FF1 , text= 'ذرة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m6.place(x=255,y=200)

        m7 = Label(FF1 , text= 'دخن' , font=('tajawal',11) , bg=color2 , fg='white' )
        m7.place(x=251,y=230) 

        m8 = Label(FF1 , text= 'دجاج' , font=('tajawal',11) , bg=color2 , fg='white' )
        m8.place(x=249,y=260)

        m9 = Label(FF1 , text= 'جبن' , font=('tajawal',11) , bg=color2 , fg='white' )
        m9.place(x=250,y=290)

        m10= Label(FF1 , text= 'حقين' , font=('tajawal',11) , bg=color2 , fg='white' )
        m10.place(x=249,y=320)

        m11= Label(FF1 , text= 'زبادي' , font=('tajawal',11) , bg=color2 , fg='white' )
        m11.place(x=245,y=350)

        m12= Label(FF1 , text= 'فاصوليا' , font=('tajawal',11) , bg=color2 , fg='white' )
        m12.place(x=238,y=380)

        m13= Label(FF1 , text= 'فول' , font=('tajawal',11) , bg=color2 , fg='white' )
        m13.place(x=251,y=410)

        m14= Label(FF1 , text= 'بازيلا' , font=('tajawal',11) , bg=color2 , fg='white' )
        m14.place(x=245,y=440)

        m15= Label(FF1 , text= 'بيض' , font=('tajawal',11) , bg=color2 , fg='white' )
        m15.place(x=250,y=470)

        m16= Label(FF1 , text= 'تونة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m16.place(x=251,y=500)

        m17= Label(FF1 , text= 'مفروم' , font=('tajawal',11) , bg=color2 , fg='white' )
        m17.place(x=245,y=530)

        m18= Label(FF1 , text= 'مكرونه' , font=('tajawal',11) , bg=color2 , fg='white' )
        m18.place(x=244,y=560)

        m19= Label(FF1 , text= 'حلاوة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m19.place(x=248,y=590)

        m20= Label(FF1 , text= 'شعيرية' , font=('tajawal',11) , bg=color2 , fg='white' )
        m20.place(x=243,y=620)

        # === entry === 
        ment1 = Entry(FF1 , textvariable= self.q1 , width=12)
        ment1.place(x= 70, y= 50 )

        ment2 = Entry(FF1, textvariable= self.q2 , width=12)
        ment2.place(x= 70, y=80 )

        ment3 = Entry(FF1 , textvariable= self.q3, width=12)
        ment3.place(x=70 , y= 110)

        ment4 = Entry(FF1 , textvariable= self.q4, width=12)
        ment4.place(x= 70, y=140 )

        ment5 = Entry(FF1 , textvariable= self.q5, width=12)
        ment5.place(x= 70, y= 170)

        ment6 = Entry(FF1 , textvariable= self.q6, width=12)
        ment6.place(x= 70, y=200 )

        ment7 = Entry(FF1 , textvariable= self.q7, width=12)
        ment7.place(x= 70, y= 230)

        ment8 = Entry(FF1 , textvariable= self.q8, width=12)
        ment8.place(x= 70, y=260 )

        ment9 = Entry(FF1, textvariable= self.q9 , width=12)
        ment9.place(x= 70, y= 290)

        ment10 = Entry(FF1 , textvariable= self.q10, width=12)
        ment10.place(x= 70, y=320 )

        ment11 = Entry(FF1 , textvariable= self.q11, width=12)
        ment11.place(x= 70, y= 350)

        ment12 = Entry(FF1 , textvariable= self.q12, width=12)
        ment12.place(x= 70, y= 380 )

        ment13 = Entry(FF1 , textvariable= self.q13, width=12)
        ment13.place(x= 70, y=410 )

        ment14 = Entry(FF1 , textvariable= self.q14, width=12)
        ment14.place(x= 70, y= 440)

        ment15 = Entry(FF1 , textvariable= self.q15, width=12)
        ment15.place(x= 70, y= 470)

        ment16 = Entry(FF1, textvariable= self.q16 , width=12)
        ment16.place(x= 70, y= 500)

        ment17 = Entry(FF1 , textvariable= self.q17, width=12)
        ment17.place(x= 70, y= 530)

        ment18 = Entry(FF1 , textvariable= self.q18, width=12)
        ment18.place(x= 70, y= 560)

        ment19 = Entry(FF1 , textvariable= self.q19, width=12)
        ment19.place(x= 70 , y= 590 )

        ment20 = Entry(FF1 , textvariable= self.q20, width=12)
        ment20.place(x= 70, y= 620 )

        #====== items[2] ==========
        FF2 = Frame(root , bd=2 , width=318 , height=668 , bg=color2)
        FF2.place(x=321 , y=30)

        t2 = Label(FF2 ,text='مواداخرى' , font = ('tajawal ' , 13 , 'bold' ) , bg=color2 , fg='gold')
        t2.place(x=120,y=0)

        m1 = Label(FF2 , text= 'ابوولد' , font=('tajawal',11) , bg=color2 , fg='white' )
        m1.place(x=240,y=50)

        m2 = Label(FF2 , text= 'بفك' , font=('tajawal',11) , bg=color2 , fg='white' )
        m2.place(x=250,y=80)

        m3 = Label(FF2 , text= 'ماري' , font=('tajawal',11) , bg=color2 , fg='white' )
        m3.place(x=248,y=110)

        m4 = Label(FF2 , text= 'شكلاة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m4.place(x=248,y=140)

        m5 = Label(FF2 , text= 'حلوا' , font=('tajawal',11) , bg=color2 , fg='white' )
        m5.place(x=250,y=170)

        m6 = Label(FF2 , text= 'ببسي' , font=('tajawal',11) , bg=color2 , fg='white' )
        m6.place(x=247,y=200)

        m7 = Label(FF2 , text= 'ماء' , font=('tajawal',11) , bg=color2 , fg='white' )
        m7.place(x=255,y=230) 

        m8 = Label(FF2 , text= 'عصيرمانجو' , font=('tajawal',11) , bg=color2 , fg='white' )
        m8.place(x=235,y=260)

        m9 = Label(FF2 , text= 'جوافة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m9.place(x=248,y=290)

        m10= Label(FF2 , text= 'رامبو' , font=('tajawal',11) , bg=color2 , fg='white' )
        m10.place(x=249,y=320)

        m11= Label(FF2 , text= 'شوفان' , font=('tajawal',11) , bg=color2 , fg='white' )
        m11.place(x=248,y=350)

        m12= Label(FF2 , text= 'محلبية' , font=('tajawal',11) , bg=color2 , fg='white' )
        m12.place(x=245,y=380)

        m13= Label(FF2 , text= 'صابون' , font=('tajawal',11) , bg=color2 , fg='white' )
        m13.place(x=250,y=410)

        m14= Label(FF2 , text= 'تمر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m14.place(x=255,y=440)

        m15= Label(FF2 , text= 'اندومي' , font=('tajawal',11) , bg=color2 , fg='white' )
        m15.place(x=245,y=470)

        m16= Label(FF2 , text= 'سيفر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m16.place(x=253,y=500)

        m17= Label(FF2 , text= 'لمبة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m17.place(x=250,y=530)

        m18= Label(FF2 , text= 'شاي' , font=('tajawal',11) , bg=color2 , fg='white' )
        m18.place(x=255,y=560)

        m19= Label(FF2 , text= 'ثلاجة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m19.place(x=248,y=590)

        m20= Label(FF2 , text= 'دفاتر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m20.place(x=249,y=620)

        # === entry === 
        ment1 = Entry(FF2 , textvariable = self.qq1, width=12)
        ment1.place(x= 70, y= 50 )

        ment2 = Entry(FF2 , textvariable= self.qq2 ,width=12)
        ment2.place(x= 70, y=80 )

        ment3 = Entry(FF2 , textvariable= self.qq3, width=12)
        ment3.place(x=70 , y= 110)

        ment4 = Entry(FF2 , textvariable= self.qq4, width=12)
        ment4.place(x= 70, y=140 )

        ment5 = Entry(FF2 , textvariable= self.qq5, width=12)
        ment5.place(x= 70, y= 170)

        ment6 = Entry(FF2 , textvariable= self.qq6, width=12)
        ment6.place(x= 70, y=200 )

        ment7 = Entry(FF2 , textvariable= self.qq7, width=12)
        ment7.place(x= 70, y= 230)

        ment8 = Entry(FF2 , textvariable= self.qq8, width=12)
        ment8.place(x= 70, y=260 )

        ment9 = Entry(FF2 , textvariable= self.qq9, width=12)
        ment9.place(x= 70, y= 290)

        ment10 = Entry(FF2 , textvariable= self.qq10, width=12)
        ment10.place(x= 70, y=320 )

        ment11 = Entry(FF2 , textvariable= self.qq11, width=12)
        ment11.place(x= 70, y= 350)

        ment12 = Entry(FF2, textvariable= self.qq12 , width=12)
        ment12.place(x= 70, y= 380 )

        ment13 = Entry(FF2, textvariable= self.qq13 , width=12)
        ment13.place(x= 70, y=410 )

        ment14 = Entry(FF2 , textvariable= self.qq14, width=12)
        ment14.place(x= 70, y= 440)

        ment15 = Entry(FF2 , textvariable= self.qq15, width=12)
        ment15.place(x= 70, y= 470)

        ment16 = Entry(FF2 , textvariable= self.qq16, width=12)
        ment16.place(x= 70, y= 500)

        ment17 = Entry(FF2 , textvariable= self.qq17, width=12)
        ment17.place(x= 70, y= 530)

        ment18 = Entry(FF2 , textvariable= self.qq18, width=12)
        ment18.place(x= 70, y= 560)

        ment19 = Entry(FF2 , textvariable= self.qq19, width=12)
        ment19.place(x= 70 , y= 590 )

        ment20 = Entry(FF2 , textvariable= self.qq20, width=12)
        ment20.place(x= 70, y= 620 )



        #====== items[3] ==========
        FF3 = Frame(root , bd=2 , width=318 , height=555 , bg=color2)
        FF3.place(x=641 , y=30)

        t2 = Label(FF3 ,text='خضروات وفواكه' , font = ('tajawal ' , 13 , 'bold' ) , bg=color2 , fg='gold')
        t2.place(x=120,y=0)

        m1 = Label(FF3 , text= 'طماط' , font=('tajawal',11) , bg=color2 , fg='white' )
        m1.place(x=230,y=50)

        m2 = Label(FF3 , text= 'بطاط' , font=('tajawal',11) , bg=color2 , fg='white' )
        m2.place(x=230,y=80)

        m3 = Label(FF3, text= 'بصل' , font=('tajawal',11) , bg=color2 , fg='white' )
        m3.place(x=235,y=110)

        m4 = Label(FF3 , text= 'ثوم' , font=('tajawal',11) , bg=color2 , fg='white' )
        m4.place(x=235,y=140)

        m5 = Label(FF3 , text= 'كوسا' , font=('tajawal',11) , bg=color2 , fg='white' )
        m5.place(x=230,y=170)

        m6 = Label(FF3 , text= 'سلطة' , font=('tajawal',11) , bg=color2 , fg='white' )
        m6.place(x=230,y=200)

        m7 = Label(FF3 , text= 'بسباس' , font=('tajawal',11) , bg=color2 , fg='white' )
        m7.place(x=228,y=230) 

        m8 = Label(FF3 , text= 'بادنجان' , font=('tajawal',11) , bg=color2 , fg='white' )
        m8.place(x=225,y=260)

        m9 = Label(FF3 , text= 'باميا' , font=('tajawal',11) , bg=color2 , fg='white' )
        m9.place(x=230,y=290)

        m10= Label(FF3 , text= 'جزر' , font=('tajawal',11) , bg=color2 , fg='white' )
        m10.place(x=235,y=320)

        m11= Label(FF3 , text= 'خيار' , font=('tajawal',11) , bg=color2 , fg='white' )
        m11.place(x=230,y=350)

        m12= Label(FF3 , text= 'عنب' , font=('tajawal',11) , bg=color2 , fg='white' )
        m12.place(x=235,y=380)

        m13= Label(FF3 , text= 'مانجو' , font=('tajawal',11) , bg=color2 , fg='white' )
        m13.place(x=228,y=410)

        m14= Label(FF3 , text= 'تفاح' , font=('tajawal',11) , bg=color2 , fg='white' )
        m14.place(x=230,y=440)

        m15= Label(FF3 , text= 'موز' , font=('tajawal',11) , bg=color2 , fg='white' )
        m15.place(x=235,y=470)

        m16= Label(FF3 , text= 'برتقال' , font=('tajawal',11) , bg=color2 , fg='white' )
        m16.place(x=228,y=500)

        # === entry === 
        ment1 = Entry(FF3 , textvariable= self.qqq1, width=12)
        ment1.place(x= 70, y= 50 )

        ment2 = Entry(FF3 , textvariable= self.qqq2 , width=12)
        ment2.place(x= 70, y=80 )

        ment3 = Entry(FF3 , textvariable= self.qqq3, width=12)
        ment3.place(x=70 , y= 110)

        ment4 = Entry(FF3 , textvariable= self.qqq4, width=12)
        ment4.place(x= 70, y=140 )

        ment5 = Entry(FF3 , textvariable= self.qqq5, width=12)
        ment5.place(x= 70, y= 170)

        ment6 = Entry(FF3 , textvariable= self.qqq6, width=12)
        ment6.place(x= 70, y=200 )

        ment7 = Entry(FF3 , textvariable= self.qqq7, width=12)
        ment7.place(x= 70, y= 230)

        ment8 = Entry(FF3 , textvariable= self.qqq8, width=12)
        ment8.place(x= 70, y=260 )

        ment9 = Entry(FF3 , textvariable= self.qqq9, width=12)
        ment9.place(x= 70, y= 290)

        ment10 = Entry(FF3 , textvariable= self.qqq10, width=12)
        ment10.place(x= 70, y=320 )

        ment11 = Entry(FF3 , textvariable= self.qqq11, width=12)
        ment11.place(x= 70, y= 350)

        ment12 = Entry(FF3 , textvariable= self.qqq12, width=12)
        ment12.place(x= 70, y= 380 )

        ment13 = Entry(FF3 , textvariable= self.qqq13, width=12)
        ment13.place(x= 70, y=410 )

        ment14 = Entry(FF3 , textvariable= self.qqq14, width=12)
        ment14.place(x= 70, y= 440)

        ment15 = Entry(FF3 , textvariable= self.qqq15, width=12)
        ment15.place(x= 70, y= 470)

        ment16 = Entry(FF3 , textvariable= self.qqq16, width=12)
        ment16.place(x= 70, y= 500)

        self.welcom()

        

    def total(self) : 
        # ====== items 1=============
        self.tabona = self.q1.get()*13000
        self.bor = self.q2.get()*12000
        self.rez = self.q3.get()*10000
        self.sokr= self.q4.get()*14000
        self.hend= self.q5.get()*13000
        self.thrh= self.q6.get()*500
        self.dhn = self.q7.get()*500
        self.chek= self.q8.get()*2000
        self.chos= self.q9.get()*1600
        self.hken= self.q10.get()*350
        self.zbad=self.q11.get()*250 
        self.faso= self.q12.get()*400
        self.fol = self.q13.get()*400
        self.paze= self.q14.get()*500
        self.egg = self.q15.get()*50
        self.tona= self.q16.get()*500
        self.mfro= self.q17.get()*700
        self.mkro= self.q18.get()*200
        self.hlaw= self.q19.get()*3200 
        self.shir= self.q20.get()*250
        #   sum 
        self.totalada = float(
            self.tabona+
            self.bor+
            self.rez+
            self.sokr+
            self.hend+
            self.thrh+
            self.dhn+
            self.chek+
            self.chos+
            self.hken+
            self.zbad+
            self.faso+
            self.fol+
            self.paze+
            self.egg+
            self.tona+
            self.mfro+
            self.mkro+
            self.hlaw+
            self.shir
        )
        self.ada.set(str(self.totalada) + "  real")

        #=====items 2 =============
        self.aboold = self.qq1.get()*300
        self.befk   = self.qq2.get()*50
        self.mary   = self.qq3.get()*300
        self.chklah = self.qq4.get()*200
        self.hloa   = self.qq5.get()*20
        self.bebsi  = self.qq6.get()*250
        self.water  = self.qq7.get()*150
        self.gos_man= self.qq8.get()*400
        self.gos_goa= self.qq9.get()*150
        self.rambo  = self.qq10.get()*150
        self.shofan =self.qq11.get()*1500
        self.mohlbeh= self.qq12.get()*1500
        self.sabon_k= self.qq13.get()*2500
        self.tmr    = self.qq14.get()*800
        self.indomi = self.qq15.get()*170
        self.sefer  = self.qq16.get()*9000
        self.lmbh   = self.qq17.get()*600
        self.shai_te= self.qq18.get()*1000
        self.thlagh = self.qq19.get()*5000
        self.dfater = self.qq20.get()*100

        #    sum  
        self.totalahra = float(
            self.aboold+
            self.befk+
            self.mary+
            self.chklah+
            self.hloa+
            self.bebsi+
            self.water+
            self.gos_man+
            self.gos_goa+
            self.rambo+
            self.shofan+
            self.mohlbeh+
            self.sabon_k+
            self.tmr+
            self.indomi+
            self.sefer+
            self.lmbh+
            self.shai_te+
            self.thlagh+
            self.dfater
        )
        self.ahra.set(str(self.totalahra) + "  real")


        #===== items 3 ================
        self.tomatos = self.qqq1.get()*500
        self.botito  = self.qqq2.get()*600
        self.basl    = self.qqq3.get()*400
        self.thoma   = self.qqq4.get()*3000
        self.kosa    = self.qqq5.get()*500
        self.slata   = self.qqq6.get()*200
        self.bsbas   = self.qqq7.get()*100
        self.badingan= self.qqq8.get()*400
        self.bamia   = self.qqq9.get()*1000
        self.jozar   = self.qqq10.get()*600
        self.hoyar   =self.qqq11.get()*400
        self.inab    = self.qqq12.get()*800
        self.mango   = self.qqq13.get()*700
        self.appel   = self.qqq14.get()*1000
        self.bnanas  = self.qqq15.get()*400
        self.orange  = self.qqq16.get()*1000
        
        #   sum    
        self.totalhdar = float(
            self.tomatos+
            self.botito+
            self.basl+
            self.thoma+
            self.kosa+
            self.slata+
            self.bsbas+
            self.badingan+
            self.bamia+
            self.jozar+
            self.hoyar+
            self.inab+
            self.mango+
            self.appel+
            self.bnanas+
            self.orange
        )
        self.hdar.set(str(self.totalhdar) + "  real")

        self.all = float(
            self.totalada +
            self.totalahra +
            self.totalhdar
        )

        self.t1 = self.t1+self.totalada
        self.t2 = self.t2+self.totalahra
        self.t3 = self.t3+self.totalhdar
        self.t4 = self.t4+self.all


        self.billing()
        
        
    def resalt (self) : 
        self.a = 'حساب المواد الغذائية : '
        self.b = 'حساب المواد الاخرى : '
        self.c = 'حساب الخضار والفواكة : ' 
        self.d = ' الحساب الكلي : '


        self.file2 = open('D:\\Project_shop\\resalt\\'+str(time.strftime('%H/%M/%S'))+'.txt' , 'x' , encoding='utf-8')
        self.file2.write(self.a + "  =  " + str(self.t1) +'\n')
        self.file2.write(self.b + "  =  " + str(self.t2) +'\n')
        self.file2.write(self.c + "  =  " + str(self.t3) +'\n')
        self.file2.write(self.d + "  =  " + str(self.t4) +'\n')
        self.file2.close() 
        


    def welcom (self) : 
        self.textarea.delete('1.0' ,END)
        self.textarea.insert(END,'\tبقالة الخير ترحب بكم ')
        self.textarea.insert(END,"\n=================================")
        self.textarea.insert(END,f"\n\t رقم الفاتورة :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t اسم العميل   :{self.namo.get()}")
        self.textarea.insert(END,f"\n\t رقم العميل   :{self.phono.get()}")
        self.textarea.insert(END,"\n========== =======================")
        self.textarea.insert(END,f"\n السعر\t    العدد \t   المشتريات")
        self.textarea.insert(END,"\n=================================")
        
    def clear (self):
        self.num = 0
        self.q1.set(0.0)
        self.q2.set(0.0)
        self.q3.set(0.0)
        self.q4.set(0.0)
        self.q5.set(0.0)
        self.q6.set(0.0)
        self.q7.set(0.0)
        self.q8.set(0.0)
        self.q9.set(0.0)
        self.q10.set(0.0)
        self.q11.set(0.0)
        self.q12.set(0.0)
        self.q13.set(0.0)
        self.q14.set(0.0)
        self.q15.set(0.0)
        self.q16.set(0.0)
        self.q17.set(0.0)
        self.q18.set(0.0)
        self.q19.set(0.0)
        self.q20.set(0.0)

        self.qq1.set(0.0)
        self.qq2.set(0.0)
        self.qq3.set(0.0)
        self.qq4.set(0.0)
        self.qq5.set(0.0)
        self.qq6.set(0.0)
        self.qq7.set(0.0)
        self.qq8.set(0.0)
        self.qq9.set(0.0)
        self.qq10.set(0.0)
        self.qq11.set(0.0)
        self.qq12.set(0.0)
        self.qq13.set(0.0)
        self.qq14.set(0.0)
        self.qq15.set(0.0)
        self.qq16.set(0.0)
        self.qq17.set(0.0)
        self.qq18.set(0.0)
        self.qq19.set(0.0)
        self.qq20.set(0.0)
        
        self.qqq1.set(0.0)
        self.qqq2.set(0.0)
        self.qqq3.set(0.0)
        self.qqq4.set(0.0)
        self.qqq5.set(0.0)
        self.qqq6.set(0.0)
        self.qqq7.set(0.0)
        self.qqq8.set(0.0)
        self.qqq9.set(0.0)
        self.qqq10.set(0.0)
        self.qqq11.set(0.0)
        self.qqq12.set(0.0)
        self.qqq13.set(0.0)
        self.qqq14.set(0.0)
        self.qqq15.set(0.0)
        self.qqq16.set(0.0)

        self.ada.set(0.0)
        self.ahra.set(0.0)
        self.hdar.set(0.0)

        self.namo.set('')
        self.phono.set('')
        self.fatora.set('')
        #  
        
        
    def close (self) :
        self.root.destroy()
        self.resalt()

    def savee (self) : 
        op = messagebox.askquestion('حفظ' , 'هل تريد حفظ الفاتورة ')
        if op == 'yes' :
            self.bb = self.textarea.get('1.0' , END)
            f1 = open('D:\\Project_shop\\shop_fatora\\'+str(self.fatora.get())+".txt" , "x" , encoding="utf-8")
            f1.write(self.bb)
            f1.close() 
        else : 
            return 
    
    def Serch(self):
        txt = StringVar()
        def serch () : 
            file = open('D:\\Project_shop\\shop_fatora\\'+ str( txt.get())+".txt" , "r" , encoding="utf-8")
            f = file.read() 
            red = Tk() 
            red.geometry('500x500')
            T = Label(red , text= f , bg='white' , fg= 'black' , font=(10))
            T.place(x=1,y=1)
            red.mainloop()
        def cler ():
            txt.set('')

        r = Tk() 
        
        r.geometry('250x100')
        f = Frame(r, bg='gold' , height=100 , width=250)
        f.place(x=0 , y=0)
        l1 = Label(r, text='ادخل رقم الفاتورة',bg='gold' , fg='black',bd=5)
        l1.place(x=140,y=3)
        en = Entry(r, textvariable= txt , width=15)
        en.place(x=20 , y=8)
        b = Button (r , bg= 'white' , text='serch' , fg='black' , width=10 , height=2 , command=serch)
        b.place(x=100 , y=50 )
        b2 = Button (r , bg= 'white' , text='cler' , fg='black' , width=10 , height=2 , command=cler)
        b2.place(x=10 , y=50 )
        r.mainloop()

    
    num = 0

    def din (self) :
        r = self.textarea.get('9.0' , END)
        if os.path.exists('D:\\Project_shop\\dain\\'+str(self.namo.get())+'.txt') == True and self.num == 0 :
            file = open('D:\\Project_shop\\dain\\'+str(self.namo.get())+'.txt', 'a' , encoding='utf-8')
            self.num = 1 
        else :
            file = open('D:\\Project_shop\\dain\\'+str(self.namo.get())+'.txt', 'x' , encoding='utf-8')
            self.num = 1
        file.write(r)
        file.close()


    def billing(self) : 
        if self.namo.get() == "" or self.phono.get() == "" :
            messagebox.showerror(  "حدث خطأ " ,"لايجوز ترك حقل الاسم ورقم الهاتف فارغا " )
        elif self.ada.get() == "0.0 real" and self.ahra.get() == "0.0 real" and self.hdar.get() == "0.0 real" : 
            messagebox.showerror( " حدث خطأ" ,"ليس هناك منتجات محددة الرجاء تحديد منتج ") 
        else :
            self.welcom() 
            if self.q1.get() != 0 :
                self.textarea.insert(END , f"\n {self.tabona}\t    {self.q1.get()}\t\t  دقيق ابيض")
            if self.q2.get() != 0 : 
                self.textarea.insert(END , f"\n {self.bor}\t    {self.q2.get()}\t\t   دقيق احمر  ")
            if self.q3.get() != 0 :
                self.textarea.insert(END , f"\n {self.rez}\t    {self.q3.get()}\t\t   رز  ")
            if self.q4.get() != 0 :
                self.textarea.insert(END , f"\n {self.sokr}\t    {self.q4.get()}\t\t  سكر")
            if self.q5.get() != 0 :
                self.textarea.insert(END , f"\n {self.hend}\t    {self.q5.get()}\t \t هند ")
            if self.q6.get() != 0 :
                self.textarea.insert(END , f"\n {self.thrh}\t    {self.q6.get()}\t\t  ذرة   ")
            if self.q7.get() != 0 :
                self.textarea.insert(END , f"\n {self.dhn}\t     {self.q7.get()}\t\t دخن ")
            if self.q8.get() != 0 :
                self.textarea.insert(END , f"\n {self.chek}\t    {self.q8.get()}\t\t دجاج")
            if self.q9.get() != 0 :
                self.textarea.insert(END , f"\n {self.chos}\t    {self.q9.get()}\t\t جبن")
            if self.q10.get() != 0 :
                self.textarea.insert(END , f"\n {self.hken}\t    {self.q10.get()}\t\t حقين")
            if self.q11.get() != 0 :
                self.textarea.insert(END , f"\n {self.zbad}\t    {self.q11.get()}\t\t زبادي")
            if self.q12.get() != 0 :
                self.textarea.insert(END , f"\n {self.faso}\t    {self.q12.get()}\t\t فاصولياء")
            if self.q13.get() != 0 :
                self.textarea.insert(END , f"\n {self.fol}\t     {self.q13.get()}\t\t فول")
            if self.q14.get() != 0 :
                self.textarea.insert(END , f"\n {self.paze}\t    {self.q14.get()}\t\t بازيلا")
            if self.q15.get() != 0 :
                self.textarea.insert(END , f"\n {self.egg}\t     {self.q15.get()}\t\t بيض")
            if self.q16.get() != 0 :
                self.textarea.insert(END , f"\n {self.tona}\t    {self.q16.get()}\t\t تونة")
            if self.q17.get() != 0 :
                self.textarea.insert(END , f"\n {self.mfro}\t    {self.q17.get()}\t\t مفروم")
            if self.q18.get() != 0 :
                self.textarea.insert(END , f"\n {self.mkro}\t    {self.q18.get()}\t\t مكرونة ")
            if self.q19.get() != 0 :
                self.textarea.insert(END , f"\n {self.hlaw}\t    {self.q19.get()}\t\t حلاوة")
            if self.q20.get() != 0 :
                self.textarea.insert(END , f"\n {self.shir}\t    {self.q20.get()}\t\t شعيرية")
            
            if self.qq1.get() != 0 :
                self.textarea.insert(END , f"\n {self.aboold}\t     {self.qq1.get()}\t\t  ابو ولد ")
            if self.qq2.get() != 0 : 
                self.textarea.insert(END , f"\n {self.befk}\t     {self.qq2.get()}\t\t بفك")
            if self.qq3.get() != 0 :
                self.textarea.insert(END , f"\n {self.mary}\t     {self.qq3.get()}\t\t ماري ")
            if self.qq4.get() != 0 :
                self.textarea.insert(END , f"\n {self.chklah}\t   {self.qq4.get()}\t\t شكلاة")
            if self.qq5.get() != 0 :
                self.textarea.insert(END , f"\n {self.hloa}\t    {self.qq5.get()}\t\tحلوا  ")
            if self.qq6.get() != 0 :
                self.textarea.insert(END , f"\n {self.bebsi}\t    {self.qq6.get()}\t\t ببسي ")
            if self.qq7.get() != 0 :
                self.textarea.insert(END , f"\n {self.water}\t    {self.qq7.get()}\t\t ماء ")
            if self.qq8.get() != 0 :
                self.textarea.insert(END , f"\n {self.gos_man}\t     {self.qq8.get()}\t\t عصير مانجو")
            if self.qq9.get() != 0 :
                self.textarea.insert(END , f"\n {self.gos_goa}\t     {self.qq9.get()}\t\t جوافة ")
            if self.qq10.get() != 0 :
                self.textarea.insert(END , f"\n {self.rambo}\t     {self.qq10.get()}\t\t رامبو ")
            if self.qq11.get() != 0 :
                self.textarea.insert(END , f"\n {self.shofan}\t     {self.qq11.get()}\t\t شوفان")
            if self.qq12.get() != 0 :
                self.textarea.insert(END , f"\n {self.mohlbeh}\t     {self.qq12.get()}\t\t محلبية")
            if self.qq13.get() != 0 :
                self.textarea.insert(END , f"\n {self.sabon_k}\t     {self.qq13.get()}\t\t صابون")
            if self.qq14.get() != 0 :
                self.textarea.insert(END , f"\n {self.tmr}\t     {self.qq14.get()}\t\t تمر")
            if self.qq15.get() != 0 :
                self.textarea.insert(END , f"\n {self.indomi}\t     {self.qq15.get()}\t\t اندومي")
            if self.qq16.get() != 0 :
                self.textarea.insert(END , f"\n {self.sefer}\t     {self.qq16.get()}\t\t سيفر")
            if self.qq17.get() != 0 :
                self.textarea.insert(END , f"\n {self.lmbh}\t     {self.qq17.get()}\t\t لمبة")
            if self.qq18.get() != 0 :
                self.textarea.insert(END , f"\n {self.shai_te}\t     {self.qq18.get()}\t\t شاي ")
            if self.qq19.get() != 0 :
                self.textarea.insert(END , f"\n {self.thlagh}\t     {self.qq19.get()}\t\t ثلاجة")
            if self.qq20.get() != 0 :
                self.textarea.insert(END , f"\n {self.dfater}\t     {self.qq20.get()}\t\t دفاتر")
            
            if self.qqq1.get() != 0 :
                self.textarea.insert(END , f"\n {self.tomatos}\t     {self.qqq1.get()}\t\t  طماط ")
            if self.qqq2.get() != 0 : 
                self.textarea.insert(END , f"\n {self.botito}\t     {self.qqq2.get()}\t\t بطاط")
            if self.qqq3.get() != 0 :
                self.textarea.insert(END , f"\n {self.basl}\t     {self.qqq3.get()}\t\t بصل ")
            if self.qqq4.get() != 0 :
                self.textarea.insert(END , f"\n {self.thoma}\t     {self.qqq4.get()}\t\t  ثوم ")
            if self.qqq5.get() != 0 :
                self.textarea.insert(END , f"\n {self.kosa}\t     {self.qqq5.get()}\t\t كوسا ")
            if self.qqq6.get() != 0 :
                self.textarea.insert(END , f"\n {self.slata}\t     {self.qqq6.get()}\t\t سلطة ")
            if self.qqq7.get() != 0 :
                self.textarea.insert(END , f"\n {self.bsbas}\t     {self.qqq7.get()}\t\t بسباس ")
            if self.qqq8.get() != 0 :
                self.textarea.insert(END , f"\n {self.badingan}\t     {self.qqq8.get()}\t\t بادنجان")
            if self.qqq9.get() != 0 :
                self.textarea.insert(END , f"\n {self.bamia}\t     {self.qqq9.get()}\t\t باميا ")
            if self.qqq10.get() != 0 :
                self.textarea.insert(END , f"\n {self.jozar}\t     {self.qqq10.get()}\t\t جزر ")
            if self.qqq11.get() != 0 :
                self.textarea.insert(END , f"\n {self.hoyar}\t     {self.qqq11.get()}\t\t خيار")
            if self.qqq12.get() != 0 :
                self.textarea.insert(END , f"\n {self.inab}\t     {self.qqq12.get()}\t\t عنب")
            if self.qqq13.get() != 0 :
                self.textarea.insert(END , f"\n {self.mango}\t     {self.qqq13.get()}\t\t مانجو")
            if self.qqq14.get() != 0 :
                self.textarea.insert(END , f"\n {self.appel}\t     {self.qqq14.get()}\t\t تفاح")
            if self.qqq15.get() != 0 :
                self.textarea.insert(END , f"\n {self.bnanas}\t     {self.qqq15.get()}\t\t موز")
            if self.qqq16.get() != 0 :
                self.textarea.insert(END , f"\n {self.orange}\t     {self.qqq16.get()}\t\t برتقال")
            
            self.textarea.insert(END,"\n........................................")
            self.textarea.insert(END,f"\n\t{self.all}  real \t  المجموع الكلي")
            self.textarea.insert(END,"\n........................................")
            self.textarea.insert(END,f"\n  التاريخ والوقت :   {self.time}")

root = Tk() 
ob = shop(root)
root.mainloop()