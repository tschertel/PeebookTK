import sys
from os import getenv, path
from tkinter.filedialog import askdirectory

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

sys.path.append("utils")

from utils import configuration


class SettingsWindow(ttk.Toplevel):
    """
    create a settings window
    """

    def __init__(self, parent, func):
        super().__init__(parent)
        self.func = func
        self.title("Peebook Configuration")
        self.geometry("400x300")
        self.resizable(False, False)
        self.config(padx=10, pady=10)
        self.iconphoto(
            False,
            ttk.PhotoImage(file="gui/icons/ebook_32.png"),
            ttk.PhotoImage(file="gui/icons/ebook_64.png"),
        )
        self.transient()
        self.grab_set()
        self.grid()
        # self.position_center()

        # upper Frame
        self.upperFrame = ttk.Frame(self)
        self.upperFrame.pack(side=TOP)

        # Dropbox Label Frame
        self.dropboxGroup = ttk.Labelframe(
            self.upperFrame, text="Dropbox configuration", padding=5
        )
        self.dropboxGroup.grid(row=0, column=0, ipadx=5, ipady=5)

        self.dropboxTokenLabel = ttk.Label(
            self.dropboxGroup, padding=10, text="Dropbox token:"
        )
        self.dropboxTokenLabel.grid(row=0, column=0)

        self.DROPBOXTOKEN = configuration.load_config("Dropbox", "token")
        self.dropboxTokenEntry = ttk.Entry(self.dropboxGroup)
        self.dropboxTokenEntry.insert(0, string=self.DROPBOXTOKEN)
        self.dropboxTokenEntry.grid(row=0, column=1)

        self.moonreaderFolderLabel = ttk.Label(
            self.dropboxGroup, padding=5, text="MoonReader+ folder:"
        )
        self.moonreaderFolderLabel.grid(row=1, column=0)

        self.MOONREADERFOLDER = configuration.load_config("Dropbox", "moonreaderfolder")
        self.moonreaderFolderEntry = ttk.Entry(self.dropboxGroup)
        if not self.MOONREADERFOLDER:
            self.moonreaderFolderEntry.insert(
                0, path.join(getenv("USERPROFILE"), "Dropbox\\Apps\\Books\\.Moon+\\Cache")
            )
            # self.moonreaderFolderEntry.configure(state="readonly")
            self.moonreaderFolderEntry.config(state="disabled")
        else:
            self.moonreaderFolderEntry.insert(0, self.MOONREADERFOLDER)
        self.moonreaderFolderEntry.grid(row=1, column=1)

        moonreaderSearchFolder = ttk.Button(
            self.dropboxGroup, text="...", command=self.onMoonreaderSearchFolder
        )
        moonreaderSearchFolder.grid(row=1, column=2, padx=5)

        # bottom frame
        self.bottomFrame = ttk.Frame(self)
        self.bottomFrame.pack(side=TOP)
        OKButton = ttk.Button(
            self.bottomFrame,
            padding=10,
            text="OK",
            command=self.onOKButton,
        )
        OKButton.grid(row=0, column=1)

        CancelButton = ttk.Button(
            self.bottomFrame,
            padding=10,
            text="CANCEL",
            bootstyle=DANGER,
            command=self.onCancelButton,
        )
        CancelButton.grid(row=0, column=3)

    def onOKButton(self):
        if self.dropboxTokenEntry.get() != self.DROPBOXTOKEN:
            configuration.save_config("Dropbox", "token", self.dropboxTokenEntry.get())
        if self.moonreaderFolderEntry.get() != self.MOONREADERFOLDER:
            configuration.save_config(
                "Dropbox", "moonreaderfolder", self.moonreaderFolderEntry.get()
            )
        self.destroy()

    def onCancelButton(self):
        self.destroy()

    def onMoonreaderSearchFolder(self):
        """Open dialogue to get MoonReader cache directory"""
        d = askdirectory()
        if d:
            self.moonreaderFolderEntry.delete(0, END)
            self.moonreaderFolderEntry.insert(0, d)

    def onChangeCheckButton(self):
        print(f"Valor na janela: {self.themeToggleState}")

    def ParentFunc(self):
        self.func(self.var.get())
