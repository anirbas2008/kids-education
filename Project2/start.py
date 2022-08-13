from pickle import LONG4
from pydoc import TextRepr
from tkinter import *
from   PIL import Image,ImageTk
import json

def register():
    root7 = Tk()
    root7.geometry('500x400')
    root7.configure(bg='#34eb9b')

    label0 = Label(root7, text="Registration",width=20,font=("bold", 20),bg='#34eb9b')
    label0.place(x=70,y=53)
    def check():
        a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        d = entry4.get()

        print(a,b,c,d)
        l = {
            'first name': a,
            'last name':b,
            'phone number':c,
            'e-mail':d
            
        }
    
        with open('register.json','r') as a:
            d = json.load(a)
            
        d.append(l)

        with open('register.json','w') as a:
            json.dump(
                d,a
            )
        root7.destroy()
        start()


    label1 = Label(root7, text="First name",width=20,font=("bold", 15),bg='#34eb9b',fg='white')
    label1.place(x=120,y=103)
    entry1 = Entry(root7, width=20,bg='white',fg='black',font=('Arial',14,'bold'))
    entry1.place(x=120,y=130)
    label2 = Label(root7, text="Last name",width=20,font=("bold", 15),bg='#34eb9b',fg='white')
    label2.place(x=120,y=163)
    entry2 = Entry(root7, width=20,bg='white',fg='black',font=('Arial',14,'bold'))
    entry2.place(x=120,y=190)
    label3 = Label(root7, text="Phone number",width=20,font=("bold", 15),bg='#34eb9b',fg='white',)
    label3.place(x=120,y=223)
    entry3 = Entry(root7, width=20,bg='white',fg='black',font=('Arial',14,'bold'), show='*')
    entry3.place(x=120,y=250)
    label4 = Label(root7, text="E-mail",width=20,font=("bold", 15),bg='#34eb9b',fg='white')
    label4.place(x=120,y=283)
    entry4 = Entry(root7, width=20,bg='white',fg='black',font=('Arial',14,'bold'))
    entry4.place(x=120,y=310)
    button = Button(root7, text='Next',width=7,height=1,bg='grey',command=check)
    button.place(y=350, x=250)
    root7.mainloop()

