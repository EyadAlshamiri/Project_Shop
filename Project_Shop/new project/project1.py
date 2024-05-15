from tkinter import * 


class window :
    #defaind color  
    red    = 'red'
    gren   = 'green'
    white  = 'white'
    black  = 'black'
    color1 = '#0B2F3A'
    color2 = '#0B4C5F'
    color3 = 'tomato'
    color4 = '#DBA901'
    gold   = 'gold' 

    root = Tk() 

    root.geometry('500x700+400+20')
    root.resizable(False,False)
    root.title('cash mony')
#   fream 1 
    f1 = Frame(root ,bg= gold, width=500, height= 700)
    f1.place(x=0 , y=0)

    t1 = Label(root , text='محفضتي '  , bg=black , fg = white , font=('tajawl' , 15 ,'bold'))
    t1.pack(fill=X)

    t2 = Label(root , text='مرحبا بكم في تطبيق محفضتي' , font = ( 'tajawal' , 12 , 'bold') , bg= gold , fg=black)
    t2.place(x= 40 , y= 50)


    root.mainloop () 