from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="blanched almond")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")

calc=Frame(root)
calc.grid()

class Calculator():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.ckeck_sum=False
        self.operator=""
        self.result=False
        
    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum==".":
                if secondnum in firstnum:
                    return
            self.current= firstnum+secondnum
        self.display(self.current)
        
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
        
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0, value)
        
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="multi":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
        
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
        
    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)
        
    def cos(self):
        self.result=False
        self.current=math.cos(float(txtDisplay.get()))
        self.display(self.current)
        
    def tan(self):
        self.result=False
        self.current=math.tan(float(txtDisplay.get()))
        self.display(self.current)
    
    def sin(self):
        self.result=False
        self.current=math.sin(float(txtDisplay.get()))
        self.display(self.current)
    
    def tau(self):
        self.result=False
        self.current=math.tau
        self.display(self.current)
        
    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)
        
add_value=Calculator()

txtDisplay = Entry(calc,font=('arial',20,'bold'), bd=30, width = 28, 
                   bg='lavender',justify='right')
txtDisplay.grid(row=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
button=[]
for j in range(2,5):
    for k in range(3):
        button.append(Button(calc, width=5, height=2, font=('arial',20,'bold'),
                    bd=4, text=numberpad[i]))
        button[i].grid(row=j,column=k, pady =1)
        button[i]["command"]= lambda x=numberpad [i]: add_value.numberEnter(x)       
        i+=1
        
#=============================================================================#
                               #STANDARD PART#
#=============================================================================#

buttonClear=Button(calc, text="C", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=1,column=0, pady=1)

buttonAllClear=Button(calc, text="CE", width=5,height=2, font=('arial',20,
                     'bold'), bd=4,bg='lavender').grid(row=1,column=1, pady=1)

buttonSquare_root=Button(calc, text="√", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender').grid(row=1,column=2, pady=1)

buttonAddition=Button(calc, text="+", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = lambda: add_value.operation("add")).grid(row=1,column=3, pady=1)

buttonSubstract=Button(calc, text="-", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender', command = lambda: add_value.operation("sub")).grid(row=2,column=3, pady=1)

buttonMultiply=Button(calc, text="*", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = lambda: add_value.operation("multi")).grid(row=3,column=3, pady=1)

buttonDivision=Button(calc, text="÷", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = lambda: add_value.operation("divide")).grid(row=4,column=3, pady=1)

buttonZero=Button(calc, text="0", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = lambda: add_value.numberEnter(0)
                  ).grid(row=5,column=0, pady=1)

buttonDot=Button(calc, text=".", width=5,height=2, font=('arial',20,'bold'),
                 bd=4,bg='lavender', command = lambda: add_value.numberEnter(".")).grid(row=5,column=1, pady=1)

buttonPM=Button(calc, text="±", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=5,column=2, pady=1)

buttonEquals=Button(calc, text="=", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=5,column=3, pady=1)

#=============================================================================#
                               #SCIENTIFIC PART#
#=============================================================================#

buttonPi=Button(calc, text="Pi", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = add_value.pi).grid(row=1,column=4, pady=1)

buttonCos=Button(calc, text="cos", width=5,height=2, font=('arial',20,
                     'bold'), bd=4,bg='lavender', command = add_value.cos).grid(row=1,column=5, pady=1)

buttonTan=Button(calc, text="tan", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender', command = add_value.tan).grid(row=1,column=6, pady=1)

buttonSin=Button(calc, text="Sin", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender', command = add_value.sin).grid(row=1,column=7, pady=1)

#=============================================================================#

button2Pi=Button(calc, text="2Pi", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender', command = add_value.tau).grid(row=2,column=4, pady=1)

buttonCosh=Button(calc, text="cosh", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=2,column=5, pady=1)

buttonTanh=Button(calc, text="tanh", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=2, column=6, pady=1)

buttonSinh=Button(calc, text="sinh", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=2,column=7, pady=1)

#=============================================================================#

buttonLog=Button(calc, text="log", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender').grid(row=3,column=4, pady=1)

buttonExp=Button(calc, text="Exp", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=3,column=5, pady=1)

buttonMod=Button(calc, text="Mod", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=3,column=6, pady=1)

buttonE=Button(calc, text="e", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=3,column=7, pady=1)

#=============================================================================#

buttonLog2=Button(calc, text="log2", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender').grid(row=4,column=4, pady=1)

buttonDeg=Button(calc, text="deg", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=4,column=5, pady=1)

buttonAcosh=Button(calc, text="acosh", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=4,column=6, pady=1)

buttonAsinh=Button(calc, text="asinh", width=5,height=2, font=('arial',20,'bold'),
                  bd=4).grid(row=4,column=7, pady=1)

#=============================================================================#

buttonLog10=Button(calc, text="log10", width=5,height=2, font=('arial',20,
                       'bold'),bd=4,bg='lavender').grid(row=5,column=4, pady=1)

buttonLog1p=Button(calc, text="log1p", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=5,column=5, pady=1)

buttonExpm1=Button(calc, text="expm1", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=5,column=6, pady=1)

buttonLgamma=Button(calc, text="lgamma", width=5,height=2, font=('arial',20,'bold'),
                  bd=4,bg='lavender').grid(row=5,column=7, pady=1)

lblDisplay=Label(calc, text="Scientific Calculator", font=('arial',25,'bold'),
                  justify = 'center')
lblDisplay.grid(row=0, column =4,columnspan =4)

#=============================================================================#

#=============================================================================#
                           #MENU & FUNCTIONS#
#=============================================================================#

def Exit():
    Exit=tkinter.messagebox.askyesno("Scientific Calculator",
                                     "Confirm if you want to exit")
    if Exit > 0:
        root.destroy()
        return
    
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("885x568+0+0")
    
def Standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")

menubar=Menu(calc)

filemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Standard", command = Standard)
filemenu.add_command(label="Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command = Exit)

editmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")

helpmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")


root.configure(menu=menubar)
root.mainloop()
