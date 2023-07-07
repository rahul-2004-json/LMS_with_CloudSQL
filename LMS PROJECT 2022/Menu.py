 
from tkinter import*
import tkinter as tk
from tkinter import ttk
from turtle import width
from tkinter import Canvas
from tkinter import messagebox
import mysql.connector as sqltor
import tkinter






def loginpage():

    root.withdraw()

    global BackgroundImage, loginButtonImage, loginButton
    top=Toplevel()
    top.title("Library Management System")
    user_name= StringVar()
    pass_word= StringVar()


    # Variables

    top.geometry("700x700")
    top.resizable(0,0)

    BackgroundImage=PhotoImage(file="login.png")
    Backgroundimagelabel=Label(top,image=BackgroundImage).place(x=0,y=0)

    canvas=Canvas(top,width=400,height=400).place(x=150,y=150)
    title=Label(top,text="Library Management System",font=("times new roman",20,"bold"),fg='green').place(x=180,y=170)  
    titlelogin=Label(top,text="Admin",font=("times new roman",20,"bold")).place(x=310,y=240) 
    usernamelabel=Label(top,text="User in SQL:",font=("times new roman",16,"bold")).place(x=180,y=305)
    passwordlabel=Label(top,text="Password:",font=("times new roman",16,"bold")).place(x=180,y=355)

    def check():
        global mycon, mycursor
        user_name = str(txtusername.get())
        pass_word = str(txtpassword.get())
        
        mycon=sqltor.connect(host="bvpx0klusnhyh5fmcpum-mysql.services.clever-cloud.com", port= '3306', user= user_name, passwd= pass_word, database="bvpx0klusnhyh5fmcpum")

        if mycon.is_connected():
            print("SUCESSFULLY CONNECTED TO THE DATABASE...")
            mycursor=mycon.cursor()
            top.destroy()
            root.deiconify()
        
        else:
            print('lol it didnt connect')
            tk.messagebox.showinfo("Invalid User or Password")

    #Entries of user 
    txtusername=Entry(top,font=("times new roman",15),textvariable=user_name,width=18)
    txtusername.place(x=330,y=305)
    txtpassword=Entry(top,font=("times new roman",15),textvariable=pass_word,width=18)
    txtpassword.place(x=330,y=355)
    loginButtonImage=PhotoImage(file="loginbutton.png")
    loginButton=Button(top,image=loginButtonImage,border=0, command =lambda: [check()]).place(x=320,y=410)


def registration_button():
    
    global BackgroundImageregister,registerationlogo, mycursor

    top=Toplevel()
    top.title("Registeration")
    top.geometry("700x700")
    top.resizable(0,0)

    ######################################### VARIABLES VALUES ############################################################
    admin_no= StringVar()
    s_name= StringVar()
    Class= StringVar()
    mob_no= StringVar()

    BackgroundImageregister=PhotoImage(file="registerbg.png")
    registerimagelabel=Label(top,image=BackgroundImageregister).place(x=0,y=0)

    registerationlogo=PhotoImage(file="registerationlogo.png")
    registerationimagelabel=Label(top,image=registerationlogo).place(x=285,y=20)
    

    canvas_register=Canvas(top,width=400,height=430).place(x=150,y=160)

    

    ############# Labeling ##################
    titleregister=Label(top,text="Register",font=("times new roman",20,"bold"),fg='black').place(x=300,y=170)
    lbladmin_no=Label(top,text="Admission ID",font=("times new roman",17,"bold")).place(x=180,y=250)
    lbls_name=Label(top,text="Student Name",font=("times new roman",17,"bold")).place(x=180,y=300)
    lblclass=Label(top,text="Class",font=("times new roman",17,"bold")).place(x=180,y=350)
    lblmob_no=Label(top,text="Mobile Number",font=("times new roman",17,"bold")).place(x=180,y=400)

    ############ Entries #####################
    txtadmin_no=Entry(top,font=("times new roman",15),textvariable=admin_no,width=18)
    txtadmin_no.place(x=350,y=250) 
    txts_name=Entry(top,font=("times new roman",15),textvariable=s_name,width=18)
    txts_name.place(x=350,y=300)
    txtclass=Entry(top,font=("times new roman",15),textvariable=Class,width=18)
    txtclass.place(x=350,y=350)
    txtmob_no=Entry(top,font=("times new roman",15),textvariable=mob_no,width=18)
    txtmob_no.place(x=350,y=400)
    ############ SQL CODE ########################
    def registration(): #for regestring a student
        admin_no= txtadmin_no.get()
        s_name=txts_name.get()
        Class= txtclass.get()
        mob_no=  txtmob_no.get()   
        global mycursor
        command='insert into students values(%s,%s,%s,%s);'
        values=(admin_no,s_name,Class,mob_no)
        mycursor.execute(command,values)
        mycon.commit() 
        messagebox.showinfo("Success","Details Entered Successfully")
        

    btnAddDetails=Button(top,text="Register",font=("arial",12,"bold"),width=10,bg="blue",fg="white",padx=10, command = lambda: [registration(), txtadmin_no.delete(0,'end'), txts_name.delete(0,'end'), txtclass.delete(0,'end'), txtmob_no.delete(0,'end')]).place(x=400,y=530)# add command in this button
    Homebtn=Button(top,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10, command = lambda: [top.destroy(), root.deiconify()]).place(x=180,y=530) 


