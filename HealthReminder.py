from pygame import mixer
from time import time
from plyer import notification
from tkinter import *
import tkinter.messagebox

window = Tk()

window.geometry("517x593+450+55")
window.configure(bg = "#ffffff")

background=PhotoImage(file="images/background.png")
bg_label=Label(window,image=background).pack()


        
def soundON(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()   

def startRem():

    init_water=time()
    init_eyes=time()
    init_exer=time()
    
    water_sec=int(waterEntry.get())
    eyes_sec=int(eyesEntry.get())
    relax_sec=int(exerEntry.get())

    while (True):
        if (water_sec==0 and eyes_sec==0 and relax_sec==0):
            break

        if water_sec>0:
            if time()-init_water>water_sec:
                notification.notify(
                    title="Water Drinking Time !",
                    message="Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat.",
                    app_icon="images/water.ico",
                    timeout=5)
                soundON("sound/notification_sound.mp3")
                water_sec=0

        if eyes_sec>0:
            if time()-init_eyes>eyes_sec:
                notification.notify(
                    title="Eyes Relaxing Time !",
                    message="While sitting or lying down in a relaxed position (but not sleeping), imagine the world around you is black. By “relaxing into the blackness,” you are teaching your brain that your eyes do not have to always strain.",
                    app_icon="images/eye.ico",
                    timeout=5)
                soundON("sound/notification_sound.mp3")
                eyes_sec=0

        if relax_sec>0:
            if time()-init_exer>relax_sec:
                notification.notify(
                    title="Body Relaxing Time !",
                    message="Relaxation is a process that decreases the effects of stress on your mind and body. Relaxation techniques can help you cope with everyday stress and with stress related to various health problems.",
                    app_icon="images/exercise.ico",
                    timeout=5)
                soundON("sound/notification_sound.mp3")
                relax_sec=0


start_button_img = PhotoImage(file = f"images/startButton.png")

Press_Button = Button(
    image = start_button_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = startRem,
    relief = SUNKEN)

Press_Button.place(
    x = 369, y = 512,
    width=119,height=47)

waterEntry = Entry(window, font=('Helvetica',15),bg='white',fg='black'
                                ,justify=RIGHT,relief=FLAT)

waterEntry.place(
    x = 270, y = 313,
    width = 51,
    height = 22.89)

eyesEntry = Entry(window, font=('Helvetica',15),bg='white',fg='black'
                                ,justify=RIGHT,relief=FLAT)

eyesEntry.place(
    x = 270, y = 370,
    width = 51,
    height = 22.89)

exerEntry = Entry(window, font=('Helvetica',15),bg='white',fg='black'
                                ,justify=RIGHT,relief=FLAT)

exerEntry.place(
    x = 270, y = 426,
    width = 51,
    height = 22.89)



window.resizable(False, False)
window.mainloop()
