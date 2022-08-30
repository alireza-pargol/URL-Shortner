"""
برای درست کار کردن این کد
باید از فیلتر شکن استنفاده کنید
"""
from tkinter import *
from pyshorteners import Shortener
import requests

def shorten():
    if shorty.get():
        shorty.delete(0,END)

    if shortner.get():
        #ساخت لینک کوتاه با استفاده از سرویس tinyurl
        url = Shortener().tinyurl.short(shortner.get())
        # نمایش خروجی روی نمایشگر
        shorty.insert(END,url)

window = Tk()
window.title("URL Shortner")
window.geometry("500x500")

Label(window, text="Enter Link To Shorten",
      font=("Arial", 30)).pack(fill="both",pady=20)

shortner = Entry(window, font=("Arial", 20))
shortner.pack(fill="both",pady=20)

btn = Button(window, text="Shorten Url",
             font=("Arial", 20), command=shorten)
btn.pack(pady=20)

shorty_lable = Label(window,text='Shortened link',font=("Arial", 14))
shorty_lable.pack(pady=50)

shorty = Entry(window,font=("Arial", 18) ,
               justify=CENTER , bd=0 , bg = "systembuttonface")
shorty.pack(fill="both",pady=15)

window.mainloop()