def addbook_button():
    
    global BackgroundImageaddbook,addbooklogo

    top=Toplevel()
    top.title("Library Management System")
    top.geometry("700x700")
    top.resizable(0,0)

    ######################################### VARIABLES VALUES ############################################################
    book_id=  StringVar()
    book_name=  StringVar()
    author_name= StringVar()
    genre= StringVar()
    book_desc= StringVar()

    ############ Background Image ####################################
    BackgroundImageaddbook=PhotoImage(file="addbooksbg.png")
    addbookimagelabel=Label(top,image=BackgroundImageaddbook).place(x=0,y=0)

    addbooklogo=PhotoImage(file="addbooklogo.png")
    addbookimagelabel=Label(top,image=addbooklogo).place(x=285,y=20)
    



    ############# Canvas ###################
    canvas_addbook=Canvas(top,width=400,height=430).place(x=160,y=160)

    ############# Labeling ##################
    titleaddbook=Label(top,text="Add Book",font=("times new roman",20,"bold"),fg='black').place(x=300,y=180) 
    lblbook_id=Label(top,text="Book Id",font=("times new roman",17,"bold")).place(x=180,y=250)
    lblbook_name=Label(top,text="Book Name",font=("times new roman",17,"bold")).place(x=180,y=300)
    lblauthor=Label(top,text="Author",font=("times new roman",17,"bold")).place(x=180,y=350)
    lblgenre=Label(top,text="Genre",font=("times new roman",17,"bold")).place(x=180,y=400)
    lblbook_desc=Label(top,text="Book Description",font=("times new roman",17,"bold")).place(x=180,y=450)  

    ############ Entries #####################
    txtbook_id=Entry(top,font=("times new roman",15,"bold"),textvariable=book_id,width=18)
    txtbook_id.place(x=365,y=250)
    txtbook_name=Entry(top,font=("times new roman",15,"bold"),textvariable=book_name,width=18)
    txtbook_name.place(x=365,y=300)
    txtauthor=Entry(top,font=("times new roman",15,"bold"),textvariable=author_name,width=18)
    txtauthor.place(x=365,y=350)   
    txtgenre=Entry(top,font=("times new roman",15,"bold"),textvariable=genre,width=18)
    txtgenre.place(x=365,y=400)
    txtbook_desc=Entry(top,font=("times new roman",15,"bold"),textvariable=book_desc,width=18)
    txtbook_desc.place(x=365,y=450)
    ################ SQL Code ##################
    def add_book(): #for adding a book
        book_id=txtbook_id.get()
        book_name=txtbook_name.get()
        author_name=txtauthor.get()
        genre=txtgenre.get()
        book_desc=txtbook_desc.get()
        global mycursor
        command='insert into books(book_id,book_name,author,genre,book_desc) values(%s,%s,%s,%s,%s);'
        values=(book_id,book_name,author_name,genre,book_desc)
        mycursor.execute(command,values)
        mycon.commit()
        messagebox.showinfo("Success","Book Added Successfully")

    ############ Buttons ######################
    btnAddBook=Button(top,text="Add Book",font=("arial",12,"bold"),width=10,bg="blue",fg="white",padx=10,command = lambda: [add_book(), txtbook_id.delete(0,'end'), txtbook_desc.delete(0,'end'), txtbook_name.delete(0,'end'),txtgenre.delete(0,'end'), txtauthor.delete(0,'end') ]).place(x=415,y=540) # add command in this button 
    Homebtn=Button(top,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10, command = lambda: [top.destroy(), root.deiconify()]).place(x=180,y=540)

    
