import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox

root = tk.Tk()
root.title('D&D')
root.iconbitmap('icon.ico')
root.configure(background='#89001c')
root.geometry('527x625')

logo = ImageTk.PhotoImage(Image.open('dnd.jpg'))
imgLabel = tk.Label(image=logo)
imgLabel.pack()
startButton = tk.Button(root, text='Start the game!', command=lambda: g.registerationWindow())
startButton.pack(pady=30)
logo1 = ImageTk.PhotoImage(Image.open('heroes.jpg'))
imgLabel1 = tk.Label(image=logo1)
imgLabel1.pack()


a = '''
                                            /-\                       /-\            ... Room
                       H                    | |                       | | Room       . . not on
                                            \#/                       \-/            ... map
                                             |              
                                      /-\   /#\   /-\                 /-\
                        G              | |-O-| #---+ |                 |:| Dark room
                                        \+/   \+/   \-/                 \-/
                                        |     X
                                /-\   ...   /+\                       /-\
                        F        | |   .?.---+ |                       |?| Special room
                                \+/   ...   \-/                       \-/
                                    |           O
                            /-\   /#\   /-\   /-\   /-\                 X   Locked door
                        E  |?|-O-| |   |?|   | #---# |                 #   Magic door
                            \+/   \-/   \+/   \+/   \-/                 O   Bombable wall
                            |     O     |     X
                            /+\   /-\   /#\   /+\                       4A - Entrance
                        D  |:#---# |   | +-X-+ |                       1E, 3E - Hints
                            \-/   \-/   \+/   \+/                       5C - Compass
                                        |     |                        4F - Map
                                /-\   /+\   /#\   /-\                 3F - 10 rupies
                        C        | #---+:+---# +-X-+:|                 2C, 3C, 4C, 1D,
                                \-/   \-/   \-/   \-/                   2D, 5A - Keys
                                                O                        2A - Stair to MAGIC BOOK
                                            /-\                       5G - Stair to MAGIC KEY
                        B                    | |                       5E - Stair to 1D
                                            \+/                       2F - Triforce
                                                |
                                /-\   /-\   /+\   /-\
                        A        | +---# +---+ +---+:|
                                \-/   \-/   \+/   \-/
'''

# #===================REMINDER!!!!=Center of screen!!!===============#


