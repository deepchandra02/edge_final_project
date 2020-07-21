import tkinter
window = tkinter.Tk()
# window title name
window.title("Snake Game")

window.geometry('600x600')

heading = tkinter.Label(window, text="Welcome!", font=("Arial Bold",50)).pack()

def instruc():
    info ="1. Moves up when pressing “w”\n2. Moves down with “s”\n3. Moves right with “d”\n4. Moves left with “a”.\n5. Eat the food to grow in size.\n6. Moves at a speed that the player has an option to modify (increase-decrease) every time he plays.\n8. Different speeds have their high scores."
    m = tkinter.messagebox.showinfo("Instructions", info)
    m.pack()

bt1 = tkinter.Button(window, text="New Game", bg="blue", fg="white").pack()
bt2 = tkinter.Button(window, text="Scores", bg="blue", fg="white").pack()
bt3 = tkinter.Button(window, text="Options", bg="blue", fg="white").pack()
bt4 = tkinter.Button(window, text="Instructions", bg="blue", fg="white", command=instruc).pack()
window.mainloop()
