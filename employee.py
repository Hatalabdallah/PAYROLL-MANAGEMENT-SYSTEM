from tkinter import *
from tkinter.ttk import Combobox
class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System | Developed by Abdallah Ddumba Kato")
        self.root.geometry('1350x700+0+0')
        self.root.config(bg = 'white')
        title = Label(self.root, text="Employee Payroll Management System", font=('times new roman', 30, 'bold'), bg="#262626", fg='white', anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        #----------------------Frame1-----------------------------------
        Frame1 = Frame(self.root,bd = 3, relief = RIDGE, bg = 'white')
        Frame1.place(x = 10, y = 70, width = 750, height = 650)
        title2 = Label(Frame1, text="Employee Details", font=('times new roman', 20), bg="lightgray", fg='black', anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        lb1_code = Label(Frame1, text="Employee Code", font=('times new roman', 20), bg="white", fg='black').place(x=10, y=70)
        lb1_code = Entry(Frame1,font=('times new roman', 17), bg="lightyellow", fg='black').place(x=220, y=70, width=200)
        btn_search = Button(Frame1, text="Search", font=('times new roman', 15), bg="lightgray", fg='black').place(x=430, y=70, height=35)

        #Row1------------------
        lb1_designation = Label(Frame1, text="Designation:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=120)
        txt_designation = Entry(Frame1, text="Designation", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=170, y=125, width=200)

        lb1_Date_of_Joining = Label(Frame1, text="D.O.J:", font=('times new roman', 17), bg="white", fg='black').place(x=380, y=120)
        txt_Date_of_Joining = Entry(Frame1, text="D.O.J", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=510, y=125)

        #Row2-----------------
        lb1_name = Label(Frame1, text="Name:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=170)
        txt_name = Entry(Frame1, text="Name", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=170, y=170, width=200)

        lb1_Date_of_Birth = Label(Frame1, text="D.O.B:", font=('times new roman', 17), bg="white", fg='black').place(x=380, y=170)
        txt_Date_of_Birth = Entry(Frame1, text="D.O.B", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=510, y=170)

        #Row3------------------
        lb1_age = Label(Frame1, text="Age:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=215)
        txt_age = Entry(Frame1, text="Age", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=170, y=215, width=200)

        lb1_Experience = Label(Frame1, text="Experience:", font=('times new roman', 17), bg="white", fg='black').place(x=380, y=215)
        txt_Experience = Entry(Frame1, text="Experience", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=510, y=215)

        #Row4------------------
        lb1_gender = Label(Frame1, text="Gender:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=260)
        combobox = Combobox(Frame1, values = ['Male', 'Female'],font=('times new roman', 15)).place(x=170, y=260, width=200)
        # txt_gender = Entry(Frame1, text="Gender", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=170, y=260, width=200)

        lb1_proof_ID = Label(Frame1, text="Proof ID:", font=('times new roman', 17), bg="white", fg='black').place(x=380, y=260)
        txt_Proof_ID = Entry(Frame1, text="Proof ID", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=510, y=260)

        #Row5------------------
        lb1_email = Label(Frame1, text="Email:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=305)
        txt_email = Entry(Frame1, text="Email", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=170, y=305, width=200)

        lb1_contact = Label(Frame1, text="Contact No:", font=('times new roman', 17), bg="white", fg='black').place(x=380, y=305)
        txt_contact = Entry(Frame1, text="Contact No", font=('times new roman', 15), bg="lightyellow", fg='black').place(x=510, y=305)

        #Row6--------------------------------------------------
        lb1_address = Label(Frame1, text="Address:", font=('times new roman', 17), bg="white", fg='black').place(x=10, y=350)
        txt_address = Text(Frame1,font=('times new roman', 15), bg="lightyellow", fg='black')
        txt_address.pack()
        txt_address.place(x=170, y=350, width=548, height=255)



        #-----------------------Frame2---------------------------------
        Frame2 = Frame(self.root,bd = 3, relief = RIDGE, bg = 'white')
        Frame2.place(x = 770, y = 70, width = 580, height = 300)


        #-----------------------Frame3----------------------------------
        Frame3 = Frame(self.root,bd = 3, relief = RIDGE, bg = 'white')
        Frame3.place(x = 770, y = 380, width = 580, height = 340) 

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()