def addrecord_button():
    
    global BackgroundImageaddrecord, addrecordlogo

    t=Toplevel()
    t.title("Library Management System")
    t.geometry("700x700")
    t.resizable(0,0)

    ######################################### VARIABLES VALUES ############################################################
    bk_id= StringVar()
    issued_by= StringVar()
    issued_on=  StringVar()


    ############ Background Image ####################################
    BackgroundImageaddrecord=PhotoImage(file="addrecordbg.png")
    addrecordimagelabel=Label(t,image=BackgroundImageaddrecord).place(x=0,y=0)
    
    addrecordlogo=PhotoImage(file="addrecordlogo.png")
    addrecordimagelabel=Label(t,image=addrecordlogo).place(x=285,y=20)

    ############# Canvas ###################
    canvas_addrecord=Canvas(t,width=400,height=350).place(x=160,y=170)

    ############# Labeling ##################
    titleaddrecord=Label(t,text="Add Record",font=("times new roman",20,"bold"),fg='black').place(x=290,y=180) 
    lblbk_id=Label(t,text="Book Id",font=("times new roman",17,"bold")).place(x=180,y=250)
    lblissuedby=Label(t,text="Issued By",font=("times new roman",17,"bold")).place(x=180,y=300)
    lblissuedon=Label(t,text="Issued On",font=("times new roman",17,"bold")).place(x=180,y=350)

    ############ Entries #####################
    txtbk_id=Entry(t,font=("times new roman",15,"bold"),textvariable=bk_id,width=18)
    txtbk_id.place(x=350,y=250)
    txtissuedby=Entry(t,font=("times new roman",15,"bold"),textvariable=issued_by,width=18)
    txtissuedby.place(x=350,y=300)
    txtissuedon=Entry(t,font=("times new roman",15,"bold"),textvariable=issued_on,width=18)
    txtissuedon.place(x=350,y=350)
    ################ SQL Code ##################
    def add_record():#for adding issuing
        bk_id=txtbk_id.get()
        issued_by=txtissuedby.get()
        issued_on=txtissuedon.get()

        command='insert into records(book_id,issued_by,issued_on) values(%s,%s,%s);' 
        values=(bk_id,issued_by,issued_on)
        mycursor.execute(command,values)
        mycon.commit()

        command1='update books set issued_by=%s where book_id=%s;'
        values1=(issued_by,bk_id)
        mycursor.execute(command1,values1)
        mycon.commit()
        a=str(bk_id)
        mycursor.execute("update books set is_issued=1 where book_id="+a +";")
        mycon.commit()
        messagebox.showinfo("Success","Issuing record added successfully")

    ############ Buttons ######################
    btnAddRecord=Button(t,text="Add Record",font=("arial",12,"bold"),width=10,bg="blue",fg="white",padx=10, command= lambda: [add_record(), txtissuedby.delete(0,'end'), txtissuedon.delete(0,'end'), txtbk_id.delete(0,'end')]).place(x=415,y=470) # add command in this button 
    Homebtn=Button(t,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10, command = lambda: [t.destroy(), root.deiconify()]).place(x=180,y=470)


