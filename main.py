import tkinter as tk
import tkinter.font as tkFont
from tkinter.constants import *
from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        # setting title
        root.title("R4R")
        # setting window size
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.overrideredirect(True)
        self.welcome_page() 
    # ================================ welcome_page =========================================
    def welcome_page(self):
        for i in root.winfo_children():
            i.destroy()
        self.frame0 = tk.Frame(root, width=width, height=height)
        self.frame0.pack()
        # Create the canvas, size in pixels.
        self.canvas = tk.Canvas(self.frame0, width=width, height=height, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg.pbm')
        self.canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # -------------make buttons-----------------
        # <----EN
        self.en_btn = tk.Button(self.frame0, text="Go to Register", command=self.select_page_En)
        self.en_btn.place(x=80,y=210,width=280,height=270)
        self.en_btn_img = tk.PhotoImage(file='images/btn_en.png')
        self.en_btn["image"] = self.en_btn_img
        self.en_btn["borderwidth"] = "0px"
        # <----SI
        self.si_btn = tk.Button(self.frame0, text="Go to Register", command=self.select_page_En)
        self.si_btn.place(x=380,y=210,width=280,height=270)
        self.si_btn_img = tk.PhotoImage(file='images/btn_si.png')
        self.si_btn["image"] = self.si_btn_img
        self.si_btn["borderwidth"] = "0px"
        # <----TI
        self.ti_btn = tk.Button(self.frame0, text="Go to Register", command=self.select_page_En)
        self.ti_btn.place(x=680,y=210,width=280,height=270)
        self.ti_btn_img = tk.PhotoImage(file='images/btn_ti.png')
        self.ti_btn["image"] = self.ti_btn_img
        self.ti_btn["borderwidth"] = "0px"

    # ============================== select_page ========================================== 
    def select_page_En(self):
        for i in root.winfo_children():
            i.destroy()
        self.frame1 = tk.Frame(root, width=width, height=height)
        self.frame1.pack()
        # Create the canvas, size in pixels.
        self.canvas = tk.Canvas(self.frame1, width=width, height=height, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_1.pbm')
        self.canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # -------------make buttons-----------------
        # <---- sacn
        self.sacn_en_btn = tk.Button(self.frame1, text="Go to Register", command=self.select_page_En)
        self.sacn_en_btn.place(x=80,y=160,width=290,height=335)
        self.en_sacn_en_btn_img = tk.PhotoImage(file='images/btn_sacn_en.png')
        self.sacn_en_btn["image"] = self.en_sacn_en_btn_img
        self.sacn_en_btn["borderwidth"] = "0px"
        # <----newUser
        self.newUser_en_btn = tk.Button(self.frame1, text="Go to Register", command=self.select_page_En)
        self.newUser_en_btn.place(x=390,y=160,width=270,height=335)
        self.newUser_en_btn_img = tk.PhotoImage(file='images/btn_newUse_en.png')
        self.newUser_en_btn["image"] = self.newUser_en_btn_img
        self.newUser_en_btn["borderwidth"] = "0px"
        # <----WithoutID
        self.WithoutID_btn = tk.Button(self.frame1, text="Go to Register", command=self.select_page_En)
        self.WithoutID_btn.place(x=680,y=160,width=270,height=335)
        self.WithoutID_btn_img = tk.PhotoImage(file='images/btn_AccWithOutID_en.png')
        self.WithoutID_btn["image"] = self.WithoutID_btn_img
        self.WithoutID_btn["borderwidth"] = "0px"
        # <----home
        self.home_btn = tk.Button(self.frame1, text="Go to Register", command=self.welcome_page)
        self.home_btn.place(x=890,y=50,width=62,height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        self.home_btn["image"] = self.home_btn_img
        self.home_btn["borderwidth"] = "0px"
        # <----back
        self.back_btn = tk.Button(self.frame1, text="Go to Register", command=self.welcome_page)
        self.back_btn.place(x=725,y=50,width=162,height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        self.back_btn["image"] = self.back_btn_img
        self.back_btn["borderwidth"] = "0px"


    def register(self):
        for i in root.winfo_children():
            i.destroy()
        self.frame2 = tk.Frame(root, width=width, height=height)
        self.frame2.pack()
        self.reg_txt2 = tk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = tk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()



if __name__ == "__main__":
    width = 1024
    height = 600
    root = tk.Tk()
    app = App(root)
    root.mainloop()
