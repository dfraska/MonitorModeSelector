'''
Created on Dec 30, 2017

@author: Dave
'''
import tkinter as tk
from tkinter import Tk, Button, Toplevel, Frame, messagebox
import screeninfo
import DisplayMode
from DisplayMode import Mode
import keyboard

LeftTV = Mode.External
RightTV = Mode.Internal

class MultimonGui(Toplevel):
    def set_duplicated(self):
        DisplayMode.set_mode(Mode.Duplicate)
        self.exit()
    
    def set_extended(self):
        DisplayMode.set_mode(Mode.Extend)
        self.exit()
    
    def set_left_screen(self):
        DisplayMode.set_mode(LeftTV)
        self.exit()
    
    
    def set_right_screen(self):
        DisplayMode.set_mode(RightTV)
        self.exit()
        
    def cancel(self):
        self.exit()
        
    def exit(self):
        keyboard.unhook_all_hotkeys()
        self.master.destroy()
    
    def _create_widgets(self, curr_mode):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)
                
        frame = Frame(self)
        frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        frame.grid_columnconfigure(0, weight=1, uniform="fred")
        frame.grid_columnconfigure(1, weight=1, uniform="fred")
        frame.grid_rowconfigure(0, weight=1, uniform="wilma")
        frame.grid_rowconfigure(1, weight=1, uniform="wilma")
        
        text = "Extend"
        if curr_mode == Mode.Extend:
            text += " (CURRENT)"
        extend = Button(frame, text=text, command=self.set_extended)
        extend.grid(row=0, column=0, sticky=tk.NSEW)
        
        text = "Duplicate"
        if curr_mode == Mode.Duplicate:
            text += " (CURRENT)"
        duplicate = Button(frame, text=text, command=self.set_duplicated)
        duplicate.grid(row=0, column=1, sticky=tk.NSEW)
        
        text = "Left TV"
        if curr_mode == LeftTV:
            text += " (CURRENT)"
        left_monitor = Button(frame, text=text, command=self.set_left_screen)
        left_monitor.grid(row=1, column=0, sticky=tk.NSEW)
        
        text = "Right TV"
        if curr_mode == RightTV:
            text += " (CURRENT)"
        right_monitor = Button(frame, text=text, command=self.set_right_screen)
        right_monitor.grid(row=1, column=1, sticky=tk.NSEW)
        
        cancel = Button(self, text='Cancel', command=self.cancel)
        cancel.grid(row=1, column=0, sticky=tk.SE)
    
    def on_keyboard(self, key):        
        if key == 'l' or key == 'left':
            self.set_left_screen()
        elif key == 'r' or key == 'right':
            self.set_right_screen()
        elif key == 'e':
            self.set_extended()
        elif key == 'd':
            self.set_duplicated()
        elif key == 'esc':
            self.exit()
            
    def add_hotkey(self, key):
        keyboard.add_hotkey(key, lambda *_: self.on_keyboard(key), suppress=True, trigger_on_release=False)

    def add_hotkeys(self):
        self.add_hotkey('left')
        self.add_hotkey('right')
        self.add_hotkey('l')
        self.add_hotkey('r')
        self.add_hotkey('e')
        self.add_hotkey('d')
        self.add_hotkey('esc')

    def __init__(self, master, monitor):
        super().__init__(master)
        
        # Capture focus so that the program
        # will get the keypresses immediately
        self.focus_set()
        
        self.add_hotkeys()
        
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