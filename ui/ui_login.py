import tkinter as tk
from tkinter import ttk
#from . import ui_main
#from . import ui_tool


class Login(tk.Tk):
    def __init__(self):
        super().__init__()  # 有点相当于tk.Tk()
        self.welcome = tk.StringVar()
        self.user = tk.StringVar()
        self.pwd = tk.StringVar()
        self.msg = tk.StringVar()
        self.btn_ok = ttk.Button()
        self.btn_google = ttk.Button()
        self.out = ttk.Button()
        self.v= tk.IntVar()
        self.run()

    def run(self):
        self.title("calender")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        frm = tk.Frame(self)
        frm.pack(padx=40, pady=20)

        self.welcome.set('calender')
        print("23")
        tk.Label(frm, textvariable=self.welcome, font=('', 30)).pack(pady=20)

        user_frm = tk.Frame(frm)
        user_frm.pack(pady=10)
        pwd_frm = tk.Frame(frm)
        pwd_frm.pack(pady=10)
        btn_frm = tk.Frame(frm)
        btn_frm.pack(pady=10)

        #tk.Label(user_frm, text='用户名', width=8, anchor='w').pack(padx=5, side='left')
        #tk.Entry(user_frm, textvariable=self.user).pack(side='left')

        #tk.Label(pwd_frm, text='密码', width=8, anchor='w').pack(padx=5, side='left')
        #tk.Entry(pwd_frm, textvariable=self.pwd, show="*").pack(side='left')

        #self.btn_ok = ttk.Button(btn_frm, text='确定')
        #self.btn_ok.pack(padx=10, side='left')
        self.btn_google = ttk.Button(btn_frm, text='google login')
        self.btn_google.pack(padx=10, side='right')
        #self.btn_out = ttk.Button(btn_frm, text='注册')
        #self.btn_out.pack()
        tk.Checkbutton(frm, text="stay login", variable=self.v).pack()
        #l = tk.Label(frm,textvariable=self.v)#显示下面的0和1
        #l.pack()
        tk.Label(frm, textvariable=self.msg, fg='red').pack(pady=10)
        #ui_tool.WinCenter(self)

if __name__ == '__main__':
    lg = Login()
    lg.title('fusion calender')
    print("22")
    lg.welcome.set('fusion calender')
    lg.mainloop()
