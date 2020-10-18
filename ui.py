from tkinter import *
master = Tk()
master.config(bg ="#ff3377")
sv_result = StringVar()
def press():
    tx = open("text.txt", "a")
    tx.write(txt1.get()+" "+
    txt2.get()+" "+
    txt3.get()+"\n")
    sv_result.set("succesfully")

Label(master, text = "name", bg = "#ff3377", fg = "#ffffff").grid(row = 0, column = 0)
txt1 = Entry(master, bg = "#ff3377")
txt1.grid(row = 0, column = 1)
Label(master, text = "familly", bg = "#ff3377", fg = "#ffffff").grid(row = 1, column = 0)
txt2 = Entry(master, bg = "#ff3377")
txt2.grid(row = 1, column = 1)
Label(master, text = "phone", bg = "#ff3377", fg = "#ffffff").grid(row = 2, column = 0)
txt3 = Entry(master, bg = "#ff3377")
txt3.grid(row = 2, column = 1)

Button(master, bg = "#00ff00", fg = "#ffffff", text = "send", command = press).grid(row = 3, column = 0)

Button(master, bg = "#ff0000", fg = "#ffffff", text = "Exit").grid(row = 3, column = 1)

Label(master, textvariable =sv_result, bg = "#ff3377", fg = "#ffffff").grid(row = 4, column = 0)





master.mainloop()