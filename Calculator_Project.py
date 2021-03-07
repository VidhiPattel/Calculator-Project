# Python program to create a simple GUI calculator using Tkinter 

# import everything from tkinter 
import tkinter as tk

#import tkinter.messagebox
from tkinter import messagebox

#import pyperclip module
import pyperclip 

#import math module
import math
        
# assigning empty string to the variable operator 
operator = ""

# assigning switch variable to none 
switch=None

#============================================================================================================================================================================#

# Function to update expression in the text entry box 
def Click(numbers):
    
    # point out the global operator variable 
    global operator 
    
    if numbers == "00":
        
        operator += numbers
    
    else:
        operator += str(numbers)
    
    # update the operator by using set method 
    text_Input.set(operator)

#============================================================================================================================================================================#

# Function to clear the contents of text entry box 
def AllClearDisplay():
    global operator
    operator = ""      
    text_Input.set("")
    
#============================================================================================================================================================================#

# Function to clear the contents of text entry box 
def ClearDisplay(numbers):
    global operator
   
    operator=operator[0:-1] # If Operator is "1234" then it sets operator to "123"

    text_Input.set(operator)

#============================================================================================================================================================================#
# Function to evaluate the final expression 
def EqualsInput():
    
    # Putting the code inside the try block which may generate the error 
    try:
        
        global operator     
        
        # eval function evaluate the operator and str function convert the result into string 
        sumup=str(eval(operator))

        text_Input.set(sumup)
        
        # initialze the operator variable by empty string 
        operator = ""
        
    except: 
        text_Input.set(" error ") 
        operator = "" 
       
#============================================================================================================================================================================#

# Function to call pi value from math value for evaluation
def Pi():
        global operator
        operator += str(math.pi)
        text_Input.set(operator)

#============================================================================================================================================================================#

# Function to find modulus
def Percent():
    global operator
    operator=float(operator)/100
    text_Input.set(operator)
    
#============================================================================================================================================================================#

# Function to find log 
def Square():
    global operator
    operator=float(operator)*float(operator)
    text_Input.set(operator)
    
#============================================================================================================================================================================#

# Function to find sine of numbers
def Sine():
   global operator
   try:
        ans = float(operator)
        if switch is True:
            operator =str( math.sin(math.radians(ans)))
            text_Input.set(operator)
            
        else:
            operator=str(math.sin(ans))
            text_Input.set(operator)
            
   except Exception:
       operator=" "
       text_Input.set("error")
        
#============================================================================================================================================================================#

# Function to find cosine of numbers
def Cosine():
    global operator
    try:
        ans = float(operator)
        if switch is True:
            operator =str( math.cos(math.radians(ans)))
            text_Input.set(operator)
            
        else:
            operator=str(math.cos(ans))
            text_Input.set(operator)
            
    except Exception:
        operator=" "
        text_Input.set("error")

#============================================================================================================================================================================#

# Function to find tangent of numbers
def Tan():
   global operator
   try:
        ans = float(operator)
        if switch is True:
            operator = str(math.tan(math.radians(ans)))
            text_Input.set(operator)
            
        else:
            operator=str(math.tan(ans))
            text_Input.set(operator)
            
   except Exception:
       operator=" "
       text_Input.set("error")
       
#============================================================================================================================================================================#

# Function to find factorial of numbers
def Factorial():
    global operator
    try:
        ans = float(operator)
        operator = str(math.factorial(ans))
        text_Input.set(operator)
        
    except Exception:
        operator=" "
        text_Input.set("error")

#============================================================================================================================================================================#

# Function to find value of log with base 10
def Logarithm():
    global operator
    try:
        operator = math.log10(float(operator))
        text_Input.set(operator)
        
    except Exception:
        operator=" "
        text_Input.set("error")

#============================================================================================================================================================================#

# Function to find natural log
def Ln():
    global operator
    try:
        ans = float(operator)
        operator = math.log(ans)
        text_Input.set(operator)
        
    except Exception:
        operator=" "
        text_Input.set("error")
        
#============================================================================================================================================================================#

# Function to switch from radian to degree and vice-versa
def Convert():
    global switch
    if switch is None:
        switch = True
        conv_btn['text'] = "Deg"
    else:
        switch = None
        conv_btn['text'] = "Rad"
        
#============================================================================================================================================================================#

# Function to find exponent of numbers
def E():
    global operator
    operator=str(math.exp(float(operator)))
    text_Input.set(operator)
    
#============================================================================================================================================================================#

# function to copy from text entry box
def Copy():
    pyperclip.copy(operator)
    
#============================================================================================================================================================================#

# function to copy from text entry box
def Paste():
    global operator
    #operator=operator+str(pyperclip.paste())
    operator += str(pyperclip.paste())
    text_Input.set(operator)
    
#============================================================================================================================================================================#

# function to exit from the application window
def Exit():
    Exit=messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if Exit > 0:
        cal.destroy()
        return

#============================================================================================================================================================================#

# Driver code 

numbers, powers, = 0, 0

# create a GUI window 
cal = tk.Tk() 

# Restrict to the given size
# Window couldn't be resized
cal.resizable(0, 0)

# set the background colour of GUI window 
cal.configure(background="light slate grey") 

# set the title of GUI window 
cal.title("Calculator") 

