    
#Shilpesh Jentilal
#MasterMind Quizz
#

from tkinter import *
from tkinter import messagebox
import time


#when exit button is pressed...
def exit1():
    exit()
def trickIspressed():
        messagebox.showinfo("Coming Soon","Coming Soon!")
   
#Maths Questions start===========================================================================================================================================================================================    
def mathIspressed():
    lbltopic.destroy()
    math.destroy()
    tricky.destroy()
    coming_soon.destroy()
    Math_1()
#Math Question one=====================================================================================================    
def Math_1():
    master.geometry("700x700")
    global M_Q1
    global Q1
    global Q1_B1
    global Q1_B2
    global Q1_B3
    global Q1_B4
 
    #Adding heading
    M_Q1=Label(master,text="QUESTION 1:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    M_Q1.grid(row=0,column=1)
    #Adding Question  
    Q1=Label(master,text="What is 2+41+86?",bg="white",fg="black",width="23",height="4",font="gray14 24 bold")
    Q1.grid(row=1, column=1)
    
    #option buttons
    global Score
    Score=0
    Q1_B1=Button(master,width=17,text="129",height="2",font="none 14 bold",fg="black", command=correct_1,bg="green")
    Q1_B1.grid(row=2,column=1,sticky=W,pady=40,padx=115)
    Q1_B2=Button(master,width=17,text="130",height="2",font="none 14 bold",fg="black", command=wrong_1,bg="green")
    Q1_B2.grid(row=2,column=1,sticky=E,pady=40,padx=115)
    Q1_B3=Button(master,width=17,text="128",height="2",font="none 14 bold",fg="black", command=wrong_1,bg="green")
    Q1_B3.grid(row=3,column=1,sticky=W,padx=115)
    Q1_B4=Button(master,width=17,text="186",height="2",font="none 14 bold",fg="black", command=wrong_1,bg="green")
    Q1_B4.grid(row=3,column=1,sticky=E,padx=115)
    
def correct_1():
    global Score
    Score+=1
    Math_2()
def wrong_1():
    Math_2()
#=====================================================================================================    
#Math Question two=====================================================================================================    
    
def Math_2():
    M_Q1.destroy()
    Q1.destroy()
    Q1_B1.destroy()
    Q1_B2.destroy()
    Q1_B3.destroy()
    Q1_B4.destroy()
    global M_Q2
    global Q2
    global Q2_B1
    global Q2_B2
    global Q2_B3
    global Q2_B4


    #Adding heading
    M_Q2=Label(master,text="QUESTION 2:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    M_Q2.grid(row=0,column=1)
    #Adding Question  
    Q2=Label(master,text="What is 5+3x6?",bg="white",fg="black",width="23",height="4",font="gray14 24 bold")
    Q2.grid(row=1, column=1)
    #option buttons
    Q2_B1=Button(master,width=17,text="48",height="2",font="none 14 bold",fg="black", command=wrong_2,bg="green")
    Q2_B1.grid(row=2,column=1,sticky=W,pady=40,padx=115)
    Q2_B2=Button(master,width=17,text="17",height="2",font="none 14 bold",fg="black", command=wrong_2,bg="green")
    Q2_B2.grid(row=2,column=1,sticky=E,pady=40,padx=115)
    Q2_B3=Button(master,width=17,text="23",height="2",font="none 14 bold",fg="black", command=correct_2,bg="green")
    Q2_B3.grid(row=3,column=1,sticky=W,padx=115)
    Q2_B4=Button(master,width=17,text="30",height="2",font="none 14 bold",fg="black", command=wrong_2,bg="green")
    Q2_B4.grid(row=3,column=1,sticky=E,padx=115)

def correct_2():
    global Score
    Score+=1
    Math_3()
    
def wrong_2():
    Math_3()
#=====================================================================================================    
#Math Question three=====================================================================================================    
def Math_3():
    M_Q2.destroy()
    Q2.destroy()
    Q2_B1.destroy()
    Q2_B2.destroy()
    Q2_B3.destroy()
    Q2_B4.destroy()
    global M_Q3
    global Q3
    global Q3_B1
    global Q3_B2
    global Q3_B3
    global Q3_B4
    #Adding heading
    M_Q3=Label(master,text="QUESTION 3:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    M_Q3.grid(row=0,column=1)
    #Adding Question  
    Q3=Label(master,text="What is the sum \nof the angle in any triangle?",bg="white",fg="black",width="23",height="4",font="gray14 24 bold")
    Q3.grid(row=1, column=1)
    #option buttons
    Q3_B1=Button(master,width=17,text="560°",height="2",font="none 14 bold",fg="black", command=wrong_3,bg="green")
    Q3_B1.grid(row=2,column=1,sticky=W,pady=40,padx=115)
    Q3_B2=Button(master,width=17,text="180°",height="2",font="none 14 bold",fg="black", command=correct_3,bg="green")
    Q3_B2.grid(row=2,column=1,sticky=E,pady=40,padx=115)
    Q3_B3=Button(master,width=17,text="360°",height="2",font="none 14 bold",fg="black", command=wrong_3,bg="green")
    Q3_B3.grid(row=3,column=1,sticky=W,padx=115)
    Q3_B4=Button(master,width=17,text="90°",height="2",font="none 14 bold",fg="black", command=wrong_3,bg="green")
    Q3_B4.grid(row=3,column=1,sticky=E,padx=115)

def correct_3():
    global Score
    Score+=1
    Math_4()
    
def wrong_3():
    Math_4()
#=====================================================================================================    

#Math Question four=====================================================================================================    

def Math_4():
    M_Q3.destroy()
    Q3.destroy()
    Q3_B1.destroy()
    Q3_B2.destroy()
    Q3_B3.destroy()
    Q3_B4.destroy()
    global M_Q4
    global Q4
    global Q4_B1
    global Q4_B2
    global Q4_B3
    global Q4_B4
    #Adding heading
    M_Q4=Label(master,text="QUESTION 4:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    M_Q4.grid(row=0,column=1)
    #Adding Question  
    Q4=Label(master,text="How many days are there \nin 8 weeks?",bg="white",fg="black",width="23",height="4",font="gray14 24 bold")
    Q4.grid(row=1, column=1)
    #option buttons
    Q4_B1=Button(master,width=17,text="7 days",height="2",font="none 14 bold",fg="black", command=wrong_4,bg="green")
    Q4_B1.grid(row=2,column=1,sticky=W,pady=40,padx=115)
    Q4_B2=Button(master,width=17,text="49 days",height="2",font="none 14 bold",fg="black", command=wrong_4,bg="green")
    Q4_B2.grid(row=2,column=1,sticky=E,pady=40,padx=115)
    Q4_B3=Button(master,width=17,text="56 days",height="2",font="none 14 bold",fg="black", command=correct_4,bg="green")
    Q4_B3.grid(row=3,column=1,sticky=W,padx=115)
    Q4_B4=Button(master,width=17,text="49 days",height="2",font="none 14 bold",fg="black", command=wrong_4,bg="green")
    Q4_B4.grid(row=3,column=1,sticky=E,padx=115)
def correct_4():
    global Score
    Score+=1
    Math_5()
    
def wrong_4():
    Math_5()

def Math_5():
    M_Q4.destroy()
    Q4.destroy()
    Q4_B1.destroy()
    Q4_B2.destroy()
    Q4_B3.destroy()
    Q4_B4.destroy()
    global M_Q5
    global Q5
    global Q5_B1
    global Q5_B2
    global Q5_B3
    global Q5_B4
    #Adding heading
    M_Q5=Label(master,text="QUESTION 5:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    M_Q5.grid(row=0,column=1)
    #Adding Question  
    Q5=Label(master,text="If 27 out of 60 cars are red,\nwhat is the percentage of \nnon-red cars?",bg="white",fg="black",width="23",height="4",font="gray14 24 bold")
    Q5.grid(row=1, column=1)
    #option buttons
    Q5_B1=Button(master,width=17,text="27%",height="2",font="none 14 bold",fg="black", command=wrong_5,bg="green")
    Q5_B1.grid(row=2,column=1,sticky=W,pady=40,padx=115)
    Q5_B2=Button(master,width=17,text="49%",height="2",font="none 14 bold",fg="black", command=wrong_5,bg="green")
    Q5_B2.grid(row=2,column=1,sticky=E,pady=40,padx=115)
    Q5_B3=Button(master,width=17,text="55%",height="2",font="none 14 bold",fg="black", command=correct_5,bg="green")
    Q5_B3.grid(row=3,column=1,sticky=W,padx=115)
    Q5_B4=Button(master,width=17,text="43%",height="2",font="none 14 bold",fg="black", command=wrong_5,bg="green")
    Q5_B4.grid(row=3,column=1,sticky=E,padx=115)

def correct_5():
    global Score
    Score+=1
    M_result()
    
def wrong_5():
    M_result()

def M_result():
    M_Q5.destroy()
    Q5.destroy()
    Q5_B1.destroy()
    Q5_B2.destroy()
    Q5_B3.destroy()
    Q5_B4.destroy()
    global lblR
    global lblS
    global lblSE
    global btnMenu
    master.geometry("500x500")
    lblR=Label(master,text="Your score is:",bg="purple",fg="white",width="17",height="4",font="gray14 35 bold")
    lblR.grid(row=0,column=1)
    lblS=Label(master,text=Score,bg="purple",fg="green",width="17",height="0",font="gray14 35 bold")
    lblS.grid(row=1,column=1)
    lblSE=Label(master,text="out of 5",bg="purple",fg="green",width="17",height="0",font="gray14 35 bold")
    lblSE.grid(row=2,column=1)
    btnMenu=Button(master,width=17,text="Main\nMenu",height="2",font="none 14 bold",fg="black", command=wma,bg="red")
    btnMenu.grid(row=3,column=1,pady=20)


#Maths Questions End===========================================================================================================================================================================================    

#when Main menu button pressed, destroys all the labels and buttons
def wma():
    lblR.destroy()
    lblS.destroy()
    lblSE.destroy()
    btnMenu.destroy()
    MainMain()



    
#============================================================================================================================================
#When Play is pressed   
def playIspressed():
    Master.destroy()
    Mind.destroy()
    Quiz.destroy()
    btnstart.destroy()
    btnexit.destroy()
    master.geometry("700x700")
    Topic()
def Topic():
    global lbltopic
    global math
    global tricky
    global coming_soon
    
    lbltopic=Label(master,text="CHOOSE A TOPIC:",bg="purple",fg="white",width="23",height="4",font="gray14 35 bold")
    lbltopic.grid(row=0,column=1,sticky=E)
    #topics
    math=Button(master,width=17,text="Maths",height="2",font="none 14 bold",fg="black", command=mathIspressed,bg="green")
    math.grid(row=1,column=1,sticky=W,padx=50)
    tricky=Button(master,width=17,text="Trick Questions",height="2",font="none 14 bold",fg="black", command=trickIspressed,bg="green")
    tricky.grid(row=1,column=1,sticky=E)

    #if u want to addd  more topics/buttons==
    coming_soon=Label(master,text="More Topics coming soon...",bg="purple",fg="white",width="23",height="4",font="gray14 20 bold")
    coming_soon.grid(row=5,column=1)
#============================================================================================================================================

#the program opens from here...>>
#Main Menu
def Main():
    global master
    master = Tk()
    master.geometry("500x500")
    master.title("Master Mind Quiz")
    master.configure(bg="purple")
    master.resizable(0,0)
    MainMain()
def MainMain():
    global Master
    global Mind
    global Quiz
    global btnstart
    global btnexit
    global destroy
    #Label for Name "Master Mind Quiz
    Master=Label(master,text="Master",bg="purple",fg="white",width="17",font="gray14 35 bold")
    Master.grid(row=0,column=1,sticky=E)    
    Mind=Label(master,text="Mind",bg="purple",fg="white",font="gray14 35 bold")
    Mind.grid(row=2,column=1)
    Quiz=Label(master,text="Quiz",bg="purple",fg="white",font="gray14 35 bold")
    Quiz.grid(row=3,column=1)
    #For Space :D
    space=Label(master,text="",bg="purple",fg="white",font="gray14 35 bold")
    space.grid(row=4,column=1)
    #button for play
    btnstart=Button(master,width=17,text="Play",height="2",font="none 14 bold",fg="white", command=playIspressed,bg="black")
    btnstart.grid(row=5,column=1)
    #button for exit
    btnexit=Button(master,width=17,text="Quit",height="2",font="none 14 bold",fg="white", command=exit1,bg="black")
    btnexit.grid(row=6,column=1,pady=20)



Main()
mainloop()
