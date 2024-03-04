import mysql.connector as mc

import tkinter as tk
import csv

from tkinter import *

from tkinter import messagebox

from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from datetime import datetime
from tkinter import filedialog
from sqlalchemy import create_engine
import pandas as pd

root=tk.Tk()

root.minsize(600,580)

root.title('Vaccination')

tabControl = ttk.Notebook(root)

  

#creating invidual tabs

tab1 = ttk.Frame(tabControl)

tab2 = ttk.Frame(tabControl)

tab3 = ttk.Frame(tabControl)

#adding tabs into tab control

tabControl.add(tab1, text ='Check-in')

tabControl.add(tab2, text ='Immunity Check')

tabControl.add(tab3, text ='Import and Export')

#placing tab control

tabControl.pack(expand = 1, fill ="both")



#adding labels and text boxes

label_id=tk.Label(tab1,text="ID")

label_id.place(x=10,y=10)

entry_id=tk.Entry(tab1)

entry_id.place(x=130,y=10)

label_firstname=tk.Label(tab1,text="First name")

label_firstname.place(x=10,y=50)

entry_firstname=tk.Entry(tab1)

entry_firstname.place(x=130,y=50)

label_lastname=tk.Label(tab1,text="Last name")

label_lastname.place(x=10,y=100)

entry_lastname=tk.Entry(tab1)

entry_lastname.place(x=130,y=100)

label_sex=tk.Label(tab1,text="Sex")

label_sex.place(x=10,y=150)
cmb_sex=ttk.Combobox(tab1,values=['Male', 'Female', 'Other'])


cmb_sex.place(x=130,y=150)

label_yob=tk.Label(tab1,text="Year of birth")

label_yob.place(x=10,y=200)

entry_yob=tk.Entry(tab1)

entry_yob.place(x=130,y=200)



label_typeofvac=tk.Label(tab1,text="Type of vaccine")

label_typeofvac.place(x=10,y=250)

#creating combo box

cmb_typeofvac=ttk.Combobox(tab1,values=['Pfizer', 'AstraZeneca', 'Moderna', 'J&J'])

cmb_typeofvac.place(x=130,y=250)



label_date=tk.Label(tab1,text="Date")

label_date.place(x=10,y=300)

entry_date= DateEntry(tab1,width=30,bg="darkblue",fg="white")

entry_date.place(x=130,y=300)

label_time=tk.Label(tab1,text="Time")

label_time.place(x=10,y=350)

entry_time=tk.Entry(tab1)

entry_time.place(x=130,y=350)



label_phonenumber=tk.Label(tab1,text="Phone no")

label_phonenumber.place(x=10,y=400)

entry_phonenumber=tk.Entry(tab1)

entry_phonenumber.place(x=130,y=400)



label_dose=tk.Label(tab1,text="Dose number [1/2]")

label_dose.place(x=10,y=450)

entry_dose=tk.Entry(tab1)

entry_dose.place(x=130,y=450)

try:



        conn = mc.connect(user='root', password='', host='localhost')
        cursor = conn.cursor()
        sql = "CREATE database VACCINATION_DB"
        cursor.execute(sql) 
        conn.close() 
        conn = mc.connect(user='root', password='', host='localhost', database="VACCINATION_DB")
        cursor = conn.cursor()



        sql ='''CREATE TABLE VACCINATED (ID CHAR(10) NOT NULL,FIRST_NAME CHAR(100),LAST_NAME CHAR(100),SEX CHAR(10),YEAR_OF_BIRTH CHAR(4),TYPE_OF_VACCINE CHAR(100),DATE CHAR(100),PHONE_NUMBER CHAR(10),DOSE CHAR(2))'''
        cursor.execute(sql) 
        conn.close() 
except:
            pass        


#creating database connection

c=mc.connect(host="localhost",

  user="root",

  passwd="",

  database="VACCINATION_DB")

cur=c.cursor()#creating cursor object