def returnbook_button():

    global BackgroundImagereturnbook, returnbooklogo

    t=Toplevel()
    t.title("Library Management System")
    t.geometry("700x700")
    t.resizable(0,0)

    ######################################### VARIABLES VALUES ############################################################
    bk_id_2=  StringVar()
    returned_on=StringVar() 

    ############ Background Image ####################################
    BackgroundImagereturnbook=PhotoImage(file="returnbookbg.png")
    returnbookimagelabel=Label(t,image=BackgroundImagereturnbook).place(x=0,y=0)
    returnbooklogo=PhotoImage(file="returnbooklogo.png")
    returnbookimagelabel=Label(t,image=returnbooklogo).place(x=285,y=25)


    ############# Canvas ###################
    canvas_retrunbook=Canvas(t,width=400,height=290).place(x=160,y=170)
    
    ############# Labeling ##################
    titlereturnbook=Label(t,text="Return Book",font=("times new roman",20,"bold"),fg='black').place(x=290,y=180) 
    lblbk_id_2=Label(t,text="Book Id",font=("times new roman",17,"bold")).place(x=180,y=250)
    lblreturned_on=Label(t,text="Returned On",font=("times new roman",17,"bold")).place(x=180,y=300)

    ############ Entries #####################
    txtbk_id_2=Entry(t,font=("times new roman",15,"bold"),textvariable=bk_id_2,width=18)
    txtbk_id_2.place(x=350,y=250)
    txtreturned_on=Entry(t,font=("times new roman",15,"bold"),textvariable=returned_on,width=18)
    txtreturned_on.place(x=350,y=300)

    ################ SQL Code ##################
    def return_date(): #for adding reaturn date in records
        bk_id_2=txtbk_id_2.get()
        returned_on=txtreturned_on.get()
        
        global mycursor
        a=str(bk_id_2)
        mycursor.execute('select issued_by from records where book_id='+a +";")
        result=mycursor.fetchall()
        mycon.commit()
        c=result[-1][-1]

        mycursor.execute('update books set last_issued=%s where book_id=%s;',(c,bk_id_2))
        mycursor.execute('update books set is_issued=False where book_id=' +a +';')
        mycursor.execute('update books set issued_by=NULL where book_id=' +a +';')
        mycon.commit()

        mycursor.execute('select rec_no from records where book_id=' +a +';')
        d=mycursor.fetchall()
        mycon.commit()
        d=d[-1][-1]
        command='update records set returned_on=%s where rec_no=%s;'
        values=(returned_on,d)
        mycursor.execute(command,values)
        mycon.commit()
        messagebox.showinfo("Success","Return record added successfully")

    ############ Buttons ######################
    btnAddRecord=Button(t,text="Return Book",font=("arial",12,"bold"),width=10,bg="blue",fg="white",padx=10, command= lambda: [return_date(), txtreturned_on.delete(0,'end'), txtbk_id_2.delete(0,'end')]).place(x=415,y=410) # add command in this button 
    Homebtn=Button(t,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10,command =lambda: [t.destroy(), root.deiconify()]).place(x=180,y=410)

def stats():

    global Trendsimage
    t=Toplevel()
    t.title("Library Management System")
    t.geometry("700x700")
    t.resizable(0,0)
    ############ Background Image ####################################
    Trendsimage=PhotoImage(file="trends.png")
    Trendsimagelabel=Label(t,image=Trendsimage).place(x=0,y=0)

    Homebtn=Button(t,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10, command =lambda: [t.destroy(), root.deiconify()]).place(x=550,y=660)