# set the configuration of GUI window 
cal.geometry("615x440") 

#creating menubar in the GUI window
menubar=tk.Menu(cal)

#adding Edit menu to menubar
editmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)

#adding copy & paste item to Edit
editmenu.add_command(label="Copy", command=Copy)
editmenu.add_command(label="Paste", command=Paste)

#adding File menu to menubar
exitmenu=tk.Menu(menubar, tearoff=0)

#adding Exit item to Exit
menubar.add_cascade(label="Exit",menu=exitmenu)
exitmenu.add_command(label="Exit", command = Exit)

# to enable the menu in main window
cal.configure(menu=menubar)

# StringVar() is the variable class 
# we create an instance of this class 
text_Input = tk.StringVar() 

# create the text entry box for showing the expression . 
# grid method is used for placing the widgets at respective positions 
# in table like structure . 
txtDisplay = tk.Entry(cal, font = ('verdana',20), textvariable=text_Input, bd=28, insertwidth=0, bg="light gray", justify='right').grid(columnspan=7)

# creating Buttons and place at a particular location inside the window . 
# when user press the button, the command or function affiliated to that button is executed .
        
buttonAllClear = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="AC", bg="lavender", command=AllClearDisplay)
buttonAllClear.grid(row=1, column=0)

percent = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="%", bg="lavender", command=lambda:Percent())
percent.grid(row=1, column=1)

buttonClear = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="<=", bg="lavender", command=lambda:ClearDisplay("<="))
buttonClear.grid(row=1, column=2)

Division = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="/", bg="thistle1", command=lambda:Click("/"))
Division.grid(row=1, column=3)

pi = tk.Button(cal, padx=16, width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="Pi", bg="thistle1", command=Pi)
pi.grid(row=1, column=4)

conv_btn = tk.Button(cal, padx=16, width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="Rad", bg="thistle1", command=Convert)
conv_btn.grid(row=1, column=5)

#============================================================================================================================================================================#

button7 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="7", bg="lavender", command=lambda:Click(7))
button7.grid(row=2, column=0)

button8 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="8", bg="lavender", command=lambda:Click(8))
button8.grid(row=2, column=1)

button9 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="9", bg="lavender", command=lambda:Click(9))
button9.grid(row=2, column=2)

Multiplication = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="*", bg="thistle1", command=lambda:Click("*"))
Multiplication.grid(row=2, column=3)

square = tk.Button(cal, padx=16,  width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="x2", bg="thistle1", command=lambda:Square())
square.grid(row=2, column=4)

log10 = tk.Button(cal, padx=16,  width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="log10", bg="thistle1", command=lambda:Logarithm())
log10.grid(row=2, column=5)

#============================================================================================================================================================================#

button4 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="4", bg="lavender", command=lambda:Click(4))
button4.grid(row=3, column=0)

button5 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="5", bg="lavender", command=lambda:Click(5))
button5.grid(row=3, column=1)

button6 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="6", bg="lavender", command=lambda:Click(6))
button6.grid(row=3, column=2)

Subtraction = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="-", bg="thistle1", command=lambda:Click("-"))
Subtraction.grid(row=3, column=3)

sine = tk.Button(cal, padx=16, bd=8,  width=3, fg="black", font = ('arial',20,'bold'), text="sin", bg="thistle1", command=lambda:Sine())
sine.grid(row=3, column=4)

exp = tk.Button(cal, padx=16, width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="e", bg="thistle1", command=lambda:E())
exp.grid(row=3, column=5)

#============================================================================================================================================================================#

button1 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="1", bg="lavender", command=lambda:Click(1))
button1.grid(row=4, column=0)

button2 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="2", bg="lavender", command=lambda:Click(2))
button2.grid(row=4, column=1)

button3 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="3", bg="lavender", command=lambda:Click(3))
button3.grid(row=4, column=2)

Addition = tk.Button(cal, padx=16, pady=2, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="+", bg="thistle1", command=lambda:Click("+"))
Addition.grid(row=4, column=3)

cosine = tk.Button(cal, padx=16, width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="cos", bg="thistle1", command=lambda:Cosine())
cosine.grid(row=4, column=4)

factorial = tk.Button(cal, padx=16,  width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="x!", bg="thistle1", command=lambda:Factorial())
factorial.grid(row=4, column=5)

#============================================================================================================================================================================#

button0 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="0", bg="lavender", command=lambda:Click(0))
button0.grid(row=5, column=0)

button00 = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="00", bg="lavender", command=lambda:Click("00"))
button00.grid(row=5, column=1)

buttonDot = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text=".", bg="lavender", command=lambda:Click("."))
buttonDot.grid(row=5, column=2)

buttonEquals = tk.Button(cal, padx=16, bd=8, width=3, fg="black", font = ('arial',20,'bold'), text="=", bg="thistle1", command=EqualsInput)
buttonEquals.grid(row=5, column=3)

tan = tk.Button(cal, padx=16, width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="tan", bg="thistle1", command=lambda:Tan())
tan.grid(row=5, column=4)

ln = tk.Button(cal, padx=16,  width=3, bd=8, fg="black", font = ('arial',20,'bold'), text="ln", bg="thistle1", command=lambda:Ln())
ln.grid(row=5, column=5)

#============================================================================================================================================================================#

#start GUI window
cal.mainloop()
