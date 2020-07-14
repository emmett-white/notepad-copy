# Import
import wx
from pathlib import Path
import webbrowser


# Variables
WILDCARD = 'Text Documents (*.txt)|*.txt|Python Documents (*.py)|*.py'
UNTITLED = 'Untitled'
HELP_URL = '...'


# Class
class Notepad(wx.Frame):
    # Functions
    def __init__(self, *args, **kwargs):
        super(Notepad, self).__init__(*args, **kwargs)

        self.path = None

        self.frame_settings()
        self.create_menus()
        self.create_gui_items()
        self.create_sizers()
        self.add_binds()
 

    def frame_settings(self):
        self.update_title()
        self.CreateStatusBar()
        self.SetMinSize((600, 400))
        self.CentreOnScreen()
 
 
    def create_menus(self):
        self.menubar = wx.MenuBar()

        self.SetMenuBar(self.menubar)
        self.create_file_menu()
        self.create_edit_menu()
        self.create_help_menu()
 
 
    def create_file_menu(self):
        file_menu = wx.Menu()

        self.menu_new = file_menu.Append(wx.ID_NEW, '&New', 'Creates a new document')
        self.menu_open = file_menu.Append(wx.ID_OPEN, '&Open', 'Open an existing file')
        self.menu_save = file_menu.Append(wx.ID_SAVE, '&Save', 'Saves the active document')
        self.menu_saveas = file_menu.Append(wx.ID_SAVEAS, 'Save &As', 'Saves the active document with a new name')

        file_menu.AppendSeparator()

        self.menu_exit = file_menu.Append(-1, 'E&xit', 'Exit the Application')

        self.menubar.Append(file_menu, '&File')
 
 
    def create_edit_menu(self):
        edit_menu = wx.Menu()
        self.menu_undo = edit_menu.Append(wx.ID_UNDO, '&Undo', 'Undo change')

        edit_menu.AppendSeparator()

        self.menu_cut = edit_menu.Append(wx.ID_CUT, 'Cu&t', 'Cut the selected text')
        self.menu_copy = edit_menu.Append(wx.ID_COPY, '&Copy', 'Copy the selected text')
        self.menu_paste = edit_menu.Append(wx.ID_PASTE, '&Paste', 'Paste from the clipboard')
        self.menu_delete = edit_menu.Append(wx.ID_DELETE, 'De&lete', 'Delete selected text')

        self.menubar.Append(edit_menu, '&Edit')
 
 
    def create_help_menu(self):
        help_menu = wx.Menu()

        self.menu_help = help_menu.Append(wx.ID_HELP, '&Help', 'Get Help from python-forum.io')

        self.menubar.Append(help_menu, '&Help')
 
 
    def create_gui_items(self):
        self.frame_panel = wx.Panel(self)
        self.txt_ctrl = wx.TextCtrl(self.frame_panel, style=wx.TE_MULTILINE | wx.BORDER_NONE)
 
 
    def create_sizers(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.frame_panel, 1, wx.EXPAND)

        p_sizer = wx.BoxSizer(wx.VERTICAL)
        p_sizer.Add(self.txt_ctrl, 1, wx.EXPAND)

        self.frame_panel.SetSizer(p_sizer)
        self.SetSizer(sizer)
        self.Layout()
 

    def add_binds(self):
        self.add_frame_binds()
        self.add_fle_menu_binds()
        self.add_edit_menu_binds()
        self.add_help_menu_binds()
 
 
    def add_frame_binds(self):
        self.Bind(wx.EVT_CLOSE, self.on_close_evt)
 
 
    def add_fle_menu_binds(self):
        self.Bind(wx.EVT_MENU, self.on_menu_new, self.menu_new)
        self.Bind(wx.EVT_MENU, self.on_menu_open, self.menu_open)
        self.Bind(wx.EVT_MENU, self.on_menu_save, self.menu_save)
        self.Bind(wx.EVT_MENU, self.on_menu_saveas, self.menu_saveas)
        self.Bind(wx.EVT_MENU, self.on_menu_exit, self.menu_exit)
 
 
    def add_edit_menu_binds(self):
        self.Bind(wx.EVT_MENU, self.on_menu_undo, self.menu_undo)
        self.Bind(wx.EVT_UPDATE_UI, self.on_menu_undo_update, self.menu_undo)
        self.Bind(wx.EVT_MENU, self.on_menu_cut, self.menu_cut)
        self.Bind(wx.EVT_UPDATE_UI, self.on_menu_cut_update, self.menu_cut)
        self.Bind(wx.EVT_MENU, self.on_menu_copy, self.menu_copy)
        self.Bind(wx.EVT_UPDATE_UI, self.on_menu_copy_update, self.menu_copy)
        self.Bind(wx.EVT_MENU, self.on_menu_paste, self.menu_paste)
        self.Bind(wx.EVT_UPDATE_UI, self.on_menu_paste_update, self.menu_paste)
        self.Bind(wx.EVT_MENU, self.on_menu_delete, self.menu_delete)
        self.Bind(wx.EVT_UPDATE_UI, self.on_menu_delete_update, self.menu_delete)
 
 
    def add_help_menu_binds(self):
        self.Bind(wx.EVT_MENU, self.on_menu_help, self.menu_help)
 
 
    def on_menu_exit(self, event):
        self.Close()
 
 
    def on_menu_new(self, event):
        if self.save_if_modified():
            self.new()
 
 
    def on_menu_open(self, event):
        if self.save_if_modified():
            self.open()
 
 
    def on_menu_save(self, event):
        self.save()
 
 
    def on_menu_saveas(self, event):
        self.save_as()
 
 
    def on_menu_undo(self, event):
        self.txt_ctrl.Undo()
 
 
    def on_menu_undo_update(self, event):
        event.Enable(self.txt_ctrl.CanUndo())
 
 
    def on_menu_cut(self, event):
        self.txt_ctrl.Cut()
 
 
    def on_menu_cut_update(self, event):
        event.Enable(self.txt_ctrl.CanCut())
 
 
    def on_menu_copy(self, event):
        self.txt_ctrl.Copy()
 
 
    def on_menu_copy_update(self, event):
        event.Enable(self.txt_ctrl.CanCopy())
 
 
    def on_menu_paste(self, event):
        self.txt_ctrl.Paste()
 
 
    def on_menu_paste_update(self, event):
        event.Enable(self.txt_ctrl.CanPaste())
 
 
    def on_menu_delete(self, event):
        self.txt_ctrl.Remove(*self.txt_ctrl.GetSelection())
 
 
    def on_menu_delete_update(self, event):
        event.Enable(bool(self.txt_ctrl.GetStringSelection()))
 
 
    def on_menu_help(self, event):
        self.open_forum_page()
 
 
    def on_close_evt(self, event):
        if event.CanVeto():
            if not self.save_if_modified():
                event.Veto()
                return
 

        self.Destroy()
 
 
    def update_title(self):
        name = UNTITLED

        if self.path:
            name = self.path.name


        self.SetTitle(f'{name} - Notepad')
 
 
    def save_changes_msg_dialog(self):
        path = self.path or UNTITLED

        dlg = wx.MessageDialog(self, (f'Do you want to save changes to {path}?'), 'Notepad', wx.YES_NO | wx.CANCEL | wx.CENTER)
        dlg.SetYesNoLabels('Save', 'Don\'t Save')

        return dlg.ShowModal()
 
 
    def save_if_modified(self):
        saved_or_dont_save = True

        if self.txt_ctrl.IsModified():
            dlg_result = self.save_changes_msg_dialog()

            if dlg_result == wx.ID_CANCEL:
                saved_or_dont_save = False

            elif dlg_result == wx.ID_YES:
                self.save()

                if not self.path:
                    saved_or_dont_save = False
 

        return saved_or_dont_save
 
    def new(self):
        self.txt_ctrl.Clear()

        self.path = None

        self.update_title()
 
 
    def open(self):
        with wx.FileDialog(self, message = 'Open', wildcard = WILDCARD, style = wx.FD_OPEN) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                directory, filename = dlg.GetDirectory(), dlg.GetFilename()

                self.path = Path(directory).joinpath(filename)

                self.txt_ctrl.LoadFile(str(self.path))
                self.update_title()
 
 
    def save(self):
        if not self.path:
            self.save_as()
        else:
            self.txt_ctrl.SaveFile(str(self.path))
            self.update_title()
 
 
    def save_as(self):
        with wx.FileDialog(self, message = 'Save as', wildcard = WILDCARD, style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                directory, filename = dlg.GetDirectory(), dlg.GetFilename()

                self.path = Path(directory).joinpath(filename)
                self.save()
 
 
    def open_forum_page(self):
        webbrowser.open(HELP_URL, 2)