def about():
    global Aboutimage, aboutlogo
    t=Toplevel()
    t.title("Library Management System")
    t.geometry("700x700")
    t.resizable(0,0)


    ############ Background Image ####################################
    Aboutimage=PhotoImage(file="aboutbg.png")
    Aboutimagelabel=Label(t,image=Aboutimage).place(x=0,y=0)
    

    aboutlogo=PhotoImage(file="aboutlogo.png")
    aboutimagelabel=Label(t,image=aboutlogo).place(x=293,y=20)

    ############# Canvas ###################
    canvas_addrecord=Canvas(t,width=485,height=350).place(x=113,y=170)

    ############# Labeling ##################
    titleabout=Label(t,text="About",font=("times new roman",20,"bold"),fg='black').place(x=330,y=180) 

    amanlb=Label(t,text="Aman Singh Rawat",font=("times new roman",15,"bold"))
    amanlb.place(x=130,y=250)

    amanlbinfo=Label(t,text="MySql Coding / Code Integration / Bug Fixing / Layout Designer",font=("times new roman",12)).place(x=130,y=275)

    rahullb=Label(t,text="Rahul Yadav",font=("times new roman",15,"bold")).place(x=130,y=350)

    rahullbinfo=Label(t,text="Interface Devloper / Tkinter Coding / Layout Designer/ Code Maintenance ",font=("times new roman",12)).place(x=130,y=375)


    Homebtn=Button(t,text="Home",font=("arial",12,"bold"),width=10,bg="green",fg="white",padx=10, command =lambda: [t.destroy(), root.deiconify()]).place(x=310,y=480)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root=Tk()
root.title("Library Management System")
root.geometry("1000x600")
root.resizable(0,0)

loginpage()

 




############################# Main Code Starts Here ##############################################

lbtitle=Label(root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",20,"bold"),padx=2,pady=6)
lbtitle.pack(side=TOP,fill=X)

################ Upward Frame ###################
frame=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
frame.place(x=0,y=90,width=1000,height=250)

#Registration column 
DataFrameLeft=LabelFrame(frame,text="Registration",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameLeft.place(x=10,y=5,width=250,height=200)
Registerimage=PhotoImage(file="register.png")
Registerimagelabel=Button(DataFrameLeft,image=Registerimage,border=0, command =lambda: [registration_button(), root.withdraw()])
Registerimagelabel.place(x=10,y=0)

#Add Book Column
DataFrameRight=LabelFrame(frame,text="Add Book",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameRight.place(x=340,y=5,width=250,height=200)
Addbookimage=PhotoImage(file="addbook.png")
Addbookimagelabel=Button(DataFrameRight,image=Addbookimage,border=0, command = lambda: [addbook_button(), root.withdraw()])
Addbookimagelabel.place(x=10,y=0)

#Add Record column
DataFrameCornRight=LabelFrame(frame,text="Add Record",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFrameCornRight.place(x=670,y=5,width=250,height=200)
Addrecordimage=PhotoImage(file="addrecord.png")
Addrecordimagelabel=Button(DataFrameCornRight,image=Addrecordimage,border=0, command = lambda: [addrecord_button(), root.withdraw()])
Addrecordimagelabel.place(x=10,y=0)



################# Down Frame #############
framedown=Frame(root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
framedown.place(x=0,y=345,width=1000,height=250)

#Return Book
DataFramedownleft=LabelFrame(framedown,text="Return Book",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFramedownleft.place(x=10,y=10,width=250,height=200)
returnbookimage=PhotoImage(file="returnbook.png")
returnbookimagelabel=Button(DataFramedownleft,image=returnbookimage,border=0, command = lambda: [returnbook_button(), root.withdraw()])
returnbookimagelabel.place(x=10,y=0)

#stats
DataFramedownright=LabelFrame(framedown,text="Statistics",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFramedownright.place(x=340,y=10,width=250,height=200)
Descriptionimage=PhotoImage(file="stats.png")
Descriptionimagelabel=Button(DataFramedownright,image=Descriptionimage,border=0, command = lambda: [stats(), root.withdraw()])
Descriptionimagelabel.place(x=10,y=0)

#about
DataFramedown=LabelFrame(framedown,text="About Us",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new roman",20,"bold"))
DataFramedown.place(x=670,y=10,width=250,height=200)
Statsimage=PhotoImage(file="help.png")
Statsimagelabel=Button(DataFramedown,image=Statsimage,border=0, command = lambda: [about(), root.withdraw()])
Statsimagelabel.place(x=10,y=0)


root.mainloop()



