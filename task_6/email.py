import tkinter as tk
import re

emailValidator = tk.Tk()

canvas1 = tk.Canvas(emailValidator, width = 400, height = 300, relief = 'raised')
canvas1.pack()

label1 = tk.Label(emailValidator, text='Validate your Email')
label1.config(fg='brown', font=('None', 20, 'bold'))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(emailValidator, text='Type your Email:')
label2.config(font=('None', 15))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(emailValidator) 
canvas1.create_window(200, 140, window=entry1)

def check():
        #regex taken from https://emailregex.com
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

        email = entry1.get()

        if(re.search(regex,email)):
                label4 = tk.Label(emailValidator, text='Valid Email !', fg='green')
                canvas1.create_window(200, 230, window=label4) 
        else:  
                label4 = tk.Label(emailValidator, text='Invalid Email !', fg='red')
                canvas1.create_window(200, 230, window=label4) 
    
button1 = tk.Button(text='Check', command=check, fg='blue')
canvas1.create_window(200, 180, window=button1)

emailValidator.mainloop()
