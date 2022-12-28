# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:55:52 2022

@author: Dell

"""
from tkinter import *
root = Tk()
root.geometry("500x500")
root.configure(bg = "cyan")

label_name_gui = Label(root , text = "Name : "  )
label_name_gui.place(relx = 0.4 , rely = 0.2 , anchor = CENTER)

label_password_gui = Label(root , text = "Passswod : " )
label_password_gui.place(relx = 0.4 , rely = 0.3 , anchor = CENTER)

label_captcha_gui = Label(root , text = "Captca : ")
label_captcha_gui.place(relx = 0.4 , rely = 0.4 , anchor = CENTER)

input_name = Entry(root)
input_name.place(relx = 0.7 , rely = 0.2 , anchor = CENTER)

input_password = Entry(root)
input_password.place(relx = 0.7 , rely = 0.3 , anchor = CENTER)

input_captcha = Entry(root)
input_captcha.place(relx = 0.7 , rely = 0.4 , anchor = CENTER)

label_name = Label(root )
label_name.place(relx = 0.4 , rely = 0.7, anchor = CENTER)

label_password = Label(root)
label_password.place(relx = 0.4 , rely = 0.8 , anchor = CENTER)

label_captcha = Label(root)
label_captcha.place(relx = 0.4 , rely = 0.9, anchor = CENTER)

class userDB:
    def __init__(self):
        self.__username = "Ruhaan"
        self.__password = "RuhaanKalla007"
        self.__captcha = "28&%7GH9"
        
    def showuser(self):
        label_name["text"] = "Name : " + self.__username
        label_password["text"] = "Password : " + self.__password
        label_captcha["text"] = "Captcha : " + self.__captcha
        
obj = userDB()
def adduser():
    global obj
    obj.username = input_name.get()
    obj.passsword = input_password.get()
    obj.captcha = input_captcha.get()
    print("details updated")
    
btn_login = Button(root , text = "Updat Login Details" , command = adduser)  
btn_login.place(relx = 0.3 , rely = 0.55 , anchor = CENTER)
btn_show_profile = Button(root , text = "Show Profile" , command = obj.showuser )  
btn_show_profile.place(relx = 0.6 , rely = 0.55 , anchor = CENTER)                

root.mainloop()