def start():
    root = Tk()
    root.geometry('1250x900')
    root.configure(bg='ivory')

    def next():
        root.destroy()
        another_courses()
    def next2():
        root.destroy()
        register()    
    def pay():
        root.destroy()
        pay1()
    def about_teachers():
        root.destroy()
        about_teachers1()
    def first():
        root.destroy()
        math()
    def second():
        root.destroy()
        english()
    def third():
        root.destroy()
        it()
    def fourth():
        root.destroy()
        chemistry()
    def fives():
        root.destroy()
        mother_tongue()
    def six():
        root.destroy()
        physic()
    def seven():
        root.destroy()
        biology()


    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(root,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(root, image=img)
    l2.place(x=30,y=30)
    btn = Button(root, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0)
    btn.place(x=500,y=50)
    btn2 = Button(root, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(root, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(root, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    l = Label(root, text='Courses',font=('Times', 17,'bold'),width=95, )
    l.place(x=0,y=250)

    img2 = Image.open('start/math.jpg').resize((200,200))
    img3= ImageTk.PhotoImage(img2)
    b1= Button(root,text='Math',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0,command=first)
    b1.place(x=90,y=500)
    l3= Label(root, image=img3)
    l3.place(x=30,y=300)

    img4 = Image.open('start/ang.jpg').resize((200,200))
    img5= ImageTk.PhotoImage(img4)
    b2= Button(root,text='English',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=second)
    b2.place(x=450,y=500)
    l4= Label(root, image=img5)
    l4.place(x=400,y=300)

    img6 = Image.open('start/IT.jpg').resize((200,200))
    img7= ImageTk.PhotoImage(img6)
    b3= Button(root,text='IT',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=third)
    b3.place(x=760,y=500)
    l5= Label(root, image=img7)
    l5.place(x=700,y=300)

    img8 = Image.open('start/kimyo.jpg').resize((200,200))
    img9= ImageTk.PhotoImage(img8)
    b4= Button(root,text='Chemistiry',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fourth)
    b4.place(x=1050,y=500)
    l6= Label(root, image=img9)
    l6.place(x=1000,y=300)

    img10 = Image.open('start/onatili.jpg').resize((200,200))
    img11= ImageTk.PhotoImage(img10)
    b5= Button(root,text='Mother tongue',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fives)
    b5.place(x=55,y=750)
    l7= Label(root, image=img11)
    l7.place(x=30,y=550)

    img12 = Image.open('start/fizika.jpg').resize((200,200))
    img13= ImageTk.PhotoImage(img12)
    b6= Button(root,text='Physics',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=six)
    b6.place(x=450,y=750)
    l8= Label(root, image=img13)
    l8.place(x=400,y=550)

    img14 = Image.open('start/biologiya.jpg').resize((200,200))
    img15= ImageTk.PhotoImage(img14)
    b7= Button(root,text='Biology',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=seven)
    b7.place(x=760,y=750)
    l9= Label(root, image=img15)
    l9.place(x=700,y=550)

    img16 = Image.open('start/img5.jpg').resize((200,200))
    img17= ImageTk.PhotoImage(img16)
    b7= Button(root,text='Another courses',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=next)
    b7.place(x=1020,y=750)
    l10= Label(root, image=img17)
    l10.place(x=1000,y=550)
    
    root.mainloop()

def pay1():
    pay = Tk()
    pay.geometry('1250x900')
    pay.configure(bg='ivory')
    def check():
        label = Label(pay, text='Payment approved!',font=('Times New Roman', 35, 'bold'), fg='green')
        label.place(x=80,y=650)
        next190.configure(bg='green')

        a = en1.get()
        b = en2.get()
        c = en3.get()
        d = en4.get()
        q = en5.get()
        p = spin.get()
        print(a,b,c,d,q,p)
        l = {
            'first name': a,
            'last name':b,
            'phone number':c,
            'amount of money to send':d,
            'card number':q,
            'group number':p
        }
    
        with open('pay.json','r') as a:
            d = json.load(a)
            
        d.append(l)

        with open('pay.json','w') as a:
            json.dump(
                d,a
            )

    def next2():
        pay.destroy()
        register()
    def menu():
        pay.destroy()
        start()
    
        pay1()
    def about_teachers():
        pay.destroy()
        about_teachers1()
    
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(pay,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(pay, image=img)
    l2.place(x=30,y=30)
    btn = Button(pay, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(pay, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0)
    btn2.place(x=650,y=50)
    btn3 = Button(pay, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(pay, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    lb1 = Label(pay, text="First and Last name",width=16,font=("bold", 15), bg='ivory')
    lb1.place(x=50,y=203)
    en1 = Entry(pay, width=50,bg='white',fg='black',font=('Arial',14,'bold'))
    en1.place(x=50,y=232)
    lb2 = Label(pay, text="Course name",width=10,font=("bold", 15), bg='ivory')
    lb2.place(x=50,y=263)
    en2 = Entry(pay, width=50,bg='white',fg='black',font=('Arial',14,'bold'))
    en2.place(x=50,y=292)
    lb3 = Label(pay, text="Phone number",width=13,font=("bold", 15), bg='ivory')
    lb3.place(x=40,y=323)
    en3 = Entry(pay, width=50,bg='white',fg='black',font=('Arial',14,'bold'))
    en3.place(x=50,y=352)
    lb4 = Label(pay, text="Amount of money to send",width=20,font=("bold", 15), bg='ivory')
    lb4.place(x=50,y=383)
    en4 = Entry(pay, width=50,bg='white',fg='black',font=('Arial',14,'bold'))
    en4.place(x=50,y=412)
    lb5 = Label(pay, text="Card number",width=10,font=("bold", 15), bg='ivory')
    lb5.place(x=50,y=443)
    en5 = Entry(pay, width=50,bg='white',fg='black',font=('Arial',14,'bold'))
    en5.place(x=50,y=472)

    sok = Button(pay,text='Group number', bd=0,font=("bold", 15), bg= 'ivory')
    sok.place(x=48, y=505)
    spin= Spinbox(pay, from_=0, to=10, width=7,bg='ivory', font=("bold", 13))
    spin.place(x=190,y=513)

    img6 = Image.open('pay.jpeg').resize((600,600))
    img7= ImageTk.PhotoImage(img6)
    l5= Label(pay, image=img7)
    l5.place(x=630,y=200)
    
    next190 = Button(pay, text='Next',width=5, height=2,command=check, bg='red')
    next190.place(x=500, y=550)

    pay.mainloop()

def about_teachers1():
    about_teachers = Tk()
    about_teachers.geometry('1250x900')
    about_teachers.configure(bg='ivory')
    def next():
        about_teachers.destroy()
        other_teachers()
    def next2():
        about_teachers.destroy()
        register()
    def menu():
        about_teachers.destroy()
        start()
        
    def pay():
        about_teachers.destroy()
        pay1()
    def first():
        about_teachers.destroy()
        math_teachers()
    def second():
        about_teachers.destroy()
        english_teachers()
    def third():
        about_teachers.destroy()
        it_teachers()
    def fourth():
        about_teachers.destroy()
        chemistry_teachers()
    def fives():
        about_teachers.destroy()
        mother_tongue_teachers()
    def six():
        about_teachers.destroy()
        physic_teachers()
    def seven():
        about_teachers.destroy()
        biology_teachers()


    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(about_teachers,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(about_teachers, image=img)
    l2.place(x=30,y=30)
    btn = Button(about_teachers, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(about_teachers, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(about_teachers, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, )
    btn3.place(x=800,y=50)
    btn4 = Button(about_teachers, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    l = Label(about_teachers, text='Teachers',font=('Times', 17,'bold'),width=95)
    l.place(x=0,y=250)


    img2 = Image.open('start/math.jpg').resize((200,200))
    img3= ImageTk.PhotoImage(img2)
    b1= Button(about_teachers,text='Math teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0,command=first)
    b1.place(x=50,y=500)
    l3= Label(about_teachers, image=img3)
    l3.place(x=30,y=300)

    img4 = Image.open('start/ang.jpg').resize((200,200))
    img5= ImageTk.PhotoImage(img4)
    b2= Button(about_teachers,text='English teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=second)
    b2.place(x=410,y=500)
    l4= Label(about_teachers, image=img5)
    l4.place(x=400,y=300)

    img6 = Image.open('start/IT.jpg').resize((200,200))
    img7= ImageTk.PhotoImage(img6)
    b3= Button(about_teachers,text='IT teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=third)
    b3.place(x=720,y=500)
    l5= Label(about_teachers, image=img7)
    l5.place(x=700,y=300)

    img8 = Image.open('start/kimyo.jpg').resize((200,200))
    img9= ImageTk.PhotoImage(img8)
    b4= Button(about_teachers,text='Chemistiry teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fourth)
    b4.place(x=1000,y=500)
    l6= Label(about_teachers, image=img9)
    l6.place(x=1000,y=300)

    img10 = Image.open('start/onatili.jpg').resize((200,200))
    img11= ImageTk.PhotoImage(img10)
    b5= Button(about_teachers,text='Mother tongue teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fives)
    b5.place(x=15,y=750)
    l7= Label(about_teachers, image=img11)
    l7.place(x=30,y=550)

    img12 = Image.open('start/fizika.jpg').resize((200,200))
    img13= ImageTk.PhotoImage(img12)
    b6= Button(about_teachers,text='Physics teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=six)
    b6.place(x=410,y=750)
    l8= Label(about_teachers, image=img13)
    l8.place(x=400,y=550)

    

    img14 = Image.open('start/biologiya.jpg').resize((200,200))
    img15= ImageTk.PhotoImage(img14)
    b7= Button(about_teachers,text='Biology teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=seven)
    b7.place(x=710,y=750)
    l9= Label(about_teachers, image=img15)
    l9.place(x=700,y=550)

    img16 = Image.open('start/img5.jpg').resize((200,200))
    img17= ImageTk.PhotoImage(img16)
    b7= Button(about_teachers,text='Other teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=next)
    b7.place(x=1030,y=750)
    l10= Label(about_teachers, image=img17)
    l10.place(x=1010,y=550)
    

    about_teachers.mainloop()

def other_teachers():
    root10 = Tk()
    root10.geometry('1250x900')
    root10.configure(bg='ivory')

    def next2():
        root10.destroy()
        register()
    def next3():
        root10.destroy()
        about_teachers1()
    def menu():
        root10.destroy()
        start()
    def pay():
        root10.destroy()
        pay1()
    def about_teachers():
        root10.destroy()
        about_teachers1()
    def first():
        root10.destroy()
        music_teachers()
    def second():
        root10.destroy()
        history_teachers()
    def third():
        root10.destroy()
        geometry_teachers()
    def fourth():
        root10.destroy()
        art_teachers()
    def fives():
        root10.destroy()
        geography_teachers()
    def six():
        root10.destroy()
        dance_teachers()
    def seven():
        root10.destroy()
        mental_arithmetic_teachers()
    def eight():
        root10.destroy()
        russian_teachers()


    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(root10,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(root10, image=img)
    l2.place(x=30,y=30)
    btn = Button(root10, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(root10, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(root10, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(root10, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    
    button=Button(root10,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    l = Label(root10, text='Courses',font=('Times', 17,'bold'),width=95)
    l.place(x=0,y=250)

    img2 = Image.open('musiqa.jpg').resize((200,200))
    img3= ImageTk.PhotoImage(img2)
    b1= Button(root10,text='Music teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=first)
    b1.place(x=55,y=500)
    l3= Label(root10, image=img3)
    l3.place(x=30,y=300)

    img4 = Image.open('tarix.jpg').resize((200,200))
    img5= ImageTk.PhotoImage(img4)
    b2= Button(root10,text='History teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=second)
    b2.place(x=420,y=500)
    l4= Label(root10, image=img5)
    l4.place(x=400,y=300)

    img6 = Image.open('geom.jpg').resize((200,200))
    img7= ImageTk.PhotoImage(img6)
    b3= Button(root10,text='Geometry teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=third)
    b3.place(x=700,y=500)
    l5= Label(root10, image=img7)
    l5.place(x=700,y=300)

    img8 = Image.open('rasm.jpg').resize((200,200))
    img9= ImageTk.PhotoImage(img8)
    b4= Button(root10,text='Art teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fourth)
    b4.place(x=1030,y=500)
    l6= Label(root10, image=img9)
    l6.place(x=1000,y=300)

    img10 = Image.open('geo.jpg').resize((200,200))
    img11= ImageTk.PhotoImage(img10)
    b5= Button(root10,text='Geography teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fives)
    b5.place(x=25,y=750)
    l7= Label(root10, image=img11)
    l7.place(x=30,y=550)

    img12 = Image.open('dance.webp').resize((200,200))
    img13= ImageTk.PhotoImage(img12)
    b6= Button(root10,text='Dance teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=six)
    b6.place(x=410,y=750)
    l8= Label(root10, image=img13)
    l8.place(x=400,y=550)
    
    

    img14 = Image.open('menar.jpg').resize((200,200))
    img15= ImageTk.PhotoImage(img14)
    b7= Button(root10,text='Mental Arithmetic teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=seven)
    b7.place(x=675,y=750)
    l9= Label(root10, image=img15)
    l9.place(x=700,y=550)

    img16 = Image.open('ruskiy.webp').resize((200,200))
    img17= ImageTk.PhotoImage(img16)
    b7= Button(root10,text='Russian teachers',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=eight)
    b7.place(x=1010,y=750)
    l10= Label(root10, image=img17)
    l10.place(x=1000,y=550)
    
    root10.mainloop()

def another_courses():
    root2 = Tk()
    root2.geometry('1250x900')
    root2.configure(bg='ivory')

    def next2():
        root2.destroy()
        register()
    def next3():
        root2.destroy()
        start()
    def menu():
        root2.destroy()
        start()
    def pay():
        root2.destroy()
        pay1()
    def about_teachers():
        root2.destroy()
        about_teachers1()
    def first():
        root2.destroy()
        music()
    def second():
        root2.destroy()
        history()
    def third():
        root2.destroy()
        geometry()
    def fourth():
        root2.destroy()
        art()
    def fives():
        root2.destroy()
        geography()
    def six():
        root2.destroy()
        dance()
    def seven():
        root2.destroy()
        mental_arithmetic()
    def eight():
        root2.destroy()
        russian()


    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(root2,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(root2, image=img)
    l2.place(x=30,y=30)
    btn = Button(root2, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(root2, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(root2, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(root2, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    
    button=Button(root2,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    l = Label(root2, text='Courses',font=('Times', 17,'bold'),width=95)
    l.place(x=0,y=250)

    img2 = Image.open('musiqa.jpg').resize((200,200))
    img3= ImageTk.PhotoImage(img2)
    b1= Button(root2,text='Music',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=first)
    b1.place(x=90,y=500)
    l3= Label(root2, image=img3)
    l3.place(x=30,y=300)

    img4 = Image.open('tarix.jpg').resize((200,200))
    img5= ImageTk.PhotoImage(img4)
    b2= Button(root2,text='History',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=second)
    b2.place(x=450,y=500)
    l4= Label(root2, image=img5)
    l4.place(x=400,y=300)

    img6 = Image.open('geom.jpg').resize((200,200))
    img7= ImageTk.PhotoImage(img6)
    b3= Button(root2,text='Geometry',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=third)
    b3.place(x=760,y=500)
    l5= Label(root2, image=img7)
    l5.place(x=700,y=300)

    img8 = Image.open('rasm.jpg').resize((200,200))
    img9= ImageTk.PhotoImage(img8)
    b4= Button(root2,text='Art',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fourth)
    b4.place(x=1050,y=500)
    l6= Label(root2, image=img9)
    l6.place(x=1000,y=300)

    img10 = Image.open('geo.jpg').resize((200,200))
    img11= ImageTk.PhotoImage(img10)
    b5= Button(root2,text='Geography',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=fives)
    b5.place(x=55,y=750)
    l7= Label(root2, image=img11)
    l7.place(x=30,y=550)

    img12 = Image.open('dance.webp').resize((200,200))
    img13= ImageTk.PhotoImage(img12)
    b6= Button(root2,text='Dance',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=six)
    b6.place(x=450,y=750)
    l8= Label(root2, image=img13)
    l8.place(x=400,y=550)

    img14 = Image.open('menar.jpg').resize((200,200))
    img15= ImageTk.PhotoImage(img14)
    b7= Button(root2,text='Mental Arithmetic',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=seven)
    b7.place(x=700,y=750)
    l9= Label(root2, image=img15)
    l9.place(x=700,y=550)

    img16 = Image.open('ruskiy.webp').resize((200,200))
    img17= ImageTk.PhotoImage(img16)
    b7= Button(root2,text='Russian',  font=('Times New Roman', 17, 'bold'),bg='ivory',activebackground='ivory', bd=0, command=eight)
    b7.place(x=1040,y=750)
    l10= Label(root2, image=img17)
    l10.place(x=1000,y=550)




    root2.mainloop()

def math():
    matem = Tk()
    matem.geometry('1250x900')
    matem.configure(bg='ivory')

    def next2():
        matem.destroy()
        register()
    def menu():
        matem.destroy()
        start()

    def pay():
        matem.destroy()
        pay1()
    def about_teachers():
        matem.destroy()
        about_teachers1()
    def next3():
        matem.destroy()
        start()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(matem,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(matem, image=img)
    l2.place(x=30,y=30)
    btn = Button(matem, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(matem, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(matem, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(matem, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    button=Button(matem,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("samarqand to'plami.webp").resize((400,400))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(matem, image=img3)
    l3.place(x=100, y=300)

    l4= Label(matem, text='Course: Math',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(matem, text="Course fee : 500.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(matem,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(matem, from_=7, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)

    l6= Label(matem, text="Book name: Samarqand to'plami",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(matem, text="Book price: 100.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)

    matem.mainloop()

def english():
    english = Tk()
    english.geometry('1250x900')
    english.configure(bg='ivory')
    def next2():
        english.destroy()
        register()
    def menu():
        english.destroy()
        start()
    def pay():
        english.destroy()
        pay1()
    def about_teachers():
        english.destroy()
        about_teachers1()
    def next3():
        english.destroy()
        start()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(english,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(english, image=img)
    l2.place(x=30,y=30)
    btn = Button(english, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(english, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(english, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(english, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    button=Button(english,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("solutions_third_edition.webp").resize((400,400))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(english, image=img3)
    l3.place(x=50, y=300)

    l4= Label(english, text='Course: Beginner',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=500,y=300)

    l5= Label(english, text="Course fee : 250.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=500,y=350)

    l6= Label(english, text="Course book : 90.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=500,y=390)

    l4= Label(english, text='Course: Elementary',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=500,y=450)

    l5= Label(english, text="Course fee : 300.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=500,y=490)

    l6= Label(english, text="Course book : 100.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=500,y=530)

    l7= Label(english, text='Course: Pre-Intermedite',  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=850,y=300)

    l8= Label(english, text="Course fee : 350.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l8.place(x=850,y=350)

    l9= Label(english, text="Course book : 120.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l9.place(x=850,y=390)

    l10= Label(english, text='Course: Intermedite',  font=('Times', 21, 'bold'),bg='ivory')
    l10.place(x=850,y=450)

    l11= Label(english, text="Course fee : 400.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l11.place(x=850,y=490)

    l12= Label(english, text="Course book : 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l12.place(x=850,y=530)

    l10= Label(english, text='Course: Upper-Intermedite',  font=('Times', 21, 'bold'),bg='ivory')
    l10.place(x=600,y=600)

    l11= Label(english, text="Course fee : 450.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l11.place(x=600,y=650)

    l12= Label(english, text="Course book : 190.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l12.place(x=600,y=690)

    b = Button(english,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=1000, y=720)
    spin= Spinbox(english, from_=0, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=1110,y=730)



    english.mainloop()

def it():
    it = Tk()
    it.geometry('1250x900')
    it.configure(bg='ivory')
    def next2():
        it.destroy()
        register()
    def menu():
        it.destroy()
        start()
    def pay():
        it.destroy()
        pay1()
    def about_teachers():
        it.destroy()
        about_teachers1()
    def next3():
        it.destroy()
        start()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(it,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(it, image=img)
    l2.place(x=30,y=30)
    btn = Button(it, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(it, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(it, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(it, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(it,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("noutbook.webp").resize((400,400))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(it, image=img3)
    l3.place(x=50, y=300)

    l4= Label(it, text='Course: Front-End',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=500,y=300)

    l5= Label(it, text="Course fee : 675.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=500,y=350)

    l6= Label(it, text="Course book : free",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=500,y=390)

    l4= Label(it, text='Course: Python',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=500,y=450)

    l5= Label(it, text="Course fee : 675.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=500,y=490)

    l6= Label(it, text="Course book : free",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=500,y=530)

    l7= Label(it, text='Course: Scratch',  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=850,y=300)

    l8= Label(it, text="Course fee : 450.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l8.place(x=850,y=350)

    l9= Label(it, text="Course book : free",  font=('Times', 21, 'bold'),bg='ivory')
    l9.place(x=850,y=390)

    l10= Label(it, text='Course: Foundation',  font=('Times', 21, 'bold'),bg='ivory')
    l10.place(x=850,y=450)

    l11= Label(it, text="Course fee : 1.100.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l11.place(x=850,y=490)

    l12= Label(it, text="Course book : free",  font=('Times', 21, 'bold'),bg='ivory')
    l12.place(x=850,y=530)

    l10= Label(it, text='Course: Back-End',  font=('Times', 21, 'bold'),bg='ivory')
    l10.place(x=600,y=600)

    l11= Label(it, text="Course fee : 1.500.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l11.place(x=600,y=650)

    l12= Label(it, text="Course book : free",  font=('Times', 21, 'bold'),bg='ivory')
    l12.place(x=600,y=690)

    b = Button(it,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=1000, y=720)
    spin= Spinbox(it, from_=0, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=1110,y=730)


    it.mainloop()

def chemistry():
    kimyo = Tk()
    kimyo.geometry('1250x900')
    kimyo.configure(bg='ivory')
    def next2():
        kimyo.destroy()
        register()
    def menu():
        kimyo.destroy()
        start()

    def pay():
        kimyo.destroy()
        pay1()
    def about_teachers():
        kimyo.destroy()
        about_teachers1()
    def next3():
        kimyo.destroy()
        start()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(kimyo,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(kimyo, image=img)
    l2.place(x=30,y=30)
    btn = Button(kimyo, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(kimyo, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(kimyo, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(kimyo, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(kimyo,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("kimyoktob.jpg").resize((400,500))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(kimyo, image=img3)
    l3.place(x=100, y=250)

    l4= Label(kimyo, text='Course: Chemistry',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(kimyo, text="Course fee : 500.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(kimyo,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(kimyo, from_=5, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)

    l6= Label(kimyo, text="Book name: Kimyo ",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(kimyo, text="Book price: 80.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)


    kimyo.mainloop()

def mother_tongue():
    onatili = Tk()
    onatili.geometry('1250x900')
    onatili.configure(bg='ivory')
    def next2():
        onatili.destroy()
        register()
    def menu():
        onatili.destroy()
        start()

    def pay():
        onatili.destroy()
        pay1()
    def about_teachers():
        onatili.destroy()
        about_teachers1()
    def next3():
        onatili.destroy()
        start()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(onatili,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(onatili, image=img)
    l2.place(x=30,y=30)
    btn = Button(onatili, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(onatili, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(onatili, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(onatili, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(onatili,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("onatilikitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(onatili, image=img3)
    l3.place(x=100, y=300)

    l4= Label(onatili, text='Course: Mother tongue',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(onatili, text="Course fee : 200.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(onatili,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(onatili, from_=0, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)

    l6= Label(onatili, text="Book name: Ona tili mukammal qo'llanma",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(onatili, text="Book price: 50.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)


    onatili.mainloop()

def physic():
    fizika = Tk()
    fizika.geometry('1250x900')
    fizika.configure(bg='ivory')
    def next2():
        fizika.destroy()
        register()
    def menu():
        fizika.destroy()
        start()

    def pay():
        fizika.destroy()
        pay1()
    def about_teachers():
        fizika.destroy()
        about_teachers1() 
    def next3():
        fizika.destroy()
        start()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(fizika,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(fizika, image=img)
    l2.place(x=30,y=30)
    btn = Button(fizika, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(fizika, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(fizika, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(fizika, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(fizika,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("fizikaktiob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(fizika, image=img3)
    l3.place(x=100, y=300)

    l4= Label(fizika, text='Course: Physic',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(fizika, text="Course fee : 400.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(fizika,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(fizika, from_=3, to=8, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)

    l6= Label(fizika, text="Book name: Samarqand to'plami",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(fizika, text="Book price: 90.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)


    fizika.mainloop()

def biology():
    biologiya = Tk()
    biologiya.geometry('1250x900')
    biologiya.configure(bg='ivory')
    def next2():
        biologiya.destroy()
        register()
    def menu():
        biologiya.destroy()
        start()

    def pay():
        biologiya.destroy()
        pay1()
    def about_teachers():
        biologiya.destroy()
        about_teachers1()
    def next3():
        biologiya.destroy()
        start()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(biologiya,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(biologiya, image=img)
    l2.place(x=30,y=30)
    btn = Button(biologiya, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(biologiya, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(biologiya, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(biologiya, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(biologiya,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("biokitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(biologiya, image=img3)
    l3.place(x=100, y=300)

    l4= Label(biologiya, text='Course: Biology',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(biologiya, text="Course fee : 250.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(biologiya,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(biologiya, from_=5, to=8, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)

    l6= Label(biologiya, text="Book name: Samarqand to'plami",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(biologiya, text="Book price: 40.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)


    biologiya.mainloop()

def music():
    musiqa = Tk()
    musiqa.geometry('1250x900')
    musiqa.configure(bg='ivory')
    def next2():
        musiqa.destroy()
        register()
    def menu():
        musiqa.destroy()
        start()

    def pay():
        musiqa.destroy()
        pay1()
    def about_teachers():
        musiqa.destroy()
        about_teachers1()
    def next3():
        musiqa.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(musiqa,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(musiqa, image=img)
    l2.place(x=30,y=30)
    btn = Button(musiqa, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(musiqa, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(musiqa, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(musiqa, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(musiqa,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("musiqakitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(musiqa, image=img3)
    l3.place(x=100, y=300)

    l4= Label(musiqa, text='Course: Music',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(musiqa, text="Course fee : 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l6= Label(musiqa, text="Book name: Musiqa tarixi",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(musiqa, text="Book price: 20.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)




    musiqa.mainloop()

def history():
    tarix = Tk()
    tarix.geometry('1250x900')
    tarix.configure(bg='ivory')
    def next2():
        tarix.destroy()
        register()
    def menu():
        tarix.destroy()
        start()

    def pay():
        tarix.destroy()
        pay1()
    def about_teachers():
        tarix.destroy()
        about_teachers1()
    def next3():
        tarix.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(tarix,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(tarix, image=img)
    l2.place(x=30,y=30)
    btn = Button(tarix, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(tarix, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(tarix, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(tarix, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(tarix,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("tarixkitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(tarix, image=img3)
    l3.place(x=100, y=300)

    l4= Label(tarix, text='Course: History',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(tarix, text="Course fee : 250.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l6= Label(tarix, text="Book name: Tarix",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(tarix, text="Book price: 50.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)



    tarix.mainloop()

def geometry():
    geometriya = Tk()
    geometriya.geometry('1250x900')
    geometriya.configure(bg='ivory')
    def next2():
        geometriya.destroy()
        register()
    def menu():
        geometriya.destroy()
        start()

    def pay():
        geometriya.destroy()
        pay1()
    def about_teachers():
        geometriya.destroy()
        about_teachers1()
    def next3():
        geometriya.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(geometriya,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(geometriya, image=img)
    l2.place(x=30,y=30)
    btn = Button(geometriya, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(geometriya, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(geometriya, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(geometriya, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(geometriya,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("geomkitob.webp").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(geometriya, image=img3)
    l3.place(x=100, y=300)

    l4= Label(geometriya, text='Course: Geometry',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(geometriya, text="Course fee : 350.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l6= Label(geometriya, text="Book name: Geometriya",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(geometriya, text="Book price: 90.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)



    geometriya.mainloop()

def art():
    rasm = Tk()
    rasm.geometry('1250x900')
    rasm.configure(bg='ivory')
    def next2():
        rasm.destroy()
        register()
    def menu():
        rasm.destroy()
        start()

    def pay():
        rasm.destroy()
        pay1()
    def about_teachers():
        rasm.destroy()
        about_teachers1()
    def next3():
        rasm.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(rasm,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(rasm, image=img)
    l2.place(x=30,y=30)
    btn = Button(rasm, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(rasm, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(rasm, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(rasm, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(rasm,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("qalamlar.jpeg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(rasm, image=img3)
    l3.place(x=100, y=300)

    l4= Label(rasm, text='Course: Art',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(rasm, text="Course fee : 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l7= Label(rasm, text="A collection og pencils price: 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=390)



    rasm.mainloop()

def geography():
    geografiya = Tk()
    geografiya.geometry('1250x900')
    geografiya.configure(bg='ivory')
    def next2():
        geografiya.destroy()
        register()
    def menu():
        geografiya.destroy()
        start()

    def pay():
        geografiya.destroy()
        pay1()
    def about_teachers():
        geografiya.destroy()
        about_teachers1()
    def next3():
        geografiya.destroy()
        another_courses()   
    button=Button(geografiya,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(geografiya,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(geografiya, image=img)
    l2.place(x=30,y=30)
    btn = Button(geografiya, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(geografiya, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(geografiya, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(geografiya, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    img2 = Image.open("geokitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(geografiya, image=img3)
    l3.place(x=100, y=300)

    l4= Label(geografiya, text='Course: Geography',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(geografiya, text="Course fee : 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l6= Label(geografiya, text="Book name: Geografiya savollar to'plami",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(geografiya, text="Book price: 80.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)



    geografiya.mainloop()

def dance():
    raqs = Tk()
    raqs.geometry('1250x900')
    raqs.configure(bg='ivory')
    def next2():
        raqs.destroy()
        register()
    def menu():
        raqs.destroy()
        start()

    def pay():
        raqs.destroy()
        pay1()
    def about_teachers():
        raqs.destroy()
        about_teachers1()
    def next3():
        raqs.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(raqs,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(raqs, image=img)
    l2.place(x=30,y=30)
    btn = Button(raqs, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(raqs, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(raqs, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(raqs, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(raqs,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("raqskiyimi.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(raqs, image=img3)
    l3.place(x=100, y=300)

    l4= Label(raqs, text='Course: Dance',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(raqs, text="Course fee : 200.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l7= Label(raqs, text="Dress price: 80.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=390)




    raqs.mainloop()

def mental_arithmetic():
    menar = Tk()
    menar.geometry('1250x900')
    menar.configure(bg='ivory')
    def next2():
        menar.destroy()
        register()
    def menu():
        menar.destroy()
        start()

    def pay():
        menar.destroy()
        pay1()
    def about_teachers():
        menar.destroy()
        about_teachers1()
    def next3():
        menar.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(menar,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(menar, image=img)
    l2.place(x=30,y=30)
    btn = Button(menar, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(menar, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(menar, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(menar, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(menar,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("menarkitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(menar, image=img3)
    l3.place(x=100, y=300)

    l4= Label(menar, text='Course: Mental arithmetic',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(menar, text="Course fee : 150.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    l6= Label(menar, text="Book name: Mental arifmetik",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(menar, text="Book price: 50.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)



    menar.mainloop()

def russian():

    rustili = Tk()
    rustili.geometry('1250x900')
    rustili.configure(bg='ivory')
    def next2():
        rustili.destroy()
        register()
    def menu():
        rustili.destroy()
        start()

    def pay():
        rustili.destroy()
        pay1()
    def about_teachers():
        rustili.destroy()
        about_teachers1()
    def next3():
        rustili.destroy()
        another_courses()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(rustili,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(rustili, image=img)
    l2.place(x=30,y=30)
    btn = Button(rustili, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(rustili, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(rustili, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(rustili, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(rustili,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open("rustilikitob.jpg").resize((400,450))
    img3= ImageTk.PhotoImage(img2)
    l3 = Label(rustili, image=img3)
    l3.place(x=100, y=300)

    l4= Label(rustili, text='Course: Russian',  font=('Times', 21, 'bold'),bg='ivory')
    l4.place(x=700,y=300)

    l5= Label(rustili, text="Course fee : 250.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l5.place(x=700,y=350)

    b = Button(rustili,text='Group', bd=0,font=('Times', 21, 'bold'), bg= 'ivory', fg='black')
    b.place(x=695, y=390)
    spin= Spinbox(rustili, from_=0, to=10, width=5,bg='ivory', font=('Times', 21, 'bold'))
    spin.place(x=810,y=400)


    l6= Label(rustili, text="Book name: Rustilining amaliy grammatikasi",  font=('Times', 21, 'bold'),bg='ivory')
    l6.place(x=700,y=450)

    l7= Label(rustili, text="Book price: 30.000soums",  font=('Times', 21, 'bold'),bg='ivory')
    l7.place(x=700,y=500)



    rustili.mainloop()

def math_teachers():
    matemoqituvchi = Tk()
    matemoqituvchi.geometry('1250x900')
    matemoqituvchi.configure(bg='ivory')

    def next2():
        matemoqituvchi.destroy()
        register()
    def menu():
        matemoqituvchi.destroy()
        start()

    def pay():
        matemoqituvchi.destroy()
        pay1()
    def about_teachers():
        matemoqituvchi.destroy()
        about_teachers1()
    def next3():
        matemoqituvchi.destroy()
        about_teachers1()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(matemoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(matemoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(matemoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(matemoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(matemoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(matemoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    button=Button(matemoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('mathteacher.webp').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(matemoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(matemoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(matemoqituvchi, text='Name: Akram',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(matemoqituvchi, text='Surname: Ashurov',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(matemoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(matemoqituvchi, text='IELTS: 6.5',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(matemoqituvchi, text='Rating: 7.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(matemoqituvchi, text='Groups: 1, 3, 5, 6, 7',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('mathteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(matemoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(matemoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(matemoqituvchi, text='Name: Shaxlo',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(matemoqituvchi, text='Surname: Rustamova',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(matemoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(matemoqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(matemoqituvchi, text='Rating: 6.0 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(matemoqituvchi, text='Groups: 2, 4, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)


    matemoqituvchi.mainloop()

def english_teachers():
    inglizoqituvchi = Tk()
    inglizoqituvchi.geometry('1250x900')
    inglizoqituvchi.configure(bg='ivory')
    def next2():
        inglizoqituvchi.destroy()
        register()
    def menu():
        inglizoqituvchi.destroy()
        start()
    def pay():
        inglizoqituvchi.destroy()
        pay1()
    def about_teachers():
        inglizoqituvchi.destroy()
        about_teachers1()
    def next3():
        inglizoqituvchi.destroy()
        about_teachers1()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(inglizoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(inglizoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(inglizoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(inglizoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(inglizoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(inglizoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)

    button=Button(inglizoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('englishteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(inglizoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(inglizoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(inglizoqituvchi, text='Name: Nodira',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(inglizoqituvchi, text='Surname: Ashurova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(inglizoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(inglizoqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(inglizoqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(inglizoqituvchi, text='Groups: 1, 2, 3, 4, 5',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('englishteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(inglizoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(inglizoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(inglizoqituvchi, text='Name: Natalya',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(inglizoqituvchi, text='Surname: Ibragimovna',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(inglizoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(inglizoqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(inglizoqituvchi, text='Rating: 7.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(inglizoqituvchi, text='Groups: 6, 7, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)



    inglizoqituvchi.mainloop()

def it_teachers():
    itoqituvchi = Tk()
    itoqituvchi.geometry('1250x900')
    itoqituvchi.configure(bg='ivory')
    def next2():
        itoqituvchi.destroy()
        register()
    def menu():
        itoqituvchi.destroy()
        start()
    def pay():
        itoqituvchi.destroy()
        pay1()
    def about_teachers():
        itoqituvchi.destroy()
        about_teachers1()
    def next3():
        itoqituvchi.destroy()
        about_teachers1()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(itoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(itoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(itoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(itoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(itoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(itoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(itoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('itteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(itoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(itoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(itoqituvchi, text='Name: Asadbek',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(itoqituvchi, text='Surname: Komilov',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(itoqituvchi, text='Language: English, Russian ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(itoqituvchi, text='IELTS: 6.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(itoqituvchi, text='Rating: 5.5 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(itoqituvchi, text='Groups: 1, 2, 3, 4, 5',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('itteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(itoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(itoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(itoqituvchi, text='Name: Shoxrux',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(itoqituvchi, text='Surname: Mirzatillayev',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(itoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(itoqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(itoqituvchi, text='Rating: 6.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(itoqituvchi, text='Groups: 6, 7, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)




    itoqituvchi.mainloop()

def chemistry_teachers():
    kimyooqituvchi = Tk()
    kimyooqituvchi.geometry('1250x900')
    kimyooqituvchi.configure(bg='ivory')
    def next2():
        kimyooqituvchi.destroy()
        register()
    def menu():
        kimyooqituvchi.destroy()
        start()

    def pay():
        kimyooqituvchi.destroy()
        pay1()
    def about_teachers():
        kimyooqituvchi.destroy()
        about_teachers1()
    def next3():
        kimyooqituvchi.destroy()
        about_teachers1()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(kimyooqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(kimyooqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(kimyooqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(kimyooqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(kimyooqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(kimyooqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(kimyooqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('chemistryteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(kimyooqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(kimyooqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(kimyooqituvchi, text='Name: Galina',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(kimyooqituvchi, text='Surname: Vladimirovna',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(kimyooqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(kimyooqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(kimyooqituvchi, text='Rating: 9.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(kimyooqituvchi, text='Groups: 1, 2, 3, 4, 5',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('chemsitryteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(kimyooqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(kimyooqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(kimyooqituvchi, text='Name: Murod',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(kimyooqituvchi, text='Surname: Shamsiyev',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(kimyooqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(kimyooqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(kimyooqituvchi, text='Rating: 7.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(kimyooqituvchi, text='Groups: 6, 7, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)



    kimyooqituvchi.mainloop()

def mother_tongue_teachers():
    onatilioqituvchi = Tk()
    onatilioqituvchi.geometry('1250x900')
    onatilioqituvchi.configure(bg='ivory')
    def next2():
        onatilioqituvchi.destroy()
        register()
    def menu():
        onatilioqituvchi.destroy()
        start()

    def pay():
        onatilioqituvchi.destroy()
        pay1()
    def about_teachers():
        onatilioqituvchi.destroy()
        about_teachers1()
    def next3():
        onatilioqituvchi.destroy()
        about_teachers1()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(onatilioqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(onatilioqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(onatilioqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(onatilioqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(onatilioqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(onatilioqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(onatilioqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('onatilioqituvchi.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(onatilioqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(onatilioqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(onatilioqituvchi, text='Name: Ozoda',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(onatilioqituvchi, text='Surname: Gafforova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(onatilioqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(onatilioqituvchi, text='IELTS: 6.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(onatilioqituvchi, text='Rating: 6.5 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(onatilioqituvchi, text='Groups: 1, 2, 3, 4, 5',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('onatilioqituvchi2.webp').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(onatilioqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(onatilioqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(onatilioqituvchi, text='Name: Amina',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(onatilioqituvchi, text='Surname: Umarova',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(onatilioqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(onatilioqituvchi, text='IELTS: 6.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(onatilioqituvchi, text='Rating: 5.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(onatilioqituvchi, text='Groups: 6, 7, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)



    onatilioqituvchi.mainloop()

def physic_teachers():
    fizikaoqituvchi = Tk()
    fizikaoqituvchi.geometry('1250x900')
    fizikaoqituvchi.configure(bg='ivory')
    def next2():
        fizikaoqituvchi.destroy()
        register()
    def menu():
        fizikaoqituvchi.destroy()
        start()

    def pay():
        fizikaoqituvchi.destroy()
        pay1()
    def about_teachers():
        fizikaoqituvchi.destroy()
        about_teachers1() 
    def next3():
        fizikaoqituvchi.destroy()
        about_teachers1()

    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(fizikaoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(fizikaoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(fizikaoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(fizikaoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(fizikaoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(fizikaoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(fizikaoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('fizik.webp').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(fizikaoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(fizikaoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(fizikaoqituvchi, text='Name: Komil',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(fizikaoqituvchi, text='Surname: Murodov',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(fizikaoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(fizikaoqituvchi, text='IELTS: 6.5',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(fizikaoqituvchi, text='Rating: .5 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(fizikaoqituvchi, text='Groups: 1, 2, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('fizik2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(fizikaoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(fizikaoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(fizikaoqituvchi, text='Name: Asal',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(fizikaoqituvchi, text='Surname: Nigmatova',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(fizikaoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(fizikaoqituvchi, text='IELTS: 8.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(fizikaoqituvchi, text='Rating: 9.0 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(fizikaoqituvchi, text='Groups: 3, 4, 5, 6, 7, 8',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)

    
    fizikaoqituvchi.mainloop()

def biology_teachers():
    biologiyaoqituvchi = Tk()
    biologiyaoqituvchi.geometry('1250x900')
    biologiyaoqituvchi.configure(bg='ivory')
    def next2():
        biologiyaoqituvchi.destroy()
        register()
    def menu():
        biologiyaoqituvchi.destroy()
        start()

    def pay():
        biologiyaoqituvchi.destroy()
        pay1()
    def about_teachers():
        biologiyaoqituvchi.destroy()
        about_teachers1()
    def next3():
        biologiyaoqituvchi.destroy()
        about_teachers1()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(biologiyaoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(biologiyaoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(biologiyaoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(biologiyaoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(biologiyaoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(biologiyaoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(biologiyaoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)

    img2 = Image.open('biologyteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(biologiyaoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(biologiyaoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(biologiyaoqituvchi, text='Name: Ozoda',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(biologiyaoqituvchi, text='Surname: Ergashova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(biologiyaoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(biologiyaoqituvchi, text='IELTS: 5.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(biologiyaoqituvchi, text='Rating: 4.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(biologiyaoqituvchi, text='Groups: 5, 6, 7, 8',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('biologyteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(biologiyaoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(biologiyaoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(biologiyaoqituvchi, text='Name: Kamila',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(biologiyaoqituvchi, text='Surname: Umarova',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(biologiyaoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(biologiyaoqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(biologiyaoqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(biologiyaoqituvchi, text='Groups: 1, 2, 3, 4, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)


    biologiyaoqituvchi.mainloop()

def music_teachers():
    musiqaoqituvci = Tk()
    musiqaoqituvci.geometry('1250x900')
    musiqaoqituvci.configure(bg='ivory')
    def next2():
        musiqaoqituvci.destroy()
        register()
    def menu():
        musiqaoqituvci.destroy()
        start()

    def pay():
        musiqaoqituvci.destroy()
        pay1()
    def about_teachers():
        musiqaoqituvci.destroy()
        about_teachers1()
    def next3():
        musiqaoqituvci.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(musiqaoqituvci,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(musiqaoqituvci, image=img)
    l2.place(x=30,y=30)
    btn = Button(musiqaoqituvci, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(musiqaoqituvci, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(musiqaoqituvci, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(musiqaoqituvci, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(musiqaoqituvci,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('musicteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(musiqaoqituvci, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(musiqaoqituvci, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(musiqaoqituvci, text='Name: Dilfuza',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(musiqaoqituvci, text="Surname: Ziyoxo'jayeva",font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(musiqaoqituvci, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(musiqaoqituvci, text='IELTS: 6.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(musiqaoqituvci, text='Rating: 7.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    img4 = Image.open('musicteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(musiqaoqituvci, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(musiqaoqituvci, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(musiqaoqituvci, text='Name: Umar',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(musiqaoqituvci, text='Surname: Shamsiddinov',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(musiqaoqituvci, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(musiqaoqituvci, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(musiqaoqituvci, text='Rating: 7.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)


    musiqaoqituvci.mainloop()

def history_teachers():
    tarixoqituvchi = Tk()
    tarixoqituvchi.geometry('1250x900')
    tarixoqituvchi.configure(bg='ivory')
    def next2():
        tarixoqituvchi.destroy()
        register()
    def menu():
        tarixoqituvchi.destroy()
        start()

    def pay():
        tarixoqituvchi.destroy()
        pay1()
    def about_teachers():
        tarixoqituvchi.destroy()
        about_teachers1()
    def next3():
        tarixoqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(tarixoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(tarixoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(tarixoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(tarixoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(tarixoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(tarixoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(tarixoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('historyteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(tarixoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(tarixoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(tarixoqituvchi, text='Name: Malika',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(tarixoqituvchi, text='Surname: Akbaraliyevna',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(tarixoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(tarixoqituvchi, text='IELTS: 6.5',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(tarixoqituvchi, text='Rating: 5.5 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    img4 = Image.open('historyteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(tarixoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(tarixoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(tarixoqituvchi, text='Name: Jamila',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(tarixoqituvchi, text='Surname: Akbarovna',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(tarixoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(tarixoqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(tarixoqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)


    tarixoqituvchi.mainloop()

def geometry_teachers():
    geomoqituvchi = Tk()
    geomoqituvchi.geometry('1250x900')
    geomoqituvchi.configure(bg='ivory')
    def next2():
        geomoqituvchi.destroy()
        register()
    def menu():
        geomoqituvchi.destroy()
        start()

    def pay():
        geomoqituvchi.destroy()
        pay1()
    def about_teachers():
        geomoqituvchi.destroy()
        about_teachers1()
    def next3():
        geomoqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(geomoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(geomoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(geomoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(geomoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(geomoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(geomoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(geomoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('geometryteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(geomoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(geomoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(geomoqituvchi, text='Name: Fotima',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(geomoqituvchi, text='Surname: Xolmurodova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(geomoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(geomoqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(geomoqituvchi, text='Rating: 7.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    img4 = Image.open('geometryteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(geomoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(geomoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(geomoqituvchi, text='Name: Anastasiya',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(geomoqituvchi, text='Surname: Bernadovna',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(geomoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(geomoqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(geomoqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)

    geomoqituvchi.mainloop()

def art_teachers():
    rasmoqituvchi = Tk()
    rasmoqituvchi.geometry('1250x900')
    rasmoqituvchi.configure(bg='ivory')
    def next2():
        rasmoqituvchi.destroy()
        register()
    def menu():
        rasmoqituvchi.destroy()
        start()

    def pay():
        rasmoqituvchi.destroy()
        pay1()
    def about_teachers():
        rasmoqituvchi.destroy()
        about_teachers1()
    def next3():
        rasmoqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(rasmoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(rasmoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(rasmoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(rasmoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(rasmoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(rasmoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(rasmoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('artteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(rasmoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(rasmoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(rasmoqituvchi, text='Name: Shaxnoza',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(rasmoqituvchi, text='Surname: Karimova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(rasmoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(rasmoqituvchi, text='IELTS: 6.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(rasmoqituvchi, text='Rating: 7.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    img4 = Image.open('artteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(rasmoqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(rasmoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(rasmoqituvchi, text='Name: Safiya',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(rasmoqituvchi, text='Surname: Ruslanova',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(rasmoqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(rasmoqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(rasmoqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)


    rasmoqituvchi.mainloop()

def geography_teachers():
    geooqituvhci = Tk()
    geooqituvhci.geometry('1250x900')
    geooqituvhci.configure(bg='ivory')
    def next2():
        geooqituvhci.destroy()
        register()
    def menu():
        geooqituvhci.destroy()
        other_teachers()

    def pay():
        geooqituvhci.destroy()
        pay1()
    def about_teachers():
        geooqituvhci.destroy()
        about_teachers1()
    def next3():
        geooqituvhci.destroy()
        other_teachers() 
    button=Button(geooqituvhci,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(geooqituvhci,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(geooqituvhci, image=img)
    l2.place(x=30,y=30)
    btn = Button(geooqituvhci, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(geooqituvhci, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(geooqituvhci, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(geooqituvhci, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)


    img2 = Image.open('geoteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(geooqituvhci, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(geooqituvhci, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(geooqituvhci, text='Name: Xolida',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(geooqituvhci, text='Surname: Alimova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(geooqituvhci, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(geooqituvhci, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(geooqituvhci, text='Rating: 8.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    img4 = Image.open('geoteahcer2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(geooqituvhci, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(geooqituvhci, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(geooqituvhci, text='Name: Karim',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(geooqituvhci, text='Surname: Aliyev',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(geooqituvhci, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(geooqituvhci, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(geooqituvhci, text='Rating: 6.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)


    geooqituvhci.mainloop()

def dance_teachers():
    raqsoqituvchi = Tk()
    raqsoqituvchi.geometry('1250x900')
    raqsoqituvchi.configure(bg='ivory')
    def next2():
        raqsoqituvchi.destroy()
        register()
    def menu():
        raqsoqituvchi.destroy()
        start()

    def pay():
        raqsoqituvchi.destroy()
        pay1()
    def about_teachers():
        raqsoqituvchi.destroy()
        about_teachers1()
    def next3():
        raqsoqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(raqsoqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(raqsoqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(raqsoqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(raqsoqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(raqsoqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(raqsoqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(raqsoqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('danceteacher.png').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(raqsoqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(raqsoqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(raqsoqituvchi, text='Name: Zilola',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(raqsoqituvchi, text='Surname: Rasulova',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(raqsoqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(raqsoqituvchi, text='IELTS: 8.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(raqsoqituvchi, text='Rating: 7.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)

    raqsoqituvchi.mainloop()

def mental_arithmetic_teachers():
    menaroqituvchi = Tk()
    menaroqituvchi.geometry('1250x900')
    menaroqituvchi.configure(bg='ivory')
    def next2():
        menaroqituvchi.destroy()
        register()
    def menu():
        menaroqituvchi.destroy()
        start()

    def pay():
        menaroqituvchi.destroy()
        pay1()
    def about_teachers():
        menaroqituvchi.destroy()
        about_teachers1()
    def next3():
        menaroqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(menaroqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(menaroqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(menaroqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(menaroqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(menaroqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(menaroqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(menaroqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('menarteacher.jpg').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(menaroqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(menaroqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(menaroqituvchi, text='Name: Sabina',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(menaroqituvchi, text='Surname: Abdullayeva',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(menaroqituvchi, text='Language: Uzbek, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(menaroqituvchi, text='IELTS: 8.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(menaroqituvchi, text='Rating: 10.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)


    menaroqituvchi.mainloop()

def russian_teachers(): 
    rustilioqituvchi = Tk()
    rustilioqituvchi.geometry('1250x900')
    rustilioqituvchi.configure(bg='ivory')
    def next2():
        rustilioqituvchi.destroy()
        register()
    def menu():
        rustilioqituvchi.destroy()
        start()
        
    def pay():
        rustilioqituvchi.destroy()
        pay1()
    def about_teachers():
        rustilioqituvchi.destroy()
        about_teachers1()
    def next3():
        rustilioqituvchi.destroy()
        other_teachers()
    img1 = Image.open('image2.jpg').resize((100,100))
    img= ImageTk.PhotoImage(img1)
    l1= Label(rustilioqituvchi,text='''Kids
            Education''',  font=('Times New Roman', 21, 'bold'),bg='ivory')
    l1.place(x=100,y=50)
    l2= Label(rustilioqituvchi, image=img)
    l2.place(x=30,y=30)
    btn = Button(rustilioqituvchi, text='Menu', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=menu)
    btn.place(x=500,y=50)
    btn2 = Button(rustilioqituvchi, text='Pay', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory', bd=0, command=pay)
    btn2.place(x=650,y=50)
    btn3 = Button(rustilioqituvchi, text='About teachers', font=('Times', 17,'bold'), width=11,height=2,bg='ivory',activebackground='ivory',bd=0, command=about_teachers)
    btn3.place(x=800,y=50)
    btn4 = Button(rustilioqituvchi, text='Register', font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next2)
    btn4.place(x=1000,y=50)
    button=Button(rustilioqituvchi,text='previous',font=('Times', 17,'bold'), width=6,height=2,bg='ivory',activebackground='ivory',bd=0, command=next3 )
    button.place(x=0,y=200)


    img2 = Image.open('russianteacher.webp').resize((350,300))
    img3 = ImageTk.PhotoImage(img2)
    lb = Label(rustilioqituvchi, image=img3)
    lb.place(x=50,y=300)

    lb1 = Label(rustilioqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb1.place(x=420,y=310)
    lb2 = Label(rustilioqituvchi, text='Name: Anastasiya',font=('Times', 15,'bold'))
    lb2.place(x=420,y=350)
    lb3 = Label(rustilioqituvchi, text='Surname: Sergeyevna',font=('Times', 15,'bold'))
    lb3.place(x=420,y=390)
    lb4 = Label(rustilioqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb4.place(x=420,y=430)
    lb5 = Label(rustilioqituvchi, text='IELTS: 7.0',font=('Times', 15,'bold'))
    lb5.place(x=420,y=470)
    lb6 = Label(rustilioqituvchi, text='Rating: 8.0 ',font=('Times', 15,'bold'))
    lb6.place(x=420,y=510)
    lb0 = Label(rustilioqituvchi, text='Groups: 1, 2, 3, 4, 5',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb0.place(x=50,y=750)

    img4 = Image.open('russianteacher2.jpg').resize((300,300))
    img5 = ImageTk.PhotoImage(img4)
    lb = Label(rustilioqituvchi, image=img5)
    lb.place(x=670,y=300)

    lb7 = Label(rustilioqituvchi, text='Information about teacher: ',font=('Times', 15,'bold'))
    lb7.place(x=990,y=310)
    lb8 = Label(rustilioqituvchi, text='Name: Feruza',font=('Times', 15,'bold'))
    lb8.place(x=990,y=350)
    lb9 = Label(rustilioqituvchi, text='Surname: Turgunbayevna',font=('Times', 15,'bold'))
    lb9.place(x=990,y=390)
    lb10 = Label(rustilioqituvchi, text='Language: Russian, English ',font=('Times', 15,'bold'))
    lb10.place(x=990,y=430)
    lb11 = Label(rustilioqituvchi, text='IELTS: 7.5',font=('Times', 15,'bold'))
    lb11.place(x=990,y=470)
    lb12= Label(rustilioqituvchi, text='Rating: 8.5 ',font=('Times', 15,'bold'))
    lb12.place(x=990,y=510)
    lb = Label(rustilioqituvchi, text='Groups: 6, 7, 8, 9, 10',font=('Times', 27,'bold'), bg='ivory', fg='green')
    lb.place(x=670,y=750)



    rustilioqituvchi.mainloop()
  
start() 