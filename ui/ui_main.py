"""
本代码由[Tkinter布局助手]生成
当前版本:3.4.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
from typing import Dict
import tkinter.messagebox

class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_tabs_lhgthn1i"] = self.__tk_tabs_lhgthn1i(self)
        self.widget_dic["tk_button_lhgy2vm0"] = self.__tk_button_lhgy2vm0(self)

    def __win(self):
        self.title("calender")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)

    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
        
    def __tk_button_lhgy2vm0(self,parent):
        btn = Button(parent, text="log out", takefocus=False,)
        btn.place(x=550, y=0, width=50, height=23)
        return btn

    def __tk_tabs_lhgthn1i(self,parent):
        frame = Notebook(parent)

        self.widget_dic["tk_tabs_lhgthn1i_0"] = self.__tk_frame_lhgthn1i_0(frame)
        frame.add(self.widget_dic["tk_tabs_lhgthn1i_0"], text="event")

        self.widget_dic["tk_tabs_lhgthn1i_1"] = self.__tk_frame_lhgthn1i_1(frame)
        frame.add(self.widget_dic["tk_tabs_lhgthn1i_1"], text="add events")

        self.widget_dic["tk_tabs_lhgthn1i_2"] = self.__tk_frame_lhgthn1i_2(frame)
        frame.add(self.widget_dic["tk_tabs_lhgthn1i_2"], text="delete events")

        self.widget_dic["tk_tabs_lhgthn1i_3"] = self.__tk_frame_lhgthn1i_3(frame)
        frame.add(self.widget_dic["tk_tabs_lhgthn1i_3"], text="offline")

        frame.place(x=0, y=0, width=598, height=503)
        return frame

    def __tk_frame_lhgthn1i_0(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=598, height=503)

        self.widget_dic["tk_table_lhij4qh9"] = self.__tk_table_lhij4qh9(frame)
        self.widget_dic["tk_button_lhzfmuo6"] = self.__tk_button_lhzfmuo6(frame)
        return frame

    def __tk_table_lhij4qh9(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":89,"summary":89,"description":119,"location":89,"start":89,"end":89,"delete ID":29}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=0, y=27, width=597, height=463)
        
        vbar = Scrollbar(parent)
        tk_table.configure(yscrollcommand=vbar.set)
        vbar.config(command=tk_table.yview)
        vbar.place(x=582, y=27, width=15, height=463)
        self.scrollbar_autohide(vbar,tk_table)
        return tk_table

    def __tk_button_lhzfmuo6(self,parent):
        btn = Button(parent, text="refresh", takefocus=False,)
        btn.place(x=0, y=0, width=599, height=27)
        return btn

    def __tk_frame_lhgthn1i_1(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=598, height=503)

        self.widget_dic["tk_button_lhgy4y0v"] = self.__tk_button_lhgy4y0v(frame)
        self.widget_dic["tk_input_lhgy591e"] = self.__tk_input_lhgy591e(frame)
        self.widget_dic["tk_input_lhgy5ab3"] = self.__tk_input_lhgy5ab3(frame)
        self.widget_dic["tk_input_lhgy5c6r"] = self.__tk_input_lhgy5c6r(frame)
        self.widget_dic["tk_input_lhgy5jay"] = self.__tk_input_lhgy5jay(frame)
        self.widget_dic["tk_label_lhgy5o9b"] = self.__tk_label_lhgy5o9b(frame)
        self.widget_dic["tk_label_lhgy5sm6"] = self.__tk_label_lhgy5sm6(frame)
        self.widget_dic["tk_label_lhgy5wc7"] = self.__tk_label_lhgy5wc7(frame)
        self.widget_dic["tk_label_lhgy652w"] = self.__tk_label_lhgy652w(frame)
        self.widget_dic["tk_input_lhgy6si8"] = self.__tk_input_lhgy6si8(frame)
        self.widget_dic["tk_label_lhgy6yd0"] = self.__tk_label_lhgy6yd0(frame)
        return frame

    def __tk_button_lhgy4y0v(self,parent):
        btn = Button(parent, text="add", takefocus=False,)
        btn.place(x=280, y=320, width=50, height=30)
        return btn

    def __tk_input_lhgy591e(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=30, width=150, height=30)
        return ipt

    def __tk_input_lhgy5ab3(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=90, width=150, height=30)
        return ipt

    def __tk_input_lhgy5c6r(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=150, width=150, height=30)
        return ipt

    def __tk_input_lhgy5jay(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=210, width=150, height=30)
        return ipt

    def __tk_label_lhgy5o9b(self,parent):
        label = Label(parent,text="summary",anchor="center", )
        label.place(x=150, y=30, width=57, height=30)
        return label

    def __tk_label_lhgy5sm6(self,parent):
        label = Label(parent,text="description",anchor="center", )
        label.place(x=150, y=90, width=66, height=30)
        return label

    def __tk_label_lhgy5wc7(self,parent):
        label = Label(parent,text="location",anchor="center", )
        label.place(x=150, y=150, width=50, height=30)
        return label

    def __tk_label_lhgy652w(self,parent):
        label = Label(parent,text="start time",anchor="center", )
        label.place(x=150, y=210, width=57, height=30)
        return label

    def __tk_input_lhgy6si8(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=270, width=150, height=30)
        return ipt

    def __tk_label_lhgy6yd0(self,parent):
        label = Label(parent,text="end time",anchor="center", )
        label.place(x=150, y=270, width=54, height=30)
        return label

    def __tk_frame_lhgthn1i_2(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=598, height=503)

        self.widget_dic["tk_input_lhzez65m"] = self.__tk_input_lhzez65m(frame)
        self.widget_dic["tk_label_lhzez9mv"] = self.__tk_label_lhzez9mv(frame)
        self.widget_dic["tk_button_lhzezyzr"] = self.__tk_button_lhzezyzr(frame)
        return frame

    def __tk_input_lhzez65m(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=250, y=120, width=150, height=30)
        return ipt

    def __tk_label_lhzez9mv(self,parent):
        label = Label(parent,text="delete ID",anchor="center", )
        label.place(x=130, y=120, width=66, height=30)
        return label

    def __tk_button_lhzezyzr(self,parent):
        btn = Button(parent, text="delete", takefocus=False,)
        btn.place(x=260, y=250, width=50, height=30)
        return btn

    def __tk_frame_lhgthn1i_3(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=598, height=503)

        self.widget_dic["tk_button_lhzf0v2x"] = self.__tk_button_lhzf0v2x(frame)
        return frame

    def __tk_button_lhzf0v2x(self,parent):
        btn = Button(parent, text="offline mode", takefocus=False,)
        btn.place(x=230, y=170, width=99, height=66)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def copy(self,evt):
        print("<Double-Button-1>事件未处理",evt)
        
    def __event_bind(self):
        self.widget_dic["tk_table_lhij4qh9"].bind('<Double-Button-1>',self.copy)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
