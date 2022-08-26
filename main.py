import tkinter as tk
import tkinter.font as tkFont
from tkinter.constants import *
import sys 
# from typing_extensions import Self
from PIL import ImageTk, Image
import requests
from requests.structures import CaseInsensitiveDict
import RPi.GPIO as GPIO

Switch_input = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(Switch_input, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

charkeys_steel = [
    ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'),
    ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'),
    (' ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<')
]

Intkeys_steel = [
    ('1', '2', '3'),
    ('4', '5', '6'),
    ('7', '8', '9'),
    ('0', '<')
]

BinID = 'FOT001'

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1c2VyIiwiYXV0aCI6IlJPTEVfVVNFUiIsImV4cCI6Mjc1ODEyNzQwMzl9.P7wkR88Uon0qxqcBzSOApY7PTP3I6yY8dxlUTnDRqJw2DndTfiC7zEMpHoOG2S-egnxz5gV5uPmu7cbSxHpaUA"

bottleReadMode = False
bottleCount = 0


def countB(channel):
    if GPIO.input(Switch_input):
        global bottleCount
        if bottleReadMode:  
            bottleCount += 1   
            print ("Bottle Adding!")
        else:
            print("mot time to insert bottle!")  
   
GPIO.add_event_detect(Switch_input, GPIO.RISING, callback=countB, bouncetime=300)

class App:
    def __init__(self, root):
        # setting title
        root.title("R4R")
        # setting window size
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,0, -30)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        #root.overrideredirect(True)
        self.welcome_page()

        # ------- read barcode values -----------
        root.bind('<KeyPress>', self.onKeyPress)
        root.bind('<Return>', self.EnterPress)

        # -------database variable ---------
        self.ID_num = ''
        self.U_Name = ''
        self.Tel_num = ''
        self.TypeRecord = ''
        self.scanMode = False
        self.wihoutID_Mode = False
        self.SendData = {'donatorId': '', 'userName': '', 'email': '', 'phoneNumber': ''}
        self.bottleData = {"phoneNumber": "", "binId": "", "bottleCount": 0}

    # ================================ welcome_page =========================================
    def welcome_page(self):
        global bottleReadMode
        bottleReadMode =False
        self.SendData = {'donatorId': '', 'userName': '','email': '', 'phoneNumber': ''}
        self.bottleData = {"phoneNumber": "", "binId": "", "bottleCount": 0}
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # -------------make buttons-----------------
        # <----EN
        en_btn = tk.Button(
            frame, text="Go to Register", command=self.select_page_En)
        en_btn.place(x=80, y=210, width=280, height=270)
        self.en_btn_img = tk.PhotoImage(file='images/btn_en.png')
        en_btn["image"] = self.en_btn_img
        en_btn["borderwidth"] = "0px"
        # <----SI
        si_btn = tk.Button(
            frame, text="Go to Register", command=self.select_page_En)
        si_btn.place(x=380, y=210, width=280, height=270)
        self.si_btn_img = tk.PhotoImage(file='images/btn_si.png')
        si_btn["image"] = self.si_btn_img
        si_btn["borderwidth"] = "0px"
        # <----TI
        ti_btn = tk.Button(
            frame, text="Go to Register", command=self.select_page_En)
        ti_btn.place(x=680, y=210, width=280, height=270)
        self.ti_btn_img = tk.PhotoImage(file='images/btn_ti.png')
        ti_btn["image"] = self.ti_btn_img
        ti_btn["borderwidth"] = "0px"
    
    def sysout(self):
        sys.exit()

    def Thanku_page_En(self):
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_6.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        
        # -------------make buttons-----------------
        # <---- home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <---- name label
        ft = tkFont.Font(family='Arial', size=24)
        txt_label = tk.Label(root, anchor=NW)
        txt_label["bg"] = "#ffffff"
        txt_label["font"] = ft
        txt_label["fg"] = "#423f49"
        txt_label["justify"] = "center"
        txt_label.place(x=80, y=460, width=360, height=60)
        txt_label["text"] = self.data['userName']
        # <---- num label
        ft = tkFont.Font(family='Arial', size=72, weight=tkFont.BOLD)
        num_label = tk.Label(root)
        num_label["bg"] = "#ffffff"
        num_label["font"] = ft
        num_label["fg"] = "#6c6c6c"
        num_label["justify"] = "center"
        num_label.place(x=825, y=408, width=110, height=115)
        num_label["text"] = str(self.bottleData["bottleCount"])

    # ================================ select_page ==========================================
    def select_page_En(self):
        self.wihoutID_Mode = False
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_1.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # -------------make buttons-----------------
        # <---- sacn
        sacn_en_btn = tk.Button(
            frame, text="Go to Register", command=self.scan_withID_En)
        sacn_en_btn.place(x=80, y=160, width=290, height=335)
        self.en_sacn_en_btn_img = tk.PhotoImage(file='images/btn_sacn_en.png')
        sacn_en_btn["image"] = self.en_sacn_en_btn_img
        sacn_en_btn["borderwidth"] = "0px"
        # <----newUser
        newUser_en_btn = tk.Button(
            frame, text="Go to Register", command=self.scan_withOutID_En)
        newUser_en_btn.place(x=390, y=160, width=270, height=335)
        self.newUser_en_btn_img = tk.PhotoImage(
            file='images/btn_newUse_en.png')
        newUser_en_btn["image"] = self.newUser_en_btn_img
        newUser_en_btn["borderwidth"] = "0px"
        # <----WithoutID
        WithoutID_btn = tk.Button(
            frame, text="Go to Register", command=self.wihoutID)
        WithoutID_btn.place(x=680, y=160, width=270, height=335)
        self.WithoutID_btn_img = tk.PhotoImage(
            file='images/btn_AccWithOutID_en.png')
        WithoutID_btn["image"] = self.WithoutID_btn_img
        WithoutID_btn["borderwidth"] = "0px"
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.sysout)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"

    # ++++++++++++++++++++++++++++++++++ sacn ID ++++++++++++++++++++++++++++++++++++++++++++
    def scan_withID_En(self):
        self.ID_num = ''
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        self.scanMode = True
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_2.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.select_page_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"

    def onKeyPress(self, event):
        if self.scanMode:
            self.ID_num += event.char

    def EnterPress(self, event):
        if self.scanMode:
            print(self.ID_num)
            # <---- get respons
            url = "http://3.131.152.241:8080/api/donators/by-index/" + self.ID_num
            resp = requests.get(url, headers=headers)
            self.data = resp.json()
            if resp.status_code == 200:
                print("get respon ok!")
                self.ins_bottels()
            elif resp.status_code == 404:
                print("invaled data move to new user")
                self.newUser_Name_En()
            else:
                print(resp.status_code)
            self.scanMode = False

    def ins_bottels(self):
        global bottleReadMode
        bottleReadMode =True
        if self.wihoutID_Mode:
            self.data['userName'] = "UNKNOWN"
            self.bottleData["phoneNumber"] = self.TypeRecord

        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_4.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        if self.wihoutID_Mode:
            back_btn = tk.Button(frame, text="Go to Register", command=self.newUser_Num_En)
        else:
            back_btn = tk.Button(frame, text="Go to Register", command=self.scan_withID_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"
        # <---- label
        ft = tkFont.Font(family='Arial', size=42)
        txt_label = tk.Label(root, anchor=NW)
        txt_label["bg"] = "#ffffff"
        txt_label["font"] = ft
        txt_label["fg"] = "#423f49"
        txt_label["justify"] = "center"
        txt_label.place(x=100, y=440, width=600, height=90)
        txt_label["text"] = self.data['userName']
        # <--- 0k button
        ok_btn = tk.Button(
            frame, text="Go to Register", command=self.num_bottels)
        ok_btn.place(x=770, y=250, width=135, height=250)
        self.ok_btn_img = tk.PhotoImage(file='images/btn_ok.png')
        ok_btn["image"] = self.ok_btn_img
        ok_btn["borderwidth"] = "0px"
        ok_btn["bg"] = "#ffffff"

    def num_bottels(self):
        global bottleReadMode
        bottleReadMode =False
        self.bottleData["bottleCount"] = bottleCount
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_5.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # ---- copy data to send json
        if not self.wihoutID_Mode:
            self.bottleData["phoneNumber"] = self.data["phoneNumber"]
        self.bottleData["binId"] = BinID

        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.ins_bottels)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"
        # <---- name label
        ft = tkFont.Font(family='Arial', size=42)
        txt_label = tk.Label(root, anchor=NW)
        txt_label["bg"] = "#ffffff"
        txt_label["font"] = ft
        txt_label["fg"] = "#423f49"
        txt_label["justify"] = "center"
        txt_label.place(x=100, y=195, width=800, height=65)
        txt_label["text"] = self.data['userName']
        # <---- num label
        ft = tkFont.Font(family='Arial', size=84, weight=tkFont.BOLD)
        num_label = tk.Label(root)
        num_label["bg"] = "#ffffff"
        num_label["font"] = ft
        num_label["fg"] = "#6c6c6c"
        num_label["justify"] = "center"
        num_label.place(x=450, y=330, width=150, height=115)
        num_label["text"] = str(self.bottleData["bottleCount"])
        # <--- ok button
        ok_btn = tk.Button(
            frame, text="Go to Register", command=self.bottleDataSend)
        ok_btn.place(x=623, y=286, width=318, height=212)
        self.ok_btn_img = tk.PhotoImage(file='images/btn_ok1.png')
        ok_btn["image"] = self.ok_btn_img
        ok_btn["borderwidth"] = "0px"
        ok_btn["bg"] = "#ffffff"

    def bottleDataSend(self):
        # <---- send json 
        print(self.bottleData)
        url = "http://3.131.152.241:8080/api/bin-histories/add/" 
        resp = requests.post(url, headers=headers, json=self.bottleData)
        if resp.status_code == 201:
            bottleCount = 0
            print("data sending ok!")
            self.Thanku_page_En()
        elif resp.status_code == 404:
            print("Error - data can't be send")
        else:
            print(resp.status_code)

    # +++++++++++++++++++++++++++++++++++ New User +++++++++++++++++++++++++++++++++++++++++++
    def scan_withOutID_En(self):
        self.ID_num = ''
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        self.scanMode = True
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_2.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.select_page_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"

    def newUser_Name_En(self):
        self.SendData['donatorId'] = self.ID_num
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_3.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.scan_withOutID_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"
        # <---- label
        ft = tkFont.Font(family='Arial', size=48)
        txt_label = tk.Label(root)
        txt_label["bg"] = "#f5f7fb"
        txt_label["font"] = ft
        txt_label["fg"] = "#423f49"
        txt_label["justify"] = "center"
        txt_label.place(x=80, y=160, width=875, height=90)
        # <---- keypad
        self.create_char_keypad(frame, txt_label)
        # <--- 0k button
        ok_btn = tk.Button(
            frame, text="Go to Register", command=self.newUser_Num_En)
        ok_btn.place(x=820, y=300, width=135, height=250)
        self.ok_btn_img = tk.PhotoImage(file='images/btn_ok.png')
        ok_btn["image"] = self.ok_btn_img
        ok_btn["borderwidth"] = "0px"
        ok_btn["bg"] = "#ffffff"

    def create_char_keypad(self, store_section, txt_label):
        # take section one by one
        xx = 80
        yy = 300
        colCount = 0
        ft = tkFont.Font(family='Arial', size=24)
        for key_section in charkeys_steel:
            for colom_keys in key_section:
                for k in colom_keys:
                    key_btn = tk.Button(store_section, text=k)
                    key_btn['command'] = lambda q=k: self.txt_button_command(
                        q, txt_label)
                    key_btn["borderwidth"] = "0px"
                    key_btn["font"] = ft
                    key_btn["fg"] = "#1cb60e"
                    if k == ' ':
                        self.key_img1 = tk.PhotoImage(
                            file='images/btn_space.png')
                        key_btn["image"] = self.key_img1
                        key_btn.place(x=xx, y=yy, width=85, height=70)
                        xx += 112
                    elif k == '<':
                        self.key_img2 = tk.PhotoImage(
                            file='images/btn_backspace.png')
                        key_btn["image"] = self.key_img2
                        xx += 12
                        key_btn.place(x=xx, y=yy, width=85, height=70)
                    else:
                        key_btn.place(x=xx, y=yy, width=65, height=70)
                        xx += 73
            colCount += 1
            if colCount == 1:
                xx = 120
            else:
                xx = 80
            yy += 87

    def txt_button_command(self, event, txt_label):
        txt = txt_label.cget("text")
        if event == '<':
            if len(txt) == 0:
                txt_label["text"] = txt
            else:
                txt_label["text"] = txt.rstrip(txt[-1])
        else:
            txt_label["text"] = txt + event
        self.TypeRecord = txt_label["text"]
        return

    def newUser_Num_En(self):
        global bottleReadMode
        bottleReadMode =False
        if self.wihoutID_Mode:
            self.data = {'donatorId': '', 'userName': '', 'email': '', 'phoneNumber': ''}
        else:
            self.SendData['userName'] = self.TypeRecord
        self.TypeRecord = ''
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_7.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)
        # <----home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        if self.wihoutID_Mode:
            back_btn = tk.Button(frame, text="Go to Register", command=self.select_page_En)
        else:
            back_btn = tk.Button(frame, text="Go to Register", command=self.newUser_Name_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"
        # <---- label
        ft = tkFont.Font(family='Arial', size=48)
        num_label = tk.Label(root)
        num_label["bg"] = "#f5f7fb"
        num_label["font"] = ft
        num_label["fg"] = "#423f49"
        num_label["justify"] = "center"
        num_label.place(x=80, y=148, width=870, height=85)
        # <---- keypad
        self.create_Num_keypad(frame, num_label)
        # <--- ok button
        if self.wihoutID_Mode:
            ok_btn = tk.Button(frame, text="Go to Register", command=self.ins_bottels)
        else:
            ok_btn = tk.Button(frame, text="Go to Register", command=self.confirm_page_En)

        ok_btn.place(x=660, y=276, width=135, height=272)
        self.ok_btn_img = tk.PhotoImage(file='images/btn_ok2.png')
        ok_btn["image"] = self.ok_btn_img
        ok_btn["borderwidth"] = "0px"
        ok_btn["bg"] = "#ffffff"

    def create_Num_keypad(self, store_section, num_label):
        # take section one by one
        xx = 230
        yy = 276
        ft = tkFont.Font(family='Arial', size=24)
        for key_section in Intkeys_steel:
            for colom_keys in key_section:
                for k in colom_keys:
                    key_btn = tk.Button(store_section, text=k)
                    key_btn['command'] = lambda q=k: self.num_button_command(
                        q, num_label)
                    key_btn["borderwidth"] = "0px"
                    key_btn["font"] = ft
                    key_btn["fg"] = "#1cb60e"
                    if k == '0':
                        key_btn.place(x=546, y=276, width=87, height=175)
                    elif k == '<':
                        self.key_img2 = tk.PhotoImage(
                            file='images/btn_backspace.png')
                        key_btn["image"] = self.key_img2
                        key_btn.place(x=546, y=465, width=87, height=82)
                    else:
                        key_btn.place(x=xx, y=yy, width=87, height=82)
                        xx += 105
            xx = 230
            yy += 94

    def num_button_command(self, event, txt_label):
        txt = txt_label.cget("text")
        if event == '<':
            if len(txt) == 0:
                txt_label["text"] = txt
            else:
                txt_label["text"] = txt.rstrip(txt[-1])
        else:
            txt_label["text"] = txt + event
        self.TypeRecord = txt_label["text"]
        return

    def confirm_page_En(self):
        self.SendData['phoneNumber'] = self.TypeRecord
        self.TypeRecord = ''
        for i in root.winfo_children():
            i.destroy()
        frame = tk.Frame(root, width=width, height=height)
        frame.pack()
        # Create the canvas, size in pixels.
        canvas = tk.Canvas(frame, width=width,
                           height=height, bg='white')
        canvas.pack(expand=YES, fill=BOTH)
        # Load the .png image file.
        self.img_bg = tk.PhotoImage(file='images/bg_8.pbm')
        canvas.create_image(0, 0, image=self.img_bg, anchor=NW)

        # -------------make buttons-----------------
        # <---- home
        home_btn = tk.Button(
            frame, text="Go to Register", command=self.welcome_page)
        home_btn.place(x=890, y=50, width=62, height=62)
        self.home_btn_img = tk.PhotoImage(file='images/btn_home.png')
        home_btn["image"] = self.home_btn_img
        home_btn["borderwidth"] = "0px"
        home_btn["bg"] = "#ffffff"
        # <----back
        back_btn = tk.Button(
            frame, text="Go to Register", command=self.newUser_Num_En)
        back_btn.place(x=725, y=50, width=162, height=62)
        self.back_btn_img = tk.PhotoImage(file='images/btn_back_en.png')
        back_btn["image"] = self.back_btn_img
        back_btn["borderwidth"] = "0px"
        back_btn["bg"] = "#ffffff"
        # <--- 0k button
        ok_btn = tk.Button(
            frame, text="Go to Register", command=self.finalConfirm_En)
        ok_btn.place(x=667, y=222, width=288, height=256)
        self.ok_btn_img = tk.PhotoImage(file='images/btn_confirm.png')
        ok_btn["image"] = self.ok_btn_img
        ok_btn["borderwidth"] = "0px"
        ok_btn["bg"] = "#ffffff"
        # <---- name label
        ft = tkFont.Font(family='Arial', size=36)
        name_label = tk.Label(root)
        name_label["bg"] = "#f5f7fb"
        name_label["font"] = ft
        name_label["fg"] = "#423f49"
        name_label["justify"] = "center"
        name_label["text"] = self.SendData['userName']
        name_label.place(x=83, y=250, width=553, height=92)
        # <----num label
        ft = tkFont.Font(family='Arial', size=36)
        num_label = tk.Label(root)
        num_label["bg"] = "#f5f7fb"
        num_label["font"] = ft
        num_label["fg"] = "#423f49"
        num_label["justify"] = "center"
        num_label["text"] = self.SendData['phoneNumber']
        num_label.place(x=83, y=388, width=553, height=92)

    def finalConfirm_En(self):
        print(self.SendData)
        self.data = self.SendData
        url = "http://3.131.152.241:8080/api/donators"
        resp = requests.post(url, headers=headers, json=self.SendData)
        if resp.status_code == 201:
            print("data sending ok!")
            self.ins_bottels()
        elif resp.status_code == 404:
            print("Error - data can't be send")
        else:
            print(resp.status_code)

    def wihoutID(self):
        self.wihoutID_Mode = True
        self.newUser_Num_En()


if __name__ == "__main__":
    width = 1024
    height = 600
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
