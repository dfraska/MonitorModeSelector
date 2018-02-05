'''
Created on Dec 30, 2017

@author: Dave
'''
import tkinter as tk
from tkinter import Tk, Button, Toplevel, Frame
import screeninfo
import DisplayMode
from DisplayMode import Mode

class MultimonGui(Toplevel):
    def duplicate_cmd(self):
        DisplayMode.set_mode(Mode.Duplicate)
        self.master.destroy()
    
    def extend_cmd(self):
        DisplayMode.set_mode(Mode.Extend)
        self.master.destroy()
    
    def internal_screen_cmd(self):
        DisplayMode.set_mode(Mode.Internal)
        self.master.destroy()
    
    def external_screen_cmd(self):
        DisplayMode.set_mode(Mode.External)
        self.master.destroy()

    def cancel(self):
        self.master.destroy()
    
    def _create_widgets(self, curr_mode):
        outer_frame = Frame(self)
        outer_frame.grid_columnconfigure(0, weight=1)
        outer_frame.grid_rowconfigure(0, weight=1)
        outer_frame.grid_rowconfigure(1, weight=0)
        outer_frame.pack(fill=tk.BOTH, expand=True)
        
        frame = Frame(outer_frame)
        frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        
        text = "Extend"
        if curr_mode == Mode.Extend:
            text += " (CURRENT)"
        extend = Button(frame, text=text, command=self.extend_cmd)
        extend.grid(row=0, column=0, sticky=tk.NSEW)
        
        text = "Duplicate"
        if curr_mode == Mode.Duplicate:
            text += " (CURRENT)"
        duplicate = Button(frame, text=text, command=self.duplicate_cmd)
        duplicate.grid(row=0, column=1, sticky=tk.NSEW)
        
        text = "Left TV"
        if curr_mode == Mode.Internal:
            text += " (CURRENT)"
        left_monitor = Button(frame, text=text, command=self.internal_screen_cmd)
        left_monitor.grid(row=1, column=0, sticky=tk.NSEW)
        
        text = "Right TV"
        if curr_mode == Mode.External:
            text += " (CURRENT)"
        right_monitor = Button(frame, text=text, command=self.external_screen_cmd)
        right_monitor.grid(row=1, column=1, sticky=tk.NSEW)
        
        cancel = Button(outer_frame, text='Cancel', command=self.cancel)
        cancel.grid(row=1, column=0, sticky=tk.SE)
    
    def __init__(self, master, monitor):
        super().__init__(master)
        
        self.wm_attributes("-topmost", 1)
        
        curr_mode = DisplayMode.get_mode()
        
        self.overrideredirect(1)
        
        width = int(monitor.width / 2)
        height = int(monitor.height / 2)
        x = int(monitor.x + width / 2)
        y = int(monitor.y + height / 2)
        
        geometry = '{:d}x{:d}+{:d}+{:d}'.format(width, height, x, y)
        self.geometry(geometry)
        
        self._create_widgets(curr_mode)

if __name__ == '__main__':
    root = Tk()
    
    # Hide the root so that only the config windows will open
    root.withdraw()
    
    # Create a gui for each monitor
    for m in screeninfo.get_monitors():
        gui = MultimonGui(root, m)
    
    root.mainloop()