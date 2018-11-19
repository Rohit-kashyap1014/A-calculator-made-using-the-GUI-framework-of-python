from tkinter import *
import parser

calc = Tk()
calc.title('Calculator')

#get the user input and place it in the textfield
i = 0
def obt_variables(num):
    global i
    display.insert(i,num)
    i+=1

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_every()
        display.insert(0,result)
    except Exception:
        clear_every()
        display.insert(0,"Error")

def do_operations(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length


def clear_every():
    display.delete(0,END)

def back():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_every()
        display.insert(0,new_string)
    else:
        clear_every()
        display.insert(0,"Error")

#adding the input field
display = Entry(calc)
display.grid(row=1,columnspan=6,sticky=W+E)

#adding buttons to the calculator

Button(calc,text="1",command = lambda :obt_variables(1)).grid(row=2,column=0)
Button(calc,text="2",command = lambda :obt_variables(2)).grid(row=2,column=1)
Button(calc,text="3",command = lambda :obt_variables(3)).grid(row=2,column=2)

Button(calc,text="4",command = lambda :obt_variables(4)).grid(row=3,column=0)
Button(calc,text="5",command = lambda :obt_variables(5)).grid(row=3,column=1)
Button(calc,text="6",command = lambda :obt_variables(6)).grid(row=3,column=2)

Button(calc,text="7",command = lambda :obt_variables(7)).grid(row=4,column=0)
Button(calc,text="8",command = lambda :obt_variables(8)).grid(row=4,column=1)
Button(calc,text="9",command = lambda :obt_variables(9)).grid(row=4,column=2)

#adding other buttons to the calculator
Button(calc,text="AC",command=lambda :clear_every()).grid(row=5,column=0)
Button(calc,text="0",command = lambda :obt_variables(0)).grid(row=5,column=1)
Button(calc,text="=",command=lambda :calculate()).grid(row=5,column=2)


Button(calc,text="+",command= lambda :do_operations("+")).grid(row=2,column=3)
Button(calc,text="-",command= lambda :do_operations("-")).grid(row=3,column=3)
Button(calc,text="*",command= lambda :do_operations("*")).grid(row=4,column=3)
Button(calc,text="/",command= lambda :do_operations("/")).grid(row=5,column=3)

# adding new operations
Button(calc,text="pi",command= lambda :do_operations("*3.14")).grid(row=2,column=4)
Button(calc,text="%",command= lambda :do_operations("%")).grid(row=3,column=4)
Button(calc,text="(",command= lambda :do_operations("(")).grid(row=4,column=4)
Button(calc,text="exp",command= lambda :do_operations("**")).grid(row=5,column=4)

Button(calc,text="<-",command= lambda :back()).grid(row=2,column=5)
Button(calc,text="x!").grid(row=3,column=5)
Button(calc,text=")",command= lambda :do_operations(")")).grid(row=4,column=5)
Button(calc,text="^2",command= lambda :do_operations("**2")).grid(row=5,column=5)


calc.mainloop()