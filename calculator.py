print('Program startded...')
import math
from tkinter import *
from tkinter.messagebox import *

# -----------------------------------variable--------------------------------------------
font = ('Verdana', 22, 'bold')


# ----------------------------------important--------------------------------------------
def per():
    try:
        ex = textField.get()
        f = eval(ex) / 100
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def qsq():
    try:
        ex = textField.get()
        c = float(ex)
        f = c ** (1 / 3)  # Calculate the cube root
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def sq():
    try:
        ex = textField.get()
        c = float(ex)
        f = math.sqrt(c)
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def sinn():
    try:
        ex = textField.get()
        c = float(ex)
        f = math.sin(c)
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def coss():
    try:
        ex = textField.get()
        c = float(ex)
        f = math.cos(c)
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def tann():
    try:
        ex = textField.get()
        c = float(ex)
        f = math.tan(c)
        textField.delete(0, END)
        textField.insert(0, f)
    except:
        e = 'Invalid input...Please Click to AC and try again'
        textField.delete(0, END)
        textField.insert(0, e)


def mod():
    try:
        ex = textField.get()
        c = float(ex)
        f = math.gamma(c + 1)
        textField.delete(0, END)
        textField.insert(0, f)
    except Exception as e:
        textField.delete(0, END)
        textField.insert(0, e)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


def click_btn_function(event):
    print("btn clicked")  # for internal use if button click the shoe click into compler
    b = event.widget  # store the faith button of input button
    text = b['text']  # store the b text valur
    print(text)  # print the b text to compiler
    if text == '=':  # if the text value is = the exicute
        try:
            ex = textField.get()  # ex=expresson get the whole expression fron textField
            answer = eval(ex)  # Evaluate the expression using eval
            textField.delete(0, END)  # delete existing expression
            textField.insert(0, answer)  # print the answer
        except Exception as e:
            print("Error...", e)
            showerror("Error...", e)
        return;
    textField.insert(END, text)


# -------------------------------------------Creating a window------------------------------------------

window = Tk()
window.title('My Calculator')  # create title
window.geometry('760x550')  # mentain the size of the window

# -------------------------------------------picture---------------------------------------------------
'''
pic = PhotoImage(file='D:\pythonProject\cal.jpg')
headingLabel = Label(window, image=pic)
headingLabel.pack(side=TOP)
'''
# ----------------------------------------Heading lable----------------------------------------------

heading = Label(window, text="My Calculator", font=font,
                underline=0)  # Heading of the calculator underline 0 -->first string
heading.pack(side=TOP)

# ----------------------------------------textfield--------------------------------------------------

textField = Entry(window, font=font, fg="blue",
                  justify=CENTER)  # input output display of the calculator justify-->the text printing formate id center
textField.pack(side=TOP, pady=10, fill=X)

# ---------------------------------------------Buttons---------------------------------------------------------

ButtonFram = Frame(window)  # creatinf logical fram in existing window
ButtonFram.pack(side=TOP)
'''
btn1=Button(ButtonFram,text="1",font=font)
btn1.pack(side=TOP)
btn2=Button(ButtonFram,text="2",font=font)
btn2.pack(side=TOP)
'''
temp = 1  # declear keyboard key number
for i in range(0, 3):  # working for row
    for j in range(0, 3):  # working for column
        btn = Button(ButtonFram, text=str(temp), font=font, width=5, relief='raised',cursor="hand2")
        btn.grid(row=i, column=j, pady=4, padx=4)  # align the button using grid function
        temp = temp + 1  # keyboard number increase by 1
        btn.bind('<Button-1>',
                 click_btn_function)  # bind function attahed file if button-1 click -->left key of mouse and the object pass on click_btn_function
zerobtn = Button(ButtonFram, text='0', font=font, width=5, relief='solid',cursor="hand2")
zerobtn.grid(row=3, column=0, pady=4, padx=4)

