from tkinter import * 
import tkinter.messagebox
import string
import random

class AppOnly():
    def __init__(self, root):
        self.root = root
        self.root.title('Random Password Generator')

        canvas = Canvas(root, width=500, height=300)
        canvas.grid(columnspan=3, rowspan=3)

        # Logo
        LogoLabel = Label(root, text="Random\nPassword Generator", 
            font=("Raleway",18,"bold"))
        LogoLabel.place(x=108, y=10)

        #var 
        LenghtOnly = StringVar()

        #intruction
        intruk = Label(root, text="Masukan Berapa Digit\nPanjang Password", font=("Ralleway", 10,))
        intruk.place(x=170, y=160)

        #textbox
        def Textbox(lenght):
            self.LabelTb = Label(root, text="Password kamu",
                font=("Ralleway", 10,)).place(x=196, y=73)
            self.textBox = Text(root, height=3, width=34, )
            self.textBox.insert(1.0, lenght)
            self.textBox.tag_configure("center", justify="center")
            self.textBox.tag_add("center", 1.0, "end")
            self.textBox.place(x=108, y=95)
            
        # func
        def Reset():
            LenghtOnly.set("")
            return
        
        def Exit():
            Exit = tkinter.messagebox.askyesno(
                "Random Password Generator", "Kamu Yakin Mau Keluar ?")
            if Exit > 0:
                root.destroy()
                return

        def lenghtOnly():
            item = LenghtOnly.get()
            
            if item.isdigit():

                #items
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                symbols = string.punctuation    

                all = lower + upper + num + symbols
                temp = random.sample(all,int(item))
                password = "".join(temp)
                Textbox(password)

                tkinter.messagebox.showinfo(
                "Correct Data", "Mantap bro :v")
                return True
            else:
                tkinter.messagebox.showwarning(
                "Wrong Data", "Goblok :v")
                LenghtOnly.set("")
                return False

        #Entry
        self.Lenght = Entry(root, font=("Raleway", 10), 
            textvariable=LenghtOnly, width=8).place(x=210, y=205)          

        #Button
        self.SumbitButton = Button(root,text="Sumbit",
            command=lenghtOnly,
            font=("Raleway", 10)).place(x=210, y=240)

        self.ExitButton = Button(root, text="Exit",
            command=Exit,
            font=("Raleway", 10)).place(x=290, y=240)

        self.ResetButton = Button(root, text="Reset",
            command=Reset,
            font=("Raleway", 10)).place(x=140, y=240)

if __name__ == "__main__":
    root = Tk()
    app = AppOnly(root)
    root.mainloop()