'''
@ Project: Notepad Application Copy in wxpython
@ Author: Emmett
@ Date: 14th July
@ Copyright (C) 2020
'''

# Import
import wx 

# Modules
import np_Class
 

# Starting application
if __name__ == '__main__':
    __wx_app = np_Class.wx.App(False)
    __frame = np_Class.Notepad(None)

    __frame.Show()
    __wx_app.MainLoop()