dotbtn = Button(ButtonFram, text='.', font=font, width=5, fg="red", relief='solid',cursor="hand2")
dotbtn.grid(row=3, column=1, pady=4, padx=4)

equalbtn = Button(ButtonFram, text='=', font=font, width=5, fg="blue", relief='solid',cursor="hand2")
equalbtn.grid(row=3, column=2, pady=4, padx=4)

plusbtn = Button(ButtonFram, text='+', font=font, width=5, fg="red", relief='solid',cursor="hand2")
plusbtn.grid(row=0, column=3, pady=4, padx=4)

minusbtn = Button(ButtonFram, text='-', font=font, width=5, fg="red", relief='solid',cursor="hand2")
minusbtn.grid(row=1, column=3, pady=4, padx=4)

multbtn = Button(ButtonFram, text='*', font=font, width=5, fg="red", relief='solid',cursor="hand2")
multbtn.grid(row=2, column=3, pady=4, padx=4)

dividbtn = Button(ButtonFram, text='/', font=font, width=5, fg="red", relief='solid',cursor="hand2")
dividbtn.grid(row=3, column=3, pady=4, padx=4)

clrbtn = Button(ButtonFram, text='<--', font=font, width=11, fg="red", relief='solid', command=clear,cursor="hand2")
clrbtn.grid(row=4, column=0, pady=4, padx=4, columnspan=2)

allclrbtn = Button(ButtonFram, text='AC', font=font, width=11, fg="red", relief='solid', command=all_clear,cursor="hand2")
allclrbtn.grid(row=4, column=2, pady=4, padx=4, columnspan=2)

modbtn = Button(ButtonFram, text='X!', font=font, width=11, fg="green", relief='solid', command=mod,cursor="hand2")
modbtn.grid(row=5, column=0, pady=4, padx=4, columnspan=2)

# ---------------------------------------------------SciButton------------------------------------------------------------

sinbtn = Button(ButtonFram, text='Sin', font=font, width=5, fg="green", relief='solid', command=sinn,cursor="hand2")
sinbtn.grid(row=0, column=4, pady=4, padx=4)

cosbtn = Button(ButtonFram, text='Cos', font=font, width=5, fg="green", relief='solid', command=coss,cursor="hand2")
cosbtn.grid(row=1, column=4, pady=4, padx=4)

tanbtn = Button(ButtonFram, text='tan', font=font, width=5, fg="green", relief='solid', command=tann,cursor="hand2")
tanbtn.grid(row=2, column=4, pady=4, padx=4)

sqrbtn = Button(ButtonFram, text='√', font=font, width=5, fg="green", relief='solid', command=sq,cursor="hand2")
sqrbtn.grid(row=3, column=4, pady=4, padx=4)

qubrotbtn = Button(ButtonFram, text='3√', font=font, width=5, fg="green", relief='solid', command=qsq,cursor="hand2")
qubrotbtn.grid(row=4, column=4, pady=4, padx=4)

pertbtn = Button(ButtonFram, text='%', font=font, width=17, fg="green", relief='solid', command=per,cursor="hand2")
pertbtn.grid(row=5, column=2, pady=4, padx=4, columnspan=3)

# Buinding all button 1
plusbtn.bind('<Button-1>', click_btn_function)  # Buinding function it binds the function with left key of the mouse
minusbtn.bind('<Button-1>', click_btn_function)
multbtn.bind('<Button-1>', click_btn_function)
dividbtn.bind('<Button-1>', click_btn_function)
zerobtn.bind('<Button-1>', click_btn_function)
dotbtn.bind('<Button-1>', click_btn_function)
equalbtn.bind('<Button-1>', click_btn_function)

# Buinding all button 2
'''
sinbtn.bind('<Button-1>',click_btn_function)
cosbtn.bind('<Button-1>',click_btn_function)
tanbtn.bind('<Button-1>',click_btn_function)
'''
window.mainloop()
