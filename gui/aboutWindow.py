import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class AboutWindow(ttk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        print(f"Peebook v{parent.version}")
        self.title("About Peebook ebook reader")
        self.geometry("400x300")
        self.iconphoto(False, ttk.PhotoImage(file="gui/icons/ebook_32.png"))
        self.resizable(False, False)

        self.transient()
        self.grab_set()
        self.grid()
        self.position_center()

        self.label_frame = ttk.LabelFrame(self, text="About Peebook")
        self.label_frame.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        self.aboutText = ttk.StringVar()
        self.aboutText.set(
            f"Peebook v{parent.version}\
            \n\nPeebook is a ebook reader that has some Moonreader+ features.\
            \n\nRight now only epubs are supported.\
            \n\nRepo: https://github.com/tschertel/Peebook-TK \
            \nThis program is distributed for free under the terms of the GNU General Public License v3"
        )

        self.aboutLabel = ttk.Label(
            self.label_frame, textvariable=self.aboutText, justify=LEFT
        )
        self.aboutLabel.pack()

        self.ok_button = ttk.Button(self, text="OK", command=self.exit_btn)
        self.ok_button.pack(pady=10)

    def exit_btn(self):
        self.destroy()
