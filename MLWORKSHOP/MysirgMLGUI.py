from tkinter import *






if __name__ == '__main__':
    root=Tk()
    root.geometry('600x500')
    root.title("Salary Prediction")
    Label(text='Welcome to Salary Prediction using ML',font='lucida 18 bold').pack()
    f1=Frame(root,bg='red',borderwidth=8,relief=SUNKEN,height='5',width='10')
    f1.pack(padx=60,pady=60,side=LEFT)
    l1=Label(f1,text="Enter experiences :").pack()

    root.mainloop()