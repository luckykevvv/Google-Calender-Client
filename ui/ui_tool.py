from tkinter import *
from tkinter.ttk import *
from typing import Dict
class WinCenter(object):
    """使窗口居中"""
    def __init__(self, window):
        window.withdraw()  # 暂时不显示窗口来移动位置
        window.update_idletasks()  # 刷新GUI，获取窗口参数
        sx = window.winfo_screenwidth()
        sy = window.winfo_screenheight()
        wx = window.winfo_width()
        wy = window.winfo_height()
        px = (sx - wx) // 2
        py = (sy - wy) // 3
        window.geometry(f'{wx}x{wy}+{px}+{py}')
        window.deiconify()  # 使窗口显示
