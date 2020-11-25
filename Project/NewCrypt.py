import tkinter
def click():
    output.delete(1.0,tkinter.END)
    text = entry1.get()
    encrypted = ''
    for i in text:
        encrypted+=chr(ord(i)^123)
    output.insert(tkinter.INSERT, encrypted)
    return encrypted
def copy():
    r = tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(click())
    r.update()  # now it stays on the clipboard after the window is closed
    r.destroy()
def paste():
    clipboard = window.clipboard_get()
    entry1.insert(0, clipboard)

def clear():
    entry1.delete(0, tkinter.END)

#MAIN WINDOW
window = tkinter.Tk()
window.title("SM")
window.configure(bg = "black")
#text label:
label1 =tkinter.Label(window, text = "Enter something to encrypt or decrypt: ",bg = 'black', fg = 'white',font = "arial")
label1.grid(row = 0, column = 0, sticky='w') #sticky = is the direction of the alignmebt w ->west
#text entry box:
entry1 = tkinter.Entry(window, width = 80,bg = 'green', fg = 'black')
entry1.grid(row = 1, column = 0, sticky='w')
#submit button
button1 = tkinter.Button(window, text = 'SUBMIT',command = click).grid(row = 1, column = 1, sticky='e')
#copy button
button2 = tkinter.Button(window, text = 'COPY', width = 6,command = copy).grid(row = 2, column = 1, sticky = 'e')
#paste button
button3 = tkinter.Button(window, text = 'PASTE', width = 6,command = paste).grid(row = 1, column = 2, sticky = 'e')
#clear button
button4 = tkinter.Button(window, text = 'CLEAR',width = 6,command = clear).grid(row = 2, column = 2, sticky = 'e')

#another label
label1 =tkinter.Label(window, text = "New text: ",bg = 'black', fg = 'white',font = "arial")
label1.grid(row = 2, column = 0, sticky='w')
#output text
output = tkinter.Text(window,width = 60 , height = 6, bg = 'green', fg = 'black')
output.grid(row = 3, column = 0, sticky='w')

#keeps the windows opened until u close it
window.mainloop()
