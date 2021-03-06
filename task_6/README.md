## #6 Design a desktop application using python to validate an email.

I had never used the tkinter library before. But I am proficient in Python. So I decided to learn about the basics of tkinter from [here](https://realpython.com/python-gui-tkinter/). 

<u>Here are the steps I followed to make the final app.</u>

1. I wrote a simple python function to validate the entered email using regex search. I found a website https://emailregex.com. The headline of site says "Email Address Regular Expression That 99.99% Works."  🤩 So I copied the regex expression from there.

2. Then I looked for example codes of tkinter and came across a simple tkinter app to find square root of number. I modified the code to work as Email Validator. 

   Yes I know I am lazy. 😜 But I managed to finish the task in 2 steps. That's what programmers do, right? Copy paste XD

<u>I only faced one difficulty while doing this task.</u>

I was using homebrew python and it does not come with [Tcl/Tk](https://www.tcl.tk) dependency required by Tkinter. The default system version is used instead which is depricated. So I had to use official macOS python installer. (which I really hate using 🥺)

## Email Validator with tkinter

<img src="https://github.com/anmolkapil/technojam-task/blob/main/task_6/images/Application.png" width="500">

## **How to use?**

1. Type your Email in the box.
2. Click on Button saying "Check".

Done! 👍🏻



## Screenshots

<img src="https://github.com/anmolkapil/technojam-task/blob/main/task_6/images/Valid.png" width="500">
<img src="https://github.com/anmolkapil/technojam-task/blob/main/task_6/images/Invalid.png" width="500">

