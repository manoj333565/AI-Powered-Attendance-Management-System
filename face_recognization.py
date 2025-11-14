from tkinter import*
from tkinter import ttk
from PIL import Image ,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

# revise this part 

class Face_recognization:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")


        title_lbl = Label(self.root,text="FACE RECOGNIZATION ",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

         # first image 
        img_top = Image.open(r"college_images\face_detector1.JPG")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

          # SECOND image 
        img_bottom = Image.open(r"college_images\facial_recognition_system.JPG")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)


        # button on f_lbl
        b1_1 = Button(f_lbl,text="Face Recognization",command=self.face_recog, cursor="hand2",font=("times new roman",18,"bold"),bg="purple",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)
    
    # ============== Attendance=========================================
    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",") 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and  (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString= now.strftime("%H:%M:%S")
                f.write(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    
    # ==================== Face Recognization ===========================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+x+w])
                confidence=int((100*(1-predict/300))) # confidence = 100-predict by chat gpt 

                #take data from mysql and create database 
                conn = mysql.connector.connect(host="localhost",username="root",password="Manoj@123#",database="face_recognizer")
                my_cursor = conn.cursor()

                #write query - ---- for student name 
                my_cursor.execute("select Name from student where Student_id="+str(id))
                #fetch data from database
                n = my_cursor.fetchone()
                n="+".join(n)

                #write query ---- for roll no
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                #fetch data from database
                r = my_cursor.fetchone()
                r="+".join(r)

                #write query ---- for Department no 
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                #fetch data from database
                d = my_cursor.fetchone()
                d="+".join(d)

                #write query ---- for student ID 
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                #fetch data from database
                i = my_cursor.fetchone()
                i="+".join(i)


                if confidence>77:  # checking how much our data can predict from the sample
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord
        #======================             ==============
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf )
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0) # 0--- for our system camera , for other camera ---- 1


        while True: #
            ret,img = video_cap.read()
            if not ret:
              print("Failed to capture video frame. Check your camera connection.")
              break

            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognization",img)

            # for closing the window
            if cv2.waitKey(1)==13: # press Enter to Exit
                break
        video_cap.release()
        cv2.destroyAllWindows()

        



if __name__ == "__main__":
    root = Tk()
    obj = Face_recognization(root)
    root.mainloop()