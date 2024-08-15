import os

# from pathlib import Path
from tkinter import Label, Listbox, Menu, StringVar
from tkinter.filedialog import askopenfilename

import pymupdf
import ttkbootstrap as ttk
from tkinterweb import HtmlFrame
from ttkbootstrap.constants import *

# from gui import icons
from gui.aboutWindow import AboutWindow
from gui.settingsWindow import SettingsWindow
from utils import configuration


class Peebook(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.version = "0.8"

        self.pack(fill=BOTH, expand=YES)
        master.iconphoto(
            False,
            ttk.PhotoImage(file="gui/icons/ebook_32.png"),
            ttk.PhotoImage(file="gui/icons/ebook_64.png"),
        )

        # Creates menubar
        self.menubarMenu = Menu(self, tearoff=False)
        self.master.config(menu=self.menubarMenu)

        # Creates File menu
        self.fileMenu = Menu(self.menubarMenu)
        self.menubarMenu.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Open...", command=self.openFile)
        self.fileMenu.add_command(label="Configure", command=self.openSettingsWindow)

        # Creates last opened files
        self.historyMenu = Menu(self.fileMenu)
        for file in self.getFileHistory():
            self.historyMenu.add_command(label=file)
        self.fileMenu.add_cascade(label="Open recent", menu=self.historyMenu)
        self.historyMenu.add_separator()
        self.historyMenu.add_command(label="Clear history...")

        # Quits app
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=master.quit)

        # Creates Help menu
        self.helpMenu = Menu(self.menubarMenu)
        self.menubarMenu.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="About", command=self.openAboutWindow)

        # Creates Status bar
        self.statusbarMessage = StringVar()
        self.statusBar = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.statusBar["textvariable"] = self.statusbarMessage
        self.statusBar.pack(side=BOTTOM, fill=X)

        # Create left PanedWindow for handle ListBox and ScrollBar
        self.mainPanedWindowWidget = ttk.PanedWindow(self, orient=HORIZONTAL)
        self.mainPanedWindowWidget.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a Frame to handle mainPanedWindowWidget
        self.chaptersFrame = ttk.Frame(self.mainPanedWindowWidget)
        self.chaptersFrame.pack(side=LEFT, fill=BOTH, expand=True)

        # Creates chapter list
        self.chaptersListBox = Listbox(
            self.chaptersFrame, width=40, selectmode=ttk.SINGLE
        )
        self.chaptersListBox.pack(side=LEFT, fill=BOTH, expand=True)
        self.chaptersListBox.select_set(0)
        # self.chaptersListBox.config(state=DISABLED)
        self.chaptersListBox.bind("<<ListboxSelect>>", self.show_chapter)

        # Creates scrollbar
        self.chaptersScrollbar = ttk.Scrollbar(self.chaptersFrame)
        self.chaptersScrollbar.pack(side=LEFT, fill=BOTH)

        self.chaptersListBox.config(yscrollcommand=self.chaptersScrollbar.set)
        self.chaptersScrollbar.config(command=self.chaptersListBox.yview)

        self.mainPanedWindowWidget.add(self.chaptersFrame)

        # Creates HTML frame to show ebook content
        self.ebookView = HtmlFrame(self, messages_enabled=False)
        self.ebookView.ignore_invalid_images(False)
        self.ebookView.load_html(
            "<html><body><h1>Welcome to Peebook!</h1></body></html>"
        )
        self.ebookView.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        # Right click menu
        self.menuPopup = Menu(self.ebookView, tearoff=0)
        self.menuPopup.add_command(
            label="Traduzir com Deepl", command=self.translateWithDeepl
        )
        self.menuPopup.add_command(
            label="Traduzir com Leo", command=self.translateWithLeo
        )
        self.menuPopup.add_command(
            label="Traduzir com Libre", command=self.translateWithLibre
        )

        # Attach right click to function
        self.ebookView.bind("<Button-3>", self.showPopupMenu)

    def openFile(self):
        """Open dialogue to get directory and update variable"""
        file_path = askopenfilename(
            initialdir=configuration.load_config("Lastdir", "path"),
            filetypes=[
                ("EPUB files", "*.epub"),
                ("PDF files", "*.pdf"),
                ("MOBI files", "*.mobi"),
            ],
        )
        if not file_path:
            return
        else:
            with open(file_path, "r") as f:
                self.book = pymupdf.open(f.name)
            self.statusbarMessage.set(f.name)

            page = self.book.load_page(0)
            self.ebookView.load_html(
                page.get_text("html")
            )
            
            configuration.save_config("Lastdir", "path", os.path.split(f.name)[0])
            configuration.save_config("History", "lastfile1", (f.name))
            
            self.chaptersListBox.delete(0, END)
            
            toc = self.book.get_toc()
            if len(toc) == 0:
                for item in range(len(self.book)):
                    self.chaptersListBox.insert(END, item)
            else:
                for item in toc:
                    self.chaptersListBox.insert(END, item[1])

    def show_chapter(self, event):
        """Show chapter content inside HTMLFrame"""
        chapterIndex = self.chaptersListBox.get(self.chaptersListBox.curselection())
        page = self.book.load_page(chapterIndex)
        self.ebookView.load_html(
            page.get_text("html")
        )
        print(f"Item selecionado: {chapterIndex}")
        #print(page.get_text("html"))

    def openSettingsWindow(self):
        self.settings = SettingsWindow(self, self.updateSettings)

    def updateSettings(self):
        raise NotImplementedError("Still to be implemented!")

    def openAboutWindow(self):
        AboutWindow(self)

    def showPopupMenu(self, event):
        if self.ebookView.get_currently_selected_text():
            self.menuPopup.post(event.x_root, event.y_root)
        else:
            return

    def translateWithDeepl(self):
        print(
            f'Traduzindo "{self.ebookView.get_currently_selected_text().strip()}" com o Deepl...'
        )

    def translateWithLibre(self):
        print(
            f'Traduzindo "{self.ebookView.get_currently_selected_text().strip()}" com o Libre...'
        )

    def translateWithLeo(self):
        print(
            f'Traduzindo "{self.ebookView.get_currently_selected_text().strip()}" com o Leo...'
        )

    def getFileHistory(self):
        lastOpenedFiles = configuration.load_config("History", None)
        lastFilesTuple = []
        for item in lastOpenedFiles:
            if all(item):
                lastFilesTuple.append(item[1])
        return lastFilesTuple

    def saveFileHistory(self):
        raise NotImplemented("Still to be implemented!")
        # bool([item for item in lastOpenedFiles if item[1] == 'C:/Users/t.schertel/Dropbox/Alemão/Bücher/Agatha Christie/Und dann gabs keines mehr - Agatha Christie.epub'])


if __name__ == "__main__":
    app = ttk.Window("Peebook ePub reader", themename="cosmo")
    Peebook(app)
    app.mainloop()
