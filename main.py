from tkinter import*
from tkinter import ttk
from PIL import Image ,ImageTk
import tkinter
import os
from student import Student            #importing Student.py
from train import Train                # importing train.py class Train
from face_recognization import Face_recognization   # importing face_recognization  from class Face_recognization
from attendance import Attendance # importing attendance from class Atttendance
from developer import Developer
from help import Help
from time import strftime  # import time 
from datetime import datetime # import date 
 
 # face recognition system =====Working 

class Face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

        # First Image
        img = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\BestFacialRecognition.JPG")
        img = img.resize((510, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x = 0,y=0,width=510,height=130)
        
        
        #Second image
        img1 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\facialrecognition.PNG")
        img1 = img1.resize((510, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        
        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x = 510,y=0,width=510,height=130)
        

        #Third Image
        img2 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\images.JPG")
        img2 = img2.resize((510, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        
        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x = 1020,y=0,width=510,height=130)


        # Background Image

        img3 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\bg.JPG")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x = 0,y=130,width=1530,height=710)
        

        title_lbl = Label(bg_img,text="AI-POWERED ATTENDANCE MANAGEMENT SYSTEM SOFTWARE",font=("times new roman",27,"bold"),bg="bisque2",fg="darkviolet")
        title_lbl.place(x=0,y=0,width=1530,height=40)

         #  =================time ==================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text =string)
            lbl.after(1000,time)

        lbl = Label(title_lbl,font=('times new roman',14,'bold'),background='bisque2',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

            

    
         # Student Button
        img4 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\student1.JPEG")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


          # Detect Face Button
        img5 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\face detection.JPEG")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",command=self.face_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        

          # Attendence Face button
        img6 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\attendance_pic.JPEG")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img,image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


         # Help desk
        img7 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\help-desk.JPG")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img,image=self.photoimg7, cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Help Desk", cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Train face button
        img8 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\Train.JPG")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img,image=self.photoimg8, cursor="hand2",command=self.Train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Train Data",command=self.Train_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        # Photo
        img9 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\pic.JPEG")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img,image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos",command=self.open_img, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


         # Developer
        img10 = Image.open(r"D:\Workspace\Project\face_recognitation_system\college_images\developer.JPG")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img,image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        # exit face button 
        img11 = Image.open(r"college_images\exit.JPG") # aise bhi kar skte withoutgiving directory because ye same folder me req.photo hai
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img,image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
    

    def open_img(self):
        os.startfile("Data")

    def iExit(self):
        ans=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if ans:
            # close main window and show login again
            parent_root= self.root.master # Toplevel(self.root) master is the original login tk
            self.root.destroy() # close main(toplevel)
            if parent_root is not None:
                parent_root.deiconify() # show login window again
        else:
            return
        
    # ================function Button==============================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def Train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_recognization(self.new_window) # Face_Recognization is class 

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window) # Attendance is class 

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window) # Developer is class 

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window) # Help is class 







if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_system(root)
    root.mainloop()
        