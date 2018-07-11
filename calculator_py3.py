from tkinter import *
from tkinter import font
# by: Raj Chauhan

input = ""
output = ""

def button0():
    global input
    input = input+"0"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button1():
    global input
    input = str(input)+"1"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button2():
    global input
    input = str(input)+"2"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button3():
    global input
    input = str(input)+"3"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button4():
    global input
    input = str(input)+"4"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button5():
    global input
    input = str(input)+"5"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button6():
    global input
    input = str(input)+"6"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button7():
    global input
    input = str(input)+"7"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button8():
    global input
    input = str(input)+"8"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def button9():
    global input
    input = str(input)+"9"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonADD():
    global input
    if input == "":
        input = input
    elif input[len(input) - 1] == "/" or input[len(input) - 1] == "*" or input[len(input) - 1] == "+":
        input = input
    else:
        input = str(input)+"+"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonSUB():
    global input
    input = str(input)+"-"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonMUL():
    global input
    if input == "":
        input = input
    elif input[len(input) - 1] == "/" or input[len(input) - 1] == "*" or input[len(input) - 1] == "+" or input[
            len(input) - 1] == "-":
        input = input
    else:
        input = str(input)+"*"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonDIV():
    global input
    if input == "":
        input = input
    elif input[len(input) - 1] == "/" or input[len(input) - 1] == "*" or input[len(input) - 1] == "+" or input[
            len(input) - 1] == "-":
        input = input
    else:
        input = str(input)+"/"
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonEQL():
    global input
    global output
    canvas.delete("all")
    if input == "":
        input = input
        canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)
    elif input[len(input)-1] == "/" or input[len(input) - 1] == "*" or input[len(input) - 1] == "+" or input[
            len(input) - 1] == "-" or input[len(input) - 1] == ".":
        input = input
        canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)
    else:
        output = eval(input)
        if len(str(output)) > 11:
            canvas.create_text(0, 100, text=str(output), font=('Helvetica', '40'), anchor=SW)
        else:
            canvas.create_text(320, 100, text=str(output), font=('Helvetica', '40'), anchor=SE)
        input = str(output)

def buttonDOT():
    global input
    if input == "":
        input = str(input)+"."
        canvas.delete("all")
        canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)
    elif input[len(input)-1] == ".":
        input = input
        canvas.delete("all")
        canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)
    else:
        input = str(input)+"."
        canvas.delete("all")
        canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)

def buttonCLR():
    global input
    input = ""
    output = ""
    canvas.delete("all")

def buttonBACKSPACE():
    global input
    input = input[:-1]
    canvas.delete("all")
    canvas.create_text(320, 100, text=str(input), font=('Helvetica', '40'), anchor=SE)


frame = Tk()
frame.title("Sabhka Calculator")
frame.geometry("340x520")

font_size = font.Font(family='Helvetica', size=32, weight='bold')
font_size_clr_backspace = font.Font(family='Helvetica', size=20, weight='bold')


# Canvas
canvas = Canvas(frame, width=330, height=100, bg="white")
canvas.grid(row=0, column=0, columnspan=4)


# Buttons
button_7 = Button(frame, text="7", command=button7, activebackground="white", activeforeground="blue")
button_7.grid(row=1, column=0, rowspan=2)
button_7['font'] = font_size

button_8 = Button(frame, text="8", command=button8, activebackground="white", activeforeground="blue")
button_8.grid(row=1, column=1, rowspan=2)
button_8['font'] = font_size

button_9 = Button(frame, text="9", command=button9, activebackground="white", activeforeground="blue")
button_9.grid(row=1, column=2, rowspan=2)
button_9['font'] = font_size

button_div = Button(frame, text="/", command=buttonDIV, padx=9.5, activebackground="white", activeforeground="blue")
button_div.grid(row=1, column=3, rowspan=2)
button_div['font'] = font_size

button_4 = Button(frame, text="4", command=button4, activebackground="white", activeforeground="blue")
button_4.grid(row=3, column=0, rowspan=2)
button_4['font'] = font_size

button_5 = Button(frame, text="5", command=button5, activebackground="white", activeforeground="blue")
button_5.grid(row=3, column=1, rowspan=2)
button_5['font'] = font_size

button_6 = Button(frame, text="6", command=button6, activebackground="white", activeforeground="blue")
button_6.grid(row=3, column=2, rowspan=2)
button_6['font'] = font_size

button_mul = Button(frame, text="X", command=buttonMUL, activebackground="white", activeforeground="blue")
button_mul.grid(row=3, column=3, rowspan=2)
button_mul['font'] = font_size

button_1 = Button(frame, text="1", command=button1, activebackground="white", activeforeground="blue")
button_1.grid(row=5, column=0, rowspan=2)
button_1['font'] = font_size

button_2 = Button(frame, text="2", command=button2, activebackground="white", activeforeground="blue")
button_2.grid(row=5, column=1, rowspan=2)
button_2['font'] = font_size

button_3 = Button(frame, text="3", command=button3, activebackground="white", activeforeground="blue")
button_3.grid(row=5, column=2, rowspan=2)
button_3['font'] = font_size

button_sub = Button(frame, text="-", command=buttonSUB, padx=8.5, activebackground="white", activeforeground="blue")
button_sub.grid(row=5, column=3, rowspan=2)
button_sub['font'] = font_size

button_dot = Button(frame, text=".", command=buttonDOT, padx=7, activebackground="white", activeforeground="blue")
button_dot.grid(row=7, column=0, rowspan=2)
button_dot['font'] = font_size

button_0 = Button(frame, text="0", command=button0, activebackground="white", activeforeground="blue")
button_0.grid(row=7, column=1, rowspan=2)
button_0['font'] = font_size

button_eql = Button(frame, text="=", command=buttonEQL, activebackground="white", activeforeground="blue")
button_eql.grid(row=7, column=2, rowspan=2)
button_eql['font'] = font_size

button_add = Button(frame, text="+", command=buttonADD, padx=3, activebackground="white", activeforeground="blue")
button_add.grid(row=7, column=3, rowspan=2)
button_add['font'] = font_size

button_clr = Button(frame, text="CLEAR", command=buttonCLR, activebackground="white", activeforeground="blue")
button_clr.grid(row=9, column=0, columnspan=2)
button_clr['font'] = font_size_clr_backspace

button_backspace = Button(frame, text="Back space", command=buttonBACKSPACE, activebackground="white", activeforeground="blue")
button_backspace.grid(row=9, column=2, columnspan=2)
button_backspace['font'] = font_size_clr_backspace

frame.mainloop()


