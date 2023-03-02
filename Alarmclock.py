from tkinter import *
import datetime
import time
import winsound

def alarm(set_timer):
    while True:
        time.sleep(1)
        currenttime=datetime.datetime.now()
        actualtime=currenttime.strftime("%H:%M:%S")
        date=currenttime.strftime("%d/%m/%y")
        print("Today's Date is:",date)
        print(actualtime)
        if actualtime==set_timer:
            print("Time to wake up!!")
            winsound.PlaySound("alarm.wav",winsound.SND_FILENAME)
            break

def alarm_time():
    set_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_timer)

clock=Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
clock.configure(bg="cyan")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Arial").place(x=90,y=12)
addTime = Label(clock,text = "Hour       Min          Sec  ",font=60,fg="red").place(x = 155,y=50)
setYourAlarm = Label(clock,text = "Time to wake you up",fg="blue",relief = "solid",font=("Helevetica",9,"bold")).place(x=11,y=90)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0]) 

minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
min.set(minutes[0]) 

seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
sec.set(seconds[0])
 
#Time required to set the alarm clock:
hourTime= OptionMenu(clock, hour, *hours )
hourTime.config(bg = "pink",width = 5)
hourTime.place(x=150,y=90)

minTime= OptionMenu(clock,min, *minutes)
minTime.config(bg = "pink",width = 5)
minTime.place(x=210,y=90)

secTime = OptionMenu(clock,sec, *seconds)
secTime.config(bg = "pink",width = 5)
secTime.place(x=270,y=90)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="black",bg="magenta",width = 10,command = alarm_time,font=("Bold")).place(x =130,y=135)
clock.mainloop()
