"""
Calculator in Python
"""
import tkinter as tk

def calculator(event):
    text = event.widget.cget("text")
    
    if text == '=':
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set(str(e))
    elif text == 'C':
        screen.set('')
    else:
        screen.set(screen.get()+text)
    
    

root =tk.Tk()
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

button_texts = [
    ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("/", 1, 3, 1),
    ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("*", 2, 3, 1),
    ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("-", 3, 3, 1),
    ("0", 4, 0, 1), (".", 4, 1, 1), ("C", 4, 2, 1), ("+", 4, 3, 1),
    ("=", 5, 0, 2),
]

for (text, row, column, columnspan) in button_texts:
    button = tk.Button(button_frame, text=text, font="lucida 15 bold", width=5, height=2)
    button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
    button.bind("<Button-1>", calculator)

root.mainloop()

"""
eval function -- to evaluate the expression 
tkinter -- for UI
root = tkinter.Tk()--to generate main window
root.title--set title of the main window

screen = tk.StringVar(): This line creates a 
Tkinter StringVar variable named screen. 

entry = tk.Entry(root, textvar=screen, font="lucida 20 bold") 
-----------------------------------
This line creates an Entry widget named entry that will be 
placed inside the root window. The textvar parameter is 
set to the screen StringVar, which means that the text 
displayed in the Entry widget will be controlled by the 
screen variable. 

entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)
---------------------------------------
This line uses the pack() geometry manager 
to add the Entry widget to the root window. 
The fill parameter is set to tk.X, which means 
the Entry widget will expand horizontally to fill
the available space. The ipadx, pady, and padx 
parameters set internal and external padding 
around the Entry widget to control its size 
and spacing within the window.

button_frame = tk.Frame(root)
---------------
This line creates a new Tkinter Frame widget. 
A Frame is a container widget that is used to group 
other widgets together. In this case, you are creating 
a Frame named button_frame that will be used to 
hold the buttons for your calculator.

button_frame.pack(): This line uses the pack() 
geometry manager to place the button_frame within 
the root window. The pack() method is used to add 
widgets to their parent container 
(in this case, the root window) and arrange them according 
to certain packing options. By calling pack() 
without any additional options, the frame will 
be added to the window, and it will try to occupy 
as much space as needed to accommodate 
its content (the buttons).

The button_texts list is a data structure that 
contains information about the buttons you want to 
create for your calculator. 
The button's label text.
The row position where the button should be placed within the grid.
The column position where the button should be placed within the grid.
The columnspan specifies how many columns the button should span.

The for loop then iterates through the button_texts 
list, creating a Tkinter Button widget for each tuple. 
"""
