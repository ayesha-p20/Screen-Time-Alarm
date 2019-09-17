#SCREEN TIME ALARM APPLICATION
from tkinter import *
import tkinter.font as font
import time
import winsound

def set_reminder():
    win.after(5*60*1000, None)
    for i in range(5):
         winsound.PlaySound("sound2.wav",winsound.SND_ASYNC)
         time.sleep(2)
    remind_win()

def remind_win():
    remind_win = Toplevel(win)
    remind_win.grab_set()
    remind_win.title("SCREEN TIME")
    pc_width = remind_win.winfo_screenwidth()
    pc_height = remind_win.winfo_screenheight()
    x_val = pc_width/2 - 125
    y_val = pc_height/2 - 75
    remind_win.geometry("250x150+%d+%d"%(x_val,y_val))
    remind_win.resizable(0,0)
    remind_win.minsize(250,150)
    lab1 = Label(remind_win,text = "REMINDER")
    lab1.place(x=85,y=25)
    lab2 = Label(remind_win,text = "YOUR SCREEN TIME IS UP!")
    lab2.place(x=35,y=50)
    button_ok = Button(remind_win,text = "Got it",height = 1, width = 11,bd = 1,bg = "white",activebackground = "light blue", command = lambda:[remind_win.destroy(),win.destroy()])
    button_ok.place(x=75,y=100)
    win.wait_window(remind_win)
    
def alarm_win():
    alarm_win = Toplevel(win)
    alarm_win.grab_set()
    alarm_win.title("SCREEN TIME")
    pc_width = alarm_win.winfo_screenwidth()
    pc_height = alarm_win.winfo_screenheight()
    x_val = pc_width/2 - 125
    y_val = pc_height/2 - 75
    alarm_win.geometry("250x150+%d+%d"%(x_val,y_val))
    alarm_win.resizable(0,0)
    alarm_win.minsize(250,150)
    label_message = Label(alarm_win,text = "YOUR SCREEN TIME IS UP!")
    label_message.place(x=35,y=45)
    button_gotit = Button(alarm_win,text = "Got it",height = 1, width = 11,bd = 1,bg = "white",activebackground = "light blue", command = lambda:[alarm_win.destroy(),win.destroy()])
    button_gotit.place(x=13,y=100)
    button_remind = Button(alarm_win, text = "Remind later", height = 1, width = 11, bd = 1,bg = "white",activebackground = "light blue", command = lambda:[alarm_win.destroy(),set_reminder()])
    button_remind.place(x=135, y=100)
    win.wait_window(alarm_win)

def ring():
    for i in range(7):
         winsound.PlaySound("Alarm01.wav",winsound.SND_ASYNC)
         time.sleep(2)
    alarm_win()

def set_alarm():  
    hour = spin_hour.get()
    mins = spin_min.get()
    sec = spin_sec.get()
    time_diff = (int(hour) - time.localtime().tm_hour)*3600 + (int(mins) - time.localtime().tm_min)*60 +  (int(sec) - time.localtime().tm_sec)    
    win.after(time_diff*1000,ring)

#app interface                 
win = Tk()
win.title("LIMIT YOUR SCREEN-TIME")
pc_width = win.winfo_screenwidth()
pc_height = win.winfo_screenheight()
x_val = pc_width/2 - 201
y_val = pc_height/2 - 125
win.geometry("402x250+%d+%d"%(x_val,y_val))
win.resizable(0,0)
win.configure(background = "light blue")

def_font = font.Font(size = 8,weight = "bold")

#labels
label_c1 = Label(win, text = ":", bg = "light blue", font = ("Helvetica", 14, "bold"))
label_c1.place(x = 115,y = 70)
label_c2 = Label(win, text = ":", bg = "light blue", font = ("Helvetica", 14, "bold"))
label_c2.place(x = 275, y = 70)
label_prompt = Label(win, text = "SELECT SCREEN TIME ALARM", bg = "light blue", font = ("Helvetica", 9, "bold"))
label_prompt.place(x = 100, y = 35)

#spinboxes
spin_hour = Spinbox(win, from_=0, to = 23, width = 7, wrap = True, justify = CENTER, bd = 3)
spin_hour.place(x = 10,y = 70)
spin_min = Spinbox(win, from_=0, to = 59, width = 7, wrap = True, justify = CENTER, bd = 3)
spin_min.place(x = 165, y = 70)
spin_sec = Spinbox(win, from_=0, to = 59, width = 7, wrap = True, justify = CENTER, bd = 3)
spin_sec.place(x = 320, y = 70)

#buttons
button1 = Button(win,text = "SET LIMIT",height = 2, width = 20,bg = "red",fg = "white", command = set_alarm)
button2 = Button(win,text = "CANCEL",height = 2, width = 20,bg = "red",fg = "white",command = win.destroy)
button1["font"] = def_font
button2["font"] = def_font
button1.place(x = 10,y = 150)
button2.place(x = 220,y = 150)
    

win.mainloop()



