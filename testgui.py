import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('D&D')
root.iconbitmap('icon.ico')

root.geometry('800x600')

logo = ImageTk.PhotoImage(Image.open('dnd.jpg'))
imgLabel = tk.Label(image=logo)
imgLabel.pack()


class GuiTools():
    def __init__(self, master):
        self.master = master

    def new_window(self):
        self.window = tk.Toplevel(self.master)
        self.window.title = ('')
        self.window.iconbitmap('icon.ico')
        self.window.geometry('800x600')

    def popUp(self):
        self.choice4_btn = messagebox.askyesno('Quit the game', 'Are you sure?')

    def registerationWindow(self):
        # creates new window
        self.window = tk.Toplevel(self.master)
        self.window.title = ('Registeration')
        self.window.iconbitmap('icon.ico')
        self.window.geometry('800x600')
        # label / entry / button for username reg.
        self.usernameLabel = tk.Label(self.window, text='Write down a unique name')
        self.usernameLabel.pack()
        self.username_txt = tk.Entry(self.window, width=30)
        self.username_txt.pack(pady=10)
        self.regButton = tk.Button(self.window, text='Register', command=lambda: g.mainMenu())
        self.regButton.pack()

    def mainMenu(self):
        self.username = self.username_txt.get()  # connect with chcreation username
        print(self.username)  # test shit
        # creates new window
        self.window = tk.Toplevel(self.master)
        self.window.title = ('Main Menu')
        self.window.iconbitmap('icon.ico')
        self.window.geometry('800x600')
        # radio buttons / buttons for choices
        # -----------BUTTONS
        self.choice1_btn = tk.Button(self.window, text='Create a new character', command=lambda: 'Menu_loop.do_new_character()')
        self.choice1_btn.grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=70)
        self.choice2_btn = tk.Button(self.window, text="Load an existing character", command=lambda: 'Menu_loop.do_load_character()')
        self.choice2_btn.grid(row=7, column=1, columnspan=2, padx=10, pady=10, ipadx=55)
        self.choice3_btn = tk.Button(self.window, text="Start the game", command=lambda: 'Menu_loop.do_start_game()')
        self.choice3_btn.grid(row=8, column=1, columnspan=2, padx=10, pady=10, ipadx=40)
        self.choice5_btn = tk.Button(self.window, text='Quit the game', command=lambda: g.popUp())
        self.choice5_btn.grid(row=9, column=1, columnspan=2, padx=10, pady=10, ipadx=40)

        if self.choice4_btn == 1:
            # return Menu_loop.do_quit(True)
            pass
        else:
            return g.mainMenu()

        # ch creation button for every each hero
        # message button for quit
        # message button for start! R u ready? Y/N
        # return gamemap()
        pass

    def gamemap(self):
        # creates new window
        # show map on window
        # directions choices
        # return battle()
        pass

    def battle(self):
        # show dungeon!????
        # show hp bar for both side
        # attack/escape buttons
        # return gamemap()
        pass


startButton = tk.Button(root, text='Start the game!', command=lambda: g.registerationWindow())
startButton.pack(pady=30)

g = GuiTools(root)
root.mainloop()