class GuiTools():
    def __init__(self, master):
        self.master = master

    def new_window(self):  # not in use
        self.window = tk.Toplevel(self.master)
        self.window.title('')
        self.window.iconbitmap('icon.ico')
        self.window.geometry('527x625')

    def areYouSure(self):
        self.response = messagebox.askokcancel('Start the game', 'Are you ready?')

        if self.response == 1:
            self.windowCh.destroy()
            self.windowMenu.destroy()
            return self.gameWindow()
        else:
            self.newChCreation()
            self.windowMenu.destroy()

    def popUp(self):
        self.choice4_btn = messagebox.askyesno('Quit the game', 'Are you sure?')

        if self.choice4_btn == 1:
            root.destroy()
            print("quit")
            # return Menu_loop.do_quit(True)
        else:
            print('Dont quit')
            self.windowMenu.destroy()
            return self.mainMenu()

    def registerationWindow(self):
        # ======creates new window======#
        self.windowReg = tk.Toplevel(self.master)
        self.windowReg.title('Registeration')
        self.windowReg.iconbitmap('icon.ico')
        self.windowReg.geometry('527x625')
        self.windowReg.configure(background='#89001c')
        # =====label / entry / button for username reg.====#
        self.usernameLabel = tk.Label(self.windowReg, text='Write down a unique name')
        self.usernameLabel.pack()
        self.username_txt = tk.Entry(self.windowReg, width=30)
        self.username_txt.pack(pady=10)
        self.regButton = tk.Button(self.windowReg, text='Register', command=lambda: [self.usernameHandler(), self.windowReg.destroy(), root.iconify()])
        self.regButton.pack()
        tk.Label(self.windowReg, text='OR').pack()
        self.continueWithoutReg = tk.Button(self.windowReg, text='Continue without registeration', command=lambda: [self.usernameHandler(), self.windowReg.destroy(), root.iconify()])
        self.continueWithoutReg.pack()
        # test shit
        # tk.Label(self.windowReg, text=self.regButton).pack()

    def usernameHandler(self):  # Checks user name
        if self.username_txt.get():
            # self.username = self.username_txt.get()  # connect with chcreation username
            # print(self.username)  # test shit
            print(self.username_txt.get())
            return self.mainMenu()
        else:
            return self.mainMenu()

    def newChCreation(self):
        self.windowCh = tk.Toplevel(self.master)
        self.windowCh.title('Character creation')
        self.windowCh.iconbitmap('icon.ico')
        self.windowCh.geometry('527x625')
        # =============Buttons For Hero Creation=============#

        self.wizardBtn = tk.Button(self.windowCh, text='Wizard', command=lambda: [self.areYouSure(), 'do_wizard', self.windowCh.destroy()])
        self.wizardBtn.pack(pady=5, ipadx=70)
        self.knightBtn = tk.Button(self.windowCh, text='Knight', command=lambda: [self.areYouSure(), 'do_knight', self.windowCh.destroy()])
        self.knightBtn.pack(pady=5, ipadx=70)
        self.thiefbtn = tk.Button(self.windowCh, text='Thief', command=lambda: [self.areYouSure(), 'do_thief', self.windowCh.destroy()])
        self.thiefbtn.pack(pady=5, ipadx=75)

        self.logoCh = ImageTk.PhotoImage(Image.open('heroes1.jpg'))
        self.imgLabelCh = tk.Label(self.windowCh, image=self.logoCh).pack()

    def loadCharacter(self):
        self.windowLoad = tk.Toplevel(self.master)
        self.windowLoad.title('Load screen')
        self.windowLoad.iconbitmap('icon.ico')
        self.windowLoad.geometry('527x625')

        pass

    def mainMenu(self):
        # creates new window
        self.windowMenu = tk.Toplevel(self.master)
        self.windowMenu.title('Main Menu')
        self.windowMenu.iconbitmap('icon.ico')
        self.windowMenu.geometry('527x625')
        # radio buttons / buttons for choices
        # -----------BUTTONS
        self.choice1_btn = tk.Button(self.windowMenu, text='Create a new character', command=lambda: self.newChCreation())
        self.choice1_btn.pack(padx=10, pady=10, ipadx=70)
        self.choice2_btn = tk.Button(self.windowMenu, text="Load an existing character", command=lambda: ['Menu_loop.do_load_character()', self.loadCharacter()])
        self.choice2_btn.pack(padx=10, pady=10, ipadx=59)
        self.choice3_btn = tk.Button(self.windowMenu, text="Start the game", command=lambda: ['Menu_loop.do_start_game()', self.windowMenu.destroy(), self.gameWindow()])
        self.choice3_btn.pack(padx=10, pady=10, ipadx=90)
        self.choice5_btn = tk.Button(self.windowMenu, text='Quit the game', command=lambda: self.popUp())
        self.choice5_btn.pack(padx=10, pady=10, ipadx=90)

        # test shit
        # tk.Label(self.windowMenu, text=self.choice1_btn).grid(row=15, column=1, columnspan=2, padx=10, pady=10, ipadx=40)

        # ch creation button for every each hero
        # message button for quit
        # message button for start! R u ready? Y/N
        # return gamemap()
        pass

    def gameWindow(self):
        # creates new window
        self.windowDnd = tk.Toplevel(self.master)
        self.windowDnd.title('Dungeon and Dragons')
        self.windowDnd.iconbitmap('icon.ico')
        self.windowDnd.geometry('527x625')
        # show map on window
        self.bisiler = tk.Label(self.windowDnd, text=a).pack()  # test map
        # =====Direction Buttons====
        self.northBtn = tk.Button(self.windowDnd, text='Go to North', command=lambda: 'do_north')
        self.southBtn = tk.Button(self.windowDnd, text='Go to South', command=lambda: 'do_south')
        self.eastBtn = tk.Button(self.windowDnd, text='Go to East', command=lambda: 'do_east')
        self.westBtn = tk.Button(self.windowDnd, text='Go to West', command=lambda: 'do_west')

        # ====Packing Buttons===
        self.eastBtn.pack(side='bottom', anchor='se')
        self.westBtn.pack(side='bottom', anchor='se')
        self.southBtn.pack(side='bottom', anchor='se')
        self.northBtn.pack(side='bottom', anchor='se')

        # =====If enemy founds:
        return self.battle()
        # =====else if shop founds:
            # return self.shop()

    def battle(self):
        # show hp bar for both side
        # attack/escape buttons
        # return gamemap()
        self.windowBattle = tk.Toplevel(self.master)
        self.windowBattle.title('You entered in a dungeon!')
        self.windowBattle.iconbitmap('icon.ico')
        self.windowBattle.geometry('800x625')
        # ======Dungeon image
        self.logoDungeon = ImageTk.PhotoImage(Image.open('dungeon.jpg'))
        self.imgLabelDungeon = tk.Label(self.windowBattle, image=self.logoDungeon)
        self.imgLabelDungeon.pack()
        # ======Dungoen Buttons======
        self.attackBtn = tk.Button(self.windowBattle, text='ATTACK!', command=lambda: [self.statusLabel.destroy(), ''])
        self.escapeBtn = tk.Button(self.windowBattle, text='ESCAPE!', command=lambda: [self.statusLabel.destroy(), ''])
        # ======Hp bar===============(testing)--attack->self.hpHandler()->self.battle===[RIMENDER]
        self.heroHpLabel = tk.Label(self.windowBattle, text='Your health points').pack(side='left')
        self.heroHP = ttk.Progressbar(self.windowBattle, orient='horizontal', length=200, mode='determinate')
        self.heroHP.pack(side='left')
        self.monsterHpLabel = tk.Label(self.windowBattle, text='Enemy health points').pack(side='right')
        self.monsterHP = ttk.Progressbar(self.windowBattle, orient='horizontal', length=200, mode='determinate')
        self.monsterHP.pack(side='right')
        # =====Fill the hp bars
        self.heroHP['value'] = 100  # hero.endurance
        self.monsterHP['value'] = 100  # monster.endurance

        # ======Dungeon Labels=======
        self.statusLabel = tk.Label(self.windowBattle, text='DungeonMaster.room_info')
        # ======Packing Buttons======
        self.attackBtn.pack()
        self.escapeBtn.pack()
        # ======Packing Labels=======
        self.statusLabel.pack()

        # if player dead:
            # return You are defeated window
        # elif if player escaped:
            # return self.gameWindow()
        # elif if monster defeated:
            # return self.gameWindow()
        #else:
            #You are escaped!
            #return self.gameWindow()


g = GuiTools(root)
root.mainloop()