def insert():

    user_id=entry_id.get()

    if len(user_id)!=10:#checking validation for ID

        messagebox.showinfo("error", "ID must be of 10 digits")

        return

    firstname=entry_firstname.get()

    if firstname.strip()=="":#checking validation for first name

        messagebox.showinfo("error", "please enter first name ")

        return

    lastname=entry_lastname.get()

    if lastname.strip()=="":#checking validation for last name

        messagebox.showinfo("error", "please enter last name ")

        return

    sex=cmb_sex.get()

    if sex.strip()=="":#checking validation for sex

        messagebox.showinfo("error", "please enter sex ")

        return

    yob=entry_yob.get()

    if yob.strip()=="":#checking validation for yob

        messagebox.showinfo("error", "please enter yob ")

        return



    if int(yob)<1900 or int(yob)>2003:

        messagebox.showinfo("error", "Year of birth must be between 1900 and 2003")

        return

    tov=cmb_typeofvac.get()

    dt=entry_date.get_date().strftime("%m/%d/%Y")

    if dt.strip()=="":#checking validation for date

        messagebox.showinfo("error", "please enter date")

        return

    

    tm=entry_time.get()

    if tm.strip()=="":#checking validation for time

        messagebox.showinfo("error", "please enter time ")

        return
    time = datetime.strptime(tm, "%H:%M").strftime("%I:%M %p")
    date_and_time=dt+' '+time

    phonenumber=entry_phonenumber.get()

    if len(phonenumber)!=10:#checking validation for phone number

        messagebox.showinfo("error", "Ph number must be of 10 digits")

        return

    dose=entry_dose.get()

    if dose.strip()=="":#checking validation for dose

        messagebox.showinfo("error", "please enter dose ")

        return
     

    sql = "INSERT INTO VACCINATED (ID, FIRST_NAME,LAST_NAME,SEX,YEAR_OF_BIRTH,TYPE_OF_VACCINE,DATE,PHONE_NUMBER,DOSE) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"

    val = (user_id,firstname,lastname,sex,yob,tov,date_and_time,phonenumber,dose)

    

    cur.execute(sql,val)#executing sql

    c.commit()#commiting the change

    messagebox.showinfo("insert", "Record inserted")

    #clearing text fields

    entry_id.delete(first=0,last=100)

    entry_firstname.delete(first=0,last=100)

    entry_lastname.delete(first=0,last=100)

    entry_yob.delete(first=0,last=100)

    entry_phonenumber.delete(first=0,last=100)

    entry_time.delete(first=0,last=100)

    entry_dose.delete(first=0,last=100)




submit_button = tk.Button(tab1,text="submit",command=insert)

submit_button.place(x=10,y=500)






#Import file function
def import_file():



    c=mc.connect(host="localhost",

    user="root",

    passwd="",

    database="VACCINATION_DB")

    cur=c.cursor()

    

    
    selected_csv_file_location = filedialog.askopenfilename()
   

    with open(selected_csv_file_location) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                
                line_count += 1
            else:

                    line_count += 1
                    sql = "INSERT INTO VACCINATED (ID, FIRST_NAME,LAST_NAME,SEX,YEAR_OF_BIRTH,TYPE_OF_VACCINE,DATE,PHONE_NUMBER,DOSE) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"

                    val = (row[3],row[0],row[1],row[2],row[4],row[5],row[6],row[7],0)

                    cur.execute(sql,val)
                    c.commit()
                    messagebox.showinfo("insert", "CSV file Record inserted")
    c.close()                


                
#Export file function
def export_file():

    selected_folder = filedialog.askdirectory()
    db_connection_str = 'mysql+pymysql://root:''@localhost/VACCINATION_DB'
    db_connection = create_engine(db_connection_str)

    df = pd.read_sql('SELECT * FROM VACCINATED', con=db_connection)
    df.drop('DOSE', inplace=True, axis=1)
    df.set_axis(['ID','FirstName', 'LastName', 'Sex','YOB', 'TOV', 'DT', 'PhoneNO'], axis=1, inplace=True)
    df=df[['FirstName', 'LastName', 'Sex','ID','YOB', 'TOV', 'DT', 'PhoneNO']]
    df.to_csv(f'{selected_folder}\\vaccinated.csv',index=FALSE)
    db_connection.dispose()



    

    messagebox.showinfo("export", "Records exported to CSV file")        

    



label_status_check=tk.Label(tab2,text="Status Check")

label_status_check.place(x=10,y=10)

label_check_by_id=tk.Label(tab2,text="ID")

label_check_by_id.place(x=10,y=60)

entry_check_by_id=tk.Entry(tab2)

entry_check_by_id.place(x=80,y=60)



label_status=tk.Label(tab2,text="Status")

label_status.place(x=10,y=100)

color_code=tk.Label(tab2,width=20)

color_code.place(x=80,y=100)


comment=tk.Label(tab2)

comment.place(x=240,y=100)

def check():

  

    c=mc.connect(host="localhost",

    user="root",

    passwd="",

    database="VACCINATION_DB")

    cur=c.cursor()

    cur.execute("SELECT * FROM VACCINATED")

    target_usr_id=int(entry_check_by_id.get())

    for i in cur:

        if int(i[0])==target_usr_id and int(i[8])==2:

            color_code.config(bg= "Green")

            comment.configure(text="Fully vaccinated")  

            break

        elif str(i[0])==target_usr_id and int(i[8])==1:

            color_code.config(bg="Yellow")

            comment.configure(text="Vaccinated")

            break

    else:

        color_code.config(bg= "Red")

        comment.configure(text="Not vaccinated")

    c.close()





check_button = tk.Button(tab2,text="Check",command=check)

check_button.place(x=10,y=150)



ll2=tk.Label(tab3,text="Import/Export")

ll2.place(x=10,y=10)

b3 = tk.Button(tab3,text="Import",command=import_file)
b3.place(x=10,y=100)
b4 = tk.Button(tab3,text="Export",command=export_file)
b4.place(x=60,y=100)
root.mainloop()


