from tkinter import*
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Currency Converter")
root.geometry("600x270")
root.resizable(False,False)
root.iconbitmap("C:\\Users\\91995\\Downloads\\icon.ico")

#------function definations-------
def show_data():
    amount = entry_1.get()
    c1 = check_1.get()
    c2 = check_12.get()
    url = "http://api.currencylayer.com/live?access_key=60c4b289605c27ad472ced1c3818adf4"

    if amount == "":
        messagebox.showerror("invalid","please fill some amount")
    elif check_12 == "":
        messagebox.showerror("invalid","please choose some currency")
    else:
        data = requests.get(url).json()
        currency = c1.strip()+c2.strip()
        amount = int(amount)
        cc = data["quotes"][currency]
        cur_con = cc*amount
        entry_12.insert(0,cur_con)
        text1.insert("end",f"{amount} USD equals to {cur_con} {c2} \n\n time updated on \t  {datetime.now()}")

def clear_val():
    entry_1.delete(0,"end")
    entry_12.delete(0,"end")
    text1.delete(1.0,"end")

#----function defination end-------


#----User Interface code start-----------
lbl_1 = Label(root,text="Amount",font=("vardana",10,"bold")).place(x=25,y=15)
entry_1 = Entry(root)
entry_1.place(x=25,y=40)
entry_12 = Entry(root)
entry_12.place(x=25,y=75)

lbl_2 = Label(root,text="USD Currency Converter",font=("vardana",10,"bold")).place(x=300,y=15)
check_1 = ttk.Combobox(root,values=("USD"),state="readonly")
check_1.place(x=300,y=40)
check_1.current(0)
check_12 = ttk.Combobox(root,values=("EUR","GBP","CAD","INR"),state="readonly")
check_12.place(x=300,y=75)

image_1 = Image.open("c:\\Users\\91995\\Downloads\\currency.png")
zoom = 0.5

size_x, size_y = tuple([int(zoom * x) for x in image_1.size])
img = ImageTk.PhotoImage(image_1.resize((size_x,size_y )))
lbl_img = Label(root,image=img)
lbl_img.place(x=190,y=35)

btn_1 = Button(root,text="Search",font=("vardhana",10,"bold"),bg="red",fg="white",command=show_data).place(x=30,y=135,relwidth=0.15)
btn_12 = Button(root,text="Clear",font=("vardhana",10,"bold"),bg="blue",fg="white",command=clear_val).place(x=30,y=190,relwidth=0.15)
text1 = Text(root,bd=2,relief=RIDGE)
text1.place(x=150,y=110,height=130,width=400)

root.mainloop()