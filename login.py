from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector # for database connect
from main import Face_recognition_system

# for defining same object call for bith login_window and register window
def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"D:\Workspace\Project\LOGIN_FORM\college_images\di.JPG")
        
        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame =Frame(self.root,background="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1 = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\LoginIconAppl.PNG")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimage1=Label(image=self.photoimage1,bg="black",borderwidth=0,)
        lblimage1.place(x=730,y=175,width=100,height=100)

        get_str =Label(frame,text="Get Started",font=("Times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #  Label
        username_lbl = Label(frame,text="Username",font=("Times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.txtuser = ttk.Entry(frame,font=("Times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        
        password_lbl = Label(frame, text="Password", font=("Times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("Times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # =============== Icon image ================

        img2 = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\LoginIconAppl.PNG")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimage2=Label(image=self.photoimage2,bg="black",borderwidth=0,)
        lblimage2.place(x=650,y=323,width=25,height=25)

        img3 = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\lock-512.PNG")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimage3=Label(image=self.photoimage3,bg="black",borderwidth=0,)
        lblimage3.place(x=650,y=395,width=25,height=25)
        
        #loginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("Times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register Button
        loginbtn=Button(frame,text="New User Register",command=self.register_window,font=("Times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=15,y=350,width=160)

        # forget Password button 
        forgetbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("Times new roman", 10, "bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window =Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() =="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            
            messagebox.showinfo("Success","Werlcome to AI BASED ATTENDANCE SYSTEM") 
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Manoj@123#",database="logindata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                 

                                                                                 self.txtuser.get(),
                                                                                 self.txtpass.get()
                                                                                   ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo",'Access only admin')
                if open_main>0:
                    self.root.withdraw() # HIDE login window(do not destroy) # changing
                    self.new_window=Toplevel(self.root) # FIXING done here 
                    self.app= Face_recognition_system(self.new_window)
                    
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    # =================================reset password========================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Select","select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the the answer",parent=self.root2)
        elif self.txt_password.get()=="":
            messagebox.showerror("Error","Please Enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Manoj@123#",database="logindata")
            my_cursor=conn.cursor()
            query =("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter The Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,Please Login new password",parent=self.root2)
                self.root2.destroy()


     # ============================== forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the mail to reset password")
        else:
             conn = mysql.connector.connect(host="localhost",user="root",password="Manoj@123#",database="logindata")
             my_cursor=conn.cursor()
             query =("select * from register where email=%s")
             value=(self.txtuser.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             #print(row)

             if row ==None:
                 messagebox.showerror("Error","Please Enter the Valid user name")
             else:
                 conn.close()
                 self.root2=Toplevel()
                 self.root2.title("Forgot Password")
                 self.root2.geometry("340x450+610+170")

                 l=Label(self.root2,text="Forgot Password",font=("Times new roman", 12, "bold"),fg="red",bg="white")
                 l.place(x=0,y=10,relwidth=1)
                
                 security_Q = Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),background="white",fg="black")
                 security_Q.place(x=50,y=80)
                

                 self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                 self.combo_security_Q["values"]=("Select","Your Birth Place","Favourite Pet Animal","Your School Name","favourite Sports")
                 self.combo_security_Q.place(x=50,y=110,width=250)
                 self.combo_security_Q.current(0)

                 security_A =Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                 security_A.place(x=50,y=150)

                 self.txt_security = ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_security.place(x=50, y=180,width=250)

                 new_password =Label(self.root2,text="New password",font=("times new roman",15,"bold"),bg="white",fg="black")
                 new_password.place(x=50,y=220)

                 self.txt_password = ttk.Entry(self.root2,font=("times new roman",15))
                 self.txt_password.place(x=50, y=250,width=250)

                 btn = Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="white",fg="green")
                 btn.place(x=100,y=290)





           


#====================Register window ======================================================
class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")

          # =============================Variable============================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()



         # ========= Background Images ===========
         # Make the window full screen
        self.root.state('zoomed')  # Works on Windows
        # For Linux/Mac use:
        # self.root.attributes('-fullscreen', True)

        # Get screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Load and resize background image to match screen
        self.original_bg = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\2-AI-invades-automobile-industry-in-2019.JPEG")
        self.bg = ImageTk.PhotoImage(self.original_bg.resize((screen_width, screen_height), Image.LANCZOS))

        # Place background
        self.bg_lbl = Label(self.root, image=self.bg)
        self.bg_lbl.place(x=0, y=0, width=screen_width, height=screen_height)

        # =================Left images ==================
        self.bg1 = ImageTk.PhotoImage(file=r"D:\Workspace\Project\LOGIN_FORM\college_images\Team.JPG") 
        left_lbl = Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550) 

         # ============ main frame ===============

        frame = Frame(self.root,bg = "white")
        frame.place(x=520,y=100,width=800,height=550)
        
        

        Register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="Darkgreen",background="white")
        Register_lbl.place(x=20,y=20)

        #==============Label and entry feild =====================
        # .............row 1 ..................

        fname = Label(frame,text="First Name",font=("times new roman",15,"bold"),background="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # ............ row2..................

        Contact = Label(frame,text="Contact No",font=("times new roman",15,"bold"),background="white",fg="black")
        Contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

      
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # .............row 3 .................

        security = Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),background="white",fg="black")
        security.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Favourite Pet Animal","Your School Name","favourite Sports")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A =Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370, y=270,width=250)    

        # .................row 4
        pswd = Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd = Label(frame,text="Confirm Paswword",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # =========== check button =======================
        self.var_check=IntVar()
        Checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

        #========================= button =========================
        img = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\register-now-button1.JPG")
        img = img.resize((200,55), Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1 = Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1 = Image.open(r"D:\Workspace\Project\LOGIN_FORM\college_images\login.PNG")
        img1 = img1.resize((200,55), Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1 = Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=330,y=420,width=200)

    
    # ========== function Declaration ============================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get() =="select":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.var_pass.get() !=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost",user="root",password="Manoj@123#",database="logindata")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                  self.var_fname.get(),
                                                                                  self.var_lname.get(),
                                                                                  self.var_contact.get(),
                                                                                  self.var_email.get(),
                                                                                  self.var_securityQ.get(),
                                                                                  self.var_SecurityA.get(),
                                                                                  self.var_pass.get(),
                                                                                
                                                                                 ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

            







if __name__ =="__main__":
    main()