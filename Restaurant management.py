from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():   #function make
    win = Tk()  
    app = LoginPage(win)  #class making
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurant Management System")

        # windows title
        self.title_label = Label(self.win, text="Restaurant Management",font=('Times and Roman',35,'bold'),bg="lightgray",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="lightgray",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        # login  text
        self.login_lb1 = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgray",font=('sans-serif',25,'bold'))
        self.login_lb1.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="lightgray",font=("sans-serif",18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        # label Enter username 
        self.entus_lb1 = Label(self.entry_frame,text="Enter Username: ",bg="lightgray",font=('sans-serif',15))
        self.entus_lb1.grid(row=0,column=0,padx=2,pady=2)

        # ==================== Variables ===================
        username = StringVar()
        password = StringVar()

        # =================================================

        self.entus_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        # label Enter password 
        self.entpass_lb1 = Label(self.entry_frame,text="Enter password: ",bg="lightgray",font=('sans-serif',15))
        self.entpass_lb1.grid(row=1,column=0,padx=2,pady=2)

        self.entpass_ent = Entry(self.entry_frame,font=('sans-serif',15),bd=6,textvariable=password)
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        # ================== functions ===============
        def check_login():
            """ this function will check login """
            if username.get() == "aashish" and password.get() == "1122Qwerty@":
                self.billing_btn.config(state="normal")
            else:
                pass # -----> Message box

        def reset():
            username.set("")
            password.set("")
        def billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        # ============================================
        

        #===================buttons ================

        self.button_frame = LabelFrame(self.entry_frame,text="option",font=('Arial',15),bg="lightgray",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn = Button(self.button_frame,text="Login",font=('Arial',12),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        
        self.billing_btn = Button(self.button_frame,text="Billing",font=('Arial',12),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=38,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=('Arial',12),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        # =============== ============================
class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1200x700+0+0")
        self.win.title("Restaurant Management System")

        # windows title
        self.title_label = Label(self.win, text="Restaurant Management",font=('Times and Roman',35,'bold'),bg="lightgray",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        # ***************** variable *******************
        bill_no = random.randint(100,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0

        # **********************************************
        
        # ============entry==============
        self.entry_frame = LabelFrame(self.win,text="Enter Details",background="lightgray",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=520,height=550)

        self.bill_no_lb1 = Label(self.entry_frame,text="Bill Number",font=('Arial',15),bg="lightgrey")
        self.bill_no_lb1.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=('Arial',15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")    #Bill no not generate

        self.cust_nm_lb1 = Label(self.entry_frame,text="Customer Name ",font=('Arial',15),bg="lightgrey")
        self.cust_nm_lb1.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Arial',15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lb1 = Label(self.entry_frame,text="Customer Contact ",font=('Arial',15),bg="lightgrey")
        self.cust_cot_lb1.grid(row=2,column=0,padx=2,pady=2)

        self.bill_cot_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Arial',15))
        self.bill_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lb1 = Label(self.entry_frame,text="Date ",font=('Arial',15),bg="lightgrey")
        self.date_lb1.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Arial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lb1 = Label(self.entry_frame,text="Item Purchased ",font=('Arial',15),bg="lightgrey")
        self.item_pur_lb1.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Arial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lb1 = Label(self.entry_frame,text="Item Quantity ",font=('Arial',15),bg="lightgrey")
        self.item_qty_lb1.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Arial',15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lb1 = Label(self.entry_frame,text="Cost of one ",font=('Arial',15),bg="lightgrey")
        self.cost_one_lb1.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=('Arial',15))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        # ****************** function **********************
        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tApna Restraunt")
            self.bill_txt.insert(END,"\n\t\t\t Street, Near Gateway omegacity,kharar")
            self.bill_txt.insert(END,"\n\t\t\t\tContact - +9122433927")
            self.bill_txt.insert(END,"\n --------------------------------------------------------------")
            self.bill_txt.insert(END,f"\n Bill Number {bill_no_tk.get()}")

        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) !=10):
                messagebox.showerror("Error!","Please enter all the fields correctly.")
            else:

                self.bill_txt.insert(END,f"\n Customer Contact : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\n Customer Name :{cust_cot.get()}")
                self.bill_txt.insert(END,f"\n Date :{date_pr.get()}")
                self.bill_txt.insert(END,"\n --------------------------------------------------------------")
                self.bill_txt.insert(END,"\nProduct Name\t\t     Quantity     \t\tPer Cost       \tTotal")
                self.bill_txt.insert(END,"\n --------------------------------------------------------------")

                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")

        def clear_func():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")
        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")

            self.bill_txt.delete("1.0",END)
            default_bill()

        def add_func():
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error!","Please enter all the fields correctly.",parent=self.win) 
            else:   
                qty = int(item_qty.get())
                cones = int(cone.get())
                total = qty * cones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t        {item_qty.get()}           Rs. \t\t{cone.get()}\t\t    Rs. {total} ")

        def total_func():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n ---------------------------------------------------------------")
            self.bill_txt.insert(END,f"\t\t\t\t\t\tGrand total : {self.grd_total}")
            self.bill_txt.insert(END,"\n ---------------------------------------------------------------")
            self.save_btn.config(state="normal")
        
        def save_func():
            user_choice = messagebox.askyesno("Confirm?",f"Do you want the bill {bill_no_tk.get()}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bills/"+str(self.bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}",parent=self.win)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill {bill_no_tk.get()} has been saved sucessfully!",parent=self.win)

            else:
                return

        # ********************************************************

        # -------------- Button ----------------------
        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Options",bg="lightgrey",font=("Arial",15))
        self.button_frame.place(x=20,y=280,width=392,height=200)

        self.add_btn = Button(self.button_frame,bd=3,text="Add",font=('Arial',12),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn = Button(self.button_frame,bd=3,text="Generate",font=('Arial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn = Button(self.button_frame,bd=3,text="Clear",font=('Arial',12),width=12,height=3,command=clear_func)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn = Button(self.button_frame,bd=3,text="Total",font=('Arial',12),width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn = Button(self.button_frame,bd=3,text="Reset",font=('Arial',12),width=12,height=3,command=reset_func)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn = Button(self.button_frame,bd=3,text="save",font=('Arial',12),width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        # ------------------------------------------------- 

        # +++++++++++++ calculator frame ++++++++++++++++++
        self.calc_frame = Frame(self.win,bd=8,background="lightgray",relief=GROOVE)
        self.calc_frame.place(x=570,y=110,width=550,height=262)

        self.num_ent = Entry(self.calc_frame,bd=15,background="lightgrey", textvariable= calc_var,font=('Arial',15),width=45,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=4)

        # IMPORTANT PART THIS CODE 
        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == "C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()

        self.btn7 = Button(self.calc_frame,bg="lightgray",text="7",width=10,height=1,font=('Arial',15))
        self.btn7.grid(row=1,column=0,padx=2,pady=4)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8 = Button(self.calc_frame,bg="lightgray",text="8",width=10,height=1,font=('Arial',15))
        self.btn8.grid(row=1,column=1,padx=2,pady=4)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9 = Button(self.calc_frame,bg="lightgray",text="9",width=10,height=1,font=('Arial',15))
        self.btn9.grid(row=1,column=2,padx=2,pady=4)
        self.btn9.bind("<Button-1>",press_btn)        

        self.btnadd = Button(self.calc_frame,bg="lightgray",text="+",width=10,height=1,font=('Arial',15))
        self.btnadd.grid(row=1,column=3,padx=2,pady=4)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4 = Button(self.calc_frame,bg="lightgray",text="4",width=10,height=1,font=('Arial',15))
        self.btn4.grid(row=2,column=0,padx=2,pady=4)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5 = Button(self.calc_frame,bg="lightgray",text="5",width=10,height=1,font=('Arial',15))
        self.btn5.grid(row=2,column=1,padx=2,pady=4)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6 = Button(self.calc_frame,bg="lightgray",text="6",width=10,height=1,font=('Arial',15))
        self.btn6.grid(row=2,column=2,padx=2,pady=4)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsub = Button(self.calc_frame,bg="lightgray",text="-",width=10,height=1,font=('Arial',15))
        self.btnsub.grid(row=2,column=3,padx=2,pady=4)
        self.btnsub.bind("<Button-1>",press_btn)

        self.btn1 = Button(self.calc_frame,bg="lightgray",text="1",width=10,height=1,font=('Arial',15))
        self.btn1.grid(row=3,column=0,padx=2,pady=4)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2 = Button(self.calc_frame,bg="lightgray",text="2",width=10,height=1,font=('Arial',15))
        self.btn2.grid(row=3,column=1,padx=2,pady=4)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3 = Button(self.calc_frame,bg="lightgray",text="3",width=10,height=1,font=('Arial',15))
        self.btn3.grid(row=3,column=2,padx=2,pady=4)
        self.btn3.bind("<Button-1>",press_btn)

        self.btnmul = Button(self.calc_frame,bg="lightgray",text="*",width=10,height=1,font=('Arial',15))
        self.btnmul.grid(row=3,column=3,padx=2,pady=4)
        self.btnmul.bind("<Button-1>",press_btn)

        self.btn0 = Button(self.calc_frame,bg="lightgray",text="0",width=10,height=1,font=('Arial',15))
        self.btn0.grid(row=4,column=0,padx=2,pady=4)
        self.btn0.bind("<Button-1>",press_btn)

        self.btnpoint = Button(self.calc_frame,bg="lightgray",text=".",width=10,height=1,font=('Arial',15))
        self.btnpoint.grid(row=4,column=1,padx=2,pady=4)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btn_clear = Button(self.calc_frame,bg="lightgray",text="=",width=10,height=1,font=('Arial',15))
        self.btn_clear.grid(row=4,column=2,padx=2,pady=4)
        self.btn_clear.bind("<Button-1>",press_btn)

        self.btndiv = Button(self.calc_frame,bg="lightgray",text="/",width=10,height=1,font=('Arial',15))
        self.btndiv.grid(row=4,column=3,padx=2,pady=4)
        self.btndiv.bind("<Button-1>",press_btn)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++

        # ------------------- Bill Frame -----------------
        self.bill_frame = LabelFrame(self.win,text="Bill Area",font=("Arial",18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_frame.place(x=571,y=380,width=550,height=250)

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()


        # ------------------------------------------------

if __name__ == "__main__":
    main()


