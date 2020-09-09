from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Student:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Computing Grades and Database")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() -
             self.root.winfo_reqwidth()) / 200
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 6
        self.root.geometry("1345x495+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # ============================= Title Area =======================================================

        self.lbl_title = Label(
            self.root, text="Computing Subject and Grades System", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=10)
        self.lbl_title.pack(side=TOP, fill=X)

        # =============================== Input Frame ===================================================

        self.input_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.input_frame.place(x=0, y=55, width=1345, height=206)

        # ======================================= Search Area =============================================

        # Space

        self.space_search = Label(
            self.input_frame, text="", bg="navy", fg="white").grid(row=0, column=3, padx=15)

        # Student Label and Entry

        self.stdID_lbl = Label(
            self.input_frame, text="Student ID: ", bg="navy", fg="white", font=("bold", 14)).grid(row=0, column=1)

        self.stdID = StringVar()
        self.stdID_entry = Entry(
            self.input_frame, textvariable=self.stdID, width=15, bd=5, relief=SUNKEN, font=("bold", 15))
        self.stdID_entry.grid(row=0, column=2, padx=10, pady=15)

        # Search Label and Entry

        self.lbl_search = Label(
            self.input_frame, text="Search Name: ", bg="navy", fg="white", font=("bold", 14)).grid(row=0, column=4)

        self.search = StringVar()
        self.search_entry = Entry(
            self.input_frame, textvariable=self.search, width=11, bd=5, relief=SUNKEN, font=("bold", 15))
        self.search_entry.grid(row=0, column=5, padx=8, pady=15)

        # Button Search

        self.search_btn = Button(self.input_frame, text='Search', width=9, bg="#fc5c01", fg="white", bd=2, relief=GROOVE,
                                 font=("roboto sans-serif", 11, "bold"))
        self.search_btn.grid(row=0, column=6, pady=6)

        # ======================================= First Name Student =======================================

        self.fname_frame = LabelFrame(
            self.input_frame, text="First Name", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.fname_frame.place(x=0, y=64, width=190, height=100)

        # First Name
        self.fname = StringVar()
        self.fname_entry = Entry(
            self.fname_frame, textvariable=self.fname, width=12, bd=5, relief=SUNKEN, font=("bold", 15))
        self.fname_entry.grid(row=0, column=0, padx=20, pady=18)

        # ======================================= Lastname Student ======================================

        self.lname_frame = LabelFrame(
            self.input_frame, text="Last Name", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.lname_frame.place(x=193, y=64, width=205, height=100)

        # Last Name
        self.lname = StringVar()
        self.lname_entry = Entry(
            self.lname_frame, textvariable=self.lname, width=12, bd=5, relief=SUNKEN, font=("bold", 15))
        self.lname_entry.grid(row=0, column=0, padx=20, pady=18)

        # ======================================= Course Student ==============================================

        self.course_frame = LabelFrame(
            self.input_frame, text="Student Course", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.course_frame.place(x=400, y=64, width=220, height=100)

        # Course
        self.course = StringVar()
        self.course_entry = Entry(
            self.course_frame, textvariable=self.course, width=15, bd=5, relief=SUNKEN, font=("bold", 15))
        self.course_entry.grid(row=0, column=0, padx=20, pady=18)

        # ======================================= Subj ==============================================

        self.name_subj = LabelFrame(
            self.input_frame, text="Subject Name", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.name_subj.place(x=625, y=64, width=220, height=100)

        # Subject Name
        self.subject = StringVar()
        self.subject_entry = Entry(
            self.name_subj, textvariable=self.subject, width=15, bd=5, relief=SUNKEN, font=("bold", 15))
        self.subject_entry.grid(row=0, column=0, padx=20, pady=18)

        # ======================================= Midterm ==============================================

        self.mid_frame = LabelFrame(
            self.input_frame, text="Midterm", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.mid_frame.place(x=848, y=64, width=120, height=100)

        # Midterm
        self.mid = IntVar()
        self.mid_entry = Entry(
            self.mid_frame, textvariable=self.mid, width=5, bd=5, relief=SUNKEN, font=("bold", 15))
        self.mid_entry.grid(row=0, column=0, padx=20, pady=18)

        # =============================== Finals Frame ============================================

        self.final_frame = LabelFrame(
            self.input_frame, text="Finals", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.final_frame.place(x=970, y=64, width=120, height=100)

        # Finals
        self.final = IntVar()
        self.final_entry = Entry(
            self.final_frame, textvariable=self.final, width=5, bd=5, relief=SUNKEN, font=("bold", 15))
        self.final_entry.grid(row=0, column=0, padx=20, pady=18)

        # =================================== Total Grade ===========================================

        self.total_frame = LabelFrame(
            self.input_frame, text="Total Grade", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.total_frame.place(x=1093, y=64, width=120, height=100)

        # Total
        self.total = IntVar()
        self.total_entry = Entry(
            self.total_frame, textvariable=self.total, width=5, bd=5, relief=SUNKEN, font=("bold", 15))
        self.total_entry.grid(row=0, column=0, padx=25, pady=18)

        # ================================== Status Frame ==============================================

        self.status_frame = LabelFrame(
            self.input_frame, text="Status", fg="white", font=("bold", 13), bd=3, relief=RIDGE, bg="navy")
        self.status_frame.place(x=1215, y=64, width=120, height=100)

        # Status
        self.status = StringVar()
        self.status_entry = Entry(
            self.status_frame, textvariable=self.status, width=8, bd=5, relief=SUNKEN, font=("bold", 15))
        self.status_entry.grid(row=0, column=0, padx=6, pady=18)

        # ========================== Buttons Area =======================================================

        # Buttons and Frame
        self.btn_frame = Frame(
            self.root, bd=5, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=1010, y=260, width=335, height=235)

        # Spacing
        self.spacing_btn = Label(self.input_frame, text='',
                                 bg="navy", fg="white").grid(row=0, column=0, sticky=W, padx=20, pady=15)

        # Save
        self.save_btn = Button(self.btn_frame, command=self.save, text='Save', width=30, height=1, bd=2, relief=GROOVE, bg="#fc5c01", fg="white",
                               font=("roboto sans-serif", 13, "bold"))
        self.save_btn.grid(row=0, column=0, pady=7)

        # Change
        self.edit_btn = Button(self.btn_frame, text='Change', command=self.update, width=30, height=1, bd=2, relief=GROOVE, bg="#fc5c01", fg="white",
                               font=("roboto sans-serif", 13, "bold"))
        self.edit_btn.grid(row=1, column=0, pady=5)

        # Delete
        self.delete_btn = Button(self.btn_frame, text='Delete', command=self.deleted, width=30, height=1, bd=2, relief=GROOVE, bg="#fc5c01", fg="white",
                                 font=("roboto sans-serif", 13, "bold"))
        self.delete_btn.grid(row=2, column=0, pady=5)

        # Clear
        self.clear_btn = Button(self.btn_frame, command=self.clear, text='Clear', width=30, height=1, bg="#fc5c01", fg="white", bd=2, relief=GROOVE,
                                font=("roboto sans-serif", 13, "bold"))
        self.clear_btn.grid(row=3, column=0, padx=8, pady=5)

        # Compute
        self.comp_btn = Button(self.btn_frame, text='Compute', width=30, command=self.compute, height=1, bg="#fc5c01", fg="white", bd=2, relief=GROOVE,
                               font=("roboto sans-serif", 13, "bold"))
        self.comp_btn.grid(row=4, column=0, pady=5)

        # ===================================== Tree View Table ==============================================

        # Pinaka Frame ng Table
        self.tree_table_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.tree_table_frame.place(x=0, y=260, width=1010, height=235)

        # Table or Tree View Frame
        self.list_frame = Frame(
            self.tree_table_frame, bd=2, relief=RIDGE, bg="navy")
        self.list_frame.place(x=0, y=0, width=1004, height=229)

        # Treeview Scrollbar
        scroll_x = Scrollbar(self.list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.list_frame, orient=VERTICAL)

        # Treeview
        self.data_list = ttk.Treeview(self.list_frame, height=12, columns=("studentID",
                                                                           "fname", "lname", "course", "subject", "midterm", "final", "total", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.data_list.configure(yscrollcommand=scroll_x.set)
        scroll_x.configure(command=self.data_list.xview)

        self.data_list.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=self.data_list.yview)

        self.data_list.heading("studentID", text="Student ID")
        self.data_list.heading("fname", text="First Name")
        self.data_list.heading("lname", text="Last Name")
        self.data_list.heading("course", text="Course")
        self.data_list.heading("subject", text="Subject Name")
        self.data_list.heading("midterm", text="Midterm")
        self.data_list.heading("final", text="Final")
        self.data_list.heading("total", text="Total")
        self.data_list.heading("status", text="Status")

        self.data_list['show'] = 'headings'

        self.data_list.column("studentID", width=110)
        self.data_list.column("fname", width=80)
        self.data_list.column("lname", width=80)
        self.data_list.column("course", width=106)
        self.data_list.column("subject", width=126)
        self.data_list.column("midterm", width=20)
        self.data_list.column("final", width=20)
        self.data_list.column("total", width=20)
        self.data_list.column("status", width=50)

        self.data_list.bind('<ButtonRelease-1>', self.select_item)

        self.data_list.pack(fill=BOTH, expand=1)

        self.populate_data()

    # =================================== Database Function Here ===========================================

    def save(self):

        con = pymysql.connect(
            host="localhost", user="root", password="", database="student")
        cur = con.cursor()

        cur.execute(
            "insert into grades (firstname ,lastname, course, subject, midterm, finals, total, status) values(%s,%s,%s,%s,%s,%s,%s,%s)",
            (self.fname.get(),
             self.lname.get(),
             self.course.get(),
             self.subject.get(),
             self.mid.get(),
             self.final.get(),
             self.total.get(),
             self.status.get()
             ))
        con.commit()
        self.populate_data()
        con.close()
        messagebox.showinfo("Success", "Adding Subject Succesfully")
        self.clear()

    def populate_data(self):

        con = pymysql.connect(
            host="localhost", user="root", password="", database="student")
        cur = con.cursor()

        cur.execute("select * from grades")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.data_list.delete(*self.data_list.get_children())
            for row in rows:
                self.data_list.insert('', END, values=row)
            con.commit()
        con.close()

    def select_item(self, ev):

        cursor_row = self.data_list.focus()
        contents = self.data_list.item(cursor_row)
        row = contents['values']
        self.stdID.set(row[0])
        self.fname.set(row[1])
        self.lname.set(row[2])
        self.course.set(row[3])
        self.subject.set(row[4])
        self.mid.set(row[5])
        self.final.set(row[6])
        self.total.set(row[7])
        self.status.set(row[8])

    def update(self):

        con = pymysql.connect(
            host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute(
            "update grades set firstname=%s, lastname=%s, course=%s, subject=%s, midterm=%s, finals=%s, total=%s, status=%s where stdid=%s",
            (
                self.fname.get(),
                self.lname.get(),
                self.course.get(),
                self.subject.get(),
                self.mid.get(),
                self.final.get(),
                self.total.get(),
                self.status.get(),
                self.stdID.get()
            ))
        con.commit()
        messagebox.showinfo("Success", "Update Successfuly")
        self.populate_data()
        self.clear()
        con.close()

    def deleted(self):

        con = pymysql.connect(
            host="localhost", user="root", password="", database="student")
        cur = con.cursor()
        cur.execute("delete from grades where stdid=%s", self.stdID.get())

        d = messagebox.askyesno(
            'Gadgets', 'Do you want to delete this file ')

        self.clear()
        con.commit()

        if d > 0:

            self.clear()
            self.populate_data()

        con.close()

    def compute(self):

        # First

        self.total_entry = float(self.mid.get() +
                                 self.final.get()
                                 ) / 2
        self.total.set(self.total_entry)

    def clear(self):

        # =====

        self.fname_entry.delete(0, END)

        self.lname_entry.delete(0, END)

        self.course_entry.delete(0, END)

        self.subject_entry.delete(0, END)

        self.stdID_entry.delete(0, END)

        # =====

        # =====

        self.mid_entry.delete("0", END)

        # =====

        self.final_entry.delete("0", END)

        # =====

        self.total.set("0")

        # =====

        self.status_entry.delete(0, END)


root = Tk()
obj = Student(root)
root.deiconify()
root.mainloop()
