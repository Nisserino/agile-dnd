import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import DungeonMaster as DM
from roomdesc import RoomDescription
from game_loop import CombatLoop
import menue as M
import subprocess


root = tk.Tk()
root.title('D&D')
root.iconbitmap('icon.ico')
root.configure(background='#89001c')
w = 527
h = 650
# ======Specifiy windows location=======
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# ======Image/Logo/Icon
logo = ImageTk.PhotoImage(Image.open('dnd.jpg'))
imgLabel = tk.Label(image=logo)
imgLabel.pack()
startButton = tk.Button(root, text='Start the game!', command=lambda: g.mainMenu())
startButton.pack(pady=30)
logo1 = ImageTk.PhotoImage(Image.open('heroes.jpg'))
imgLabel1 = tk.Label(image=logo1)
imgLabel1.pack()

# ======================================= # ============================ #
# combat = CombatLoop()
# pickBoard = PickBoardSize()

a = '''
'''


class GuiTools():
    def __init__(self, master):
        self.master = master
        self.width = 527
        self.height = 650
        self.ws = self.master.winfo_screenwidth()
        self.hs = self.master.winfo_screenheight()
        self.x = (self.ws/2) - (self.width/2)
        self.y = (self.hs/2) - (self.height/2)

    def testFunc(self):
        pass

    def areYouSure(self):
        self.response = messagebox.askyesno('Hero selection', 'Are you ready?')

        if self.response == 1:
            self.windowCh.destroy()
            return self.registerationWindow()
        else:
            return self.windowCh

    def popUp(self):
        self.choice4_btn = messagebox.askyesno('Quit the game', 'Are you sure?')

        if self.choice4_btn == 1:
            root.destroy()
            # print("quit")
        else:
            # print('Dont quit')
            return self.mainMenu()

    def registerationWindow(self):
        # ======creates new window======#
        self.windowReg = tk.Toplevel(self.master)
        self.windowReg.title('Registeration')
        self.windowReg.iconbitmap('icon.ico')
        self.windowReg.geometry('%dx%d+%d+%d' % (w, h, x, y))
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
        self.child = subprocess.Popen(['python', 'menue.py'], stdin=subprocess.PIPE)
        self.child.communicate(self.username_txt.get())

    def newChCreation(self):
        self.windowCh = tk.Toplevel(self.master)
        self.windowCh.title('Character creation')
        self.windowCh.iconbitmap('icon.ico')
        self.windowCh.configure(background='#89001c')
        self.windowCh.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # ============Image==================
        self.logoCh = ImageTk.PhotoImage(Image.open('heroes1.jpg'))
        self.imgLabelCh = tk.Label(self.windowCh, image=self.logoCh).pack()
        # =============Hero creation buttons========
        self.wizardBtn = tk.Button(self.windowCh, text='Wizard', command=lambda: [self.areYouSure() , chCreate.do_wizard('wizard')])
        self.knightBtn = tk.Button(self.windowCh, text='Knight', command=lambda: [self.areYouSure(), chCreate.do_knight('knight')])
        self.thiefBtn = tk.Button(self.windowCh, text='Thief', command=lambda: [self.areYouSure(), chCreate.do_theif('theif')])
        # ============Buttons placement============
        self.wizardBtn.pack(pady=5, ipadx=70)
        self.knightBtn.pack(pady=5, ipadx=70)
        self.thiefBtn.pack(pady=5, ipadx=75)

    def loadCharacter(self):
        # =======Create a new window========
        self.windowLoad = tk.Toplevel(self.master)
        self.windowLoad.title('Load screen')
        self.windowLoad.iconbitmap('icon.ico')
        self.windowLoad.configure(background='#89001c')
        self.windowLoad.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # =======Show saved files============
        self.loadBtn = []
        for i in range(10):
            self.loadBtn.append(tk.Button(self.windowLoad, text='Load file ' + str(i+1), command=lambda i=i: 'Menue_loop.do_load_character, self.open_this(i)'))
            self.loadBtn[i].pack()  # grid(column=4, row=i+1, sticky='w')
        # =======Load and Quit Buttons=======
        # self.loadBtn = tk.Button(self.windowLoad, text='LOAD', command=lambda: '')
        self.quitBtn = tk.Button(self.windowLoad, text='Return the main menu', command=lambda: [self.windowMenu, self.windowLoad.destroy()])
        self.quitBtn.pack()

    def mainMenu(self):
        # creates new window
        self.windowMenu = tk.Toplevel(self.master)
        self.windowMenu.title('Main Menu')
        self.windowMenu.iconbitmap('icon.ico')
        self.windowMenu.configure(background='#89001c')
        self.windowMenu.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # radio buttons / buttons for choices
        # -----------BUTTONS
        self.choice1_btn = tk.Button(self.windowMenu, text='Create a new character', command=lambda: [self.newChCreation(), M.Menue_loop().onecmd('new_character')])
        self.choice1_btn.pack(padx=10, pady=10, ipadx=70)
        self.choice2_btn = tk.Button(self.windowMenu, text="Load an existing character", command=lambda: [self.loadCharacter(), M.Menue_loop().onecmd('load_character')])
        self.choice2_btn.pack(padx=10, pady=10, ipadx=59)
        self.choice3_btn = tk.Button(self.windowMenu, text="Start the game", command=lambda: [M.Menue_loop().onecmd('start_game'), self.mapSize(), self.windowMenu.destroy(), M.Menue_loop().onecmd('start_game')])
        self.choice3_btn.pack(padx=10, pady=10, ipadx=90)
        self.choice5_btn = tk.Button(self.windowMenu, text='Quit the game', command=lambda: [self.popUp(), M.Menue_loop().onecmd('quit')])
        self.choice5_btn.pack(padx=10, pady=10, ipadx=90)

        # test shit
        # tk.Label(self.windowMenu, text=self.choice1_btn).grid(row=15, column=1, columnspan=2, padx=10, pady=10, ipadx=40)

        # ch creation button for every each hero
        # message button for quit
        # message button for start! R u ready? Y/N
        # return gamemap()
        pass

    def mapSize(self):
        # creates new window
        # self.mapSizeWindow = tk.Toplevel(self.master)
        # self.mapSizeWindow.title('Chosing map size')
        # self.mapSizeWindow.iconbitmap('icon.ico')
        # self.mapSizeWindow.configure(background='#89001c')
        # self.mapSizeWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # self.map = tk.IntVar()
        # self.smallMap = tk.Radiobutton(self.mapSizeWindow(), text='', variable=self.map, value=1).pack()
        # self.mediumMap = tk.Radiobutton(self.mapSizeWindow(), text='', variable=self.map, value=2).pack()
        # self.bigMap = tk.Radiobutton(self.mapSizeWindow(), text='', variable=self.map, value=3).pack()

        # if self.map.get() == 1:
        #     return pickBoard.do_small()
        # elif self.map.get() == 2:
        #     return pickBoard.do_medium()
        # else:
        #     return pickBoard.do_big()
        return self.gameWindow()

    def gameWindow(self):
        # creates new window
        self.windowDnd = tk.Toplevel(self.master)
        self.windowDnd.title('Dungeon and Dragons')
        self.windowDnd.iconbitmap('icon.ico')
        self.windowDnd.configure(background='#89001c')
        self.windowDnd.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # show map on window
        self.bisiler = tk.Label(self.windowDnd, text=a).pack()  # test map
        # =====Direction Buttons====
        self.northBtn = tk.Button(self.windowDnd, text='Go to North', command=lambda: 'do_north')
        self.southBtn = tk.Button(self.windowDnd, text='Go to South', command=lambda: 'do_south')
        self.eastBtn = tk.Button(self.windowDnd, text='Go to East', command=lambda: 'do_east')
        self.westBtn = tk.Button(self.windowDnd, text='Go to West', command=lambda: 'do_west')
        # ====Packing Buttons===
        self.eastBtn.pack(anchor='e', pady=10)
        self.westBtn.pack(anchor='w', pady=10)
        self.southBtn.pack(anchor='s', pady=10)
        self.northBtn.pack(anchor='n', pady=10)

        # =====If enemy founds:
        return self.battle()
        # =====else if shop founds:
            # return self.shop()

    def buyItems(self):  # ============TESTING===================
        self.varList = [self.variableHp.get(), self.bigPotVar.get(), self.armorVar.get(), self.swordVar.get()]
        self.counter = 0
        for i in range(len(self.varList)):
            if self.varList[i] == 'On':
                self.counter += 1
        self.boughtLabel = tk.Label(self.windowShop, text='You bought ' + str(self.counter) + ' item/s').pack()

    def shop(self):
        # =======Create new window
        self.windowShop = tk.Toplevel(self.master)
        self.windowShop.title('Shop')
        self.windowShop.iconbitmap('icon.ico')
        self.windowShop.configure(background='#89001c')
        self.windowShop.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # =======Images==========
        self.hpPotPic = ImageTk.PhotoImage(Image.open('small_hp_pot.png'))
        self.bigHpPotPic = ImageTk.PhotoImage(Image.open('big_hp_pot.png'))
        self.bodyArmorPic = ImageTk.PhotoImage(Image.open('body_armor.png'))
        self.swordPic = ImageTk.PhotoImage(Image.open('sword.jpg'))
        # =======Image placement==
        self.hpPotLabel = tk.Label(self.windowShop, image=self.hpPotPic).pack()
        self.bigHpPotLabel = tk.Label(self.windowShop, image=self.bigHpPotPic).pack()
        self.bodyArmorLabel = tk.Label(self.windowShop, image=self.bodyArmorPic).pack()
        self.swordLabel = tk.Label(self.windowShop, image=self.swordPic).pack()
        # =======Buttons=========
        self.buyBtn = tk.Button(self.windowShop, text='Buy', command=lambda: self.buyItems())
        self.goBackBtn = tk.Button(self.windowShop, text='Go back', command=lambda: '')
        # ======Button placement
        self.buyBtn.pack()
        self.goBackBtn.pack()
        # ======Check List=====
        self.hpPotSmall = tk.Checkbutton(self.windowShop, text='Small Hp potion')
        self.variableHp = tk.StringVar()
        self.hpPotSmall.config(variable=self.variableHp, onvalue='On', offvalue='Off')
        self.hpPotSmall.deselect()
        self.hpPotSmall.pack()  # Replace=======
        self.hpPotBig = tk.Checkbutton(self.windowShop, text='Big Hp potion')
        self.bigPotVar = tk.StringVar()
        self.hpPotBig.config(variable=self.bigPotVar, onvalue='On', offvalue='Off')
        self.hpPotBig.deselect()
        self.hpPotBig.pack()  # Replace=======
        self.bodyArmor = tk.Checkbutton(self.windowShop, text='Body armor')
        self.armorVar = tk.StringVar()
        self.bodyArmor.config(variable=self.armorVar, onvalue='On', offvalue='Off')
        self.bodyArmor.deselect()
        self.bodyArmor.pack()  # Replace=======
        self.sword = tk.Checkbutton(self.windowShop, text='Sword')
        self.swordVar = tk.StringVar()
        self.sword.config(variable=self.swordVar, onvalue='On', offvalue='Off')
        self.sword.deselect()
        self.sword.pack()  # Replace=======

    def defeat(self):
        # =======Create new window
        self.windowDefeat = tk.Toplevel(self.master)
        self.windowDefeat.title('Dungeon and Dragons')
        self.windowDefeat.iconbitmap('icon.ico')
        self.windowDefeat.configure(background='#89001c')
        self.windowDefeat.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # put a defeat image
        # quit/ play again close all windows

    def hpHandler(self):
        # ======Hp bar===============(testing)
        self.heroHpLabel = tk.Label(self.windowBattle, text='Your health points').pack(anchor='w')
        self.heroHP = ttk.Progressbar(self.windowBattle, orient='horizontal', length=200, mode='determinate')
        self.heroHP.pack(anchor='w')
        # =======Multipple Hp bar for monsters=
        self.monsterHPBars = []
        for i in range(4):
            self.monsterHPLabel = tk.Label(self.windowBattle, text='Monster health points').pack(anchor='e')
            self.monsterHPBars.append(ttk.Progressbar(self.windowBattle, orient='horizontal', length=200, mode='determinate'))
            self.monsterHPBars[i].pack(anchor='e')  # grid(column=4, row=i+1, sticky='w')
            self.monsterHPBars[i]['value'] = 100  # monster.endurance*10
        # =====Fill the hp bars
        self.heroHP['value'] = 100  # hero.endurance*10

        if self.heroHP['value'] > 0 and self.monsterHPBars['value'] == 0:
            self.answer = messagebox.showinfo('Victory!', 'You won!')
            if self.answer.lower() == 'ok':
                self.windowBattle.destroy()
                self.windowDnd.destroy()
                return self.gameWindow()
        else:
            self.answer = messagebox.showinfo('You are died', 'You are defeated!')
            if self.answer.lower() == 'ok':
                self.windowBattle.destroy()
                self.windowDnd.destroy()
                return self.defeat()

    # def checkStats(self):  # To check stats in dungeon
    #     self.statsLabel = tk.Label(self.windowBattle, text='combat.get_stats'()).pack()

    def battle(self):
        self.windowBattle = tk.Toplevel(self.master)
        self.windowBattle.title('You entered in a dungeon!')
        self.windowBattle.iconbitmap('icon.ico')
        self.windowBattle.configure(background='#89001c')
        self.windowBattle.geometry('%dx%d+%d+%d' % (800, 625, x, y))
        # ======Dungeon image=======
        self.logoDungeon = ImageTk.PhotoImage(Image.open('dungeon.jpg'))
        self.imgLabelDungeon = tk.Label(self.windowBattle, image=self.logoDungeon)
        self.imgLabelDungeon.pack()
        # ======Dungeon Description==
        self.randomdesc = '''
        aslkdjasldkjkasldjaskldjsakdljaskdlasjdladasl
        lsdklf;lsdfks;ldfk;lasdkas;ldkas;dlaskdl;asdk
        sd;lfksdl;fksdf;lksdf;lksdf;lskdf;lsdkf;lsdfk
        sdlkfsdlkfjsdflksdf;sdlfksdf;lkf;sdkfsd;fks;d
        ;sldkfsd;lfksd;flksdf;lskdf;lsfdks;dflksd;fks
        '''
        self.descVar = tk.StringVar()
        self.descVar.set(RoomDescription().get_description())
        self.descLabel = tk.Label(self.windowBattle, textvariable=self.descVar, bg='black', fg='white').pack()
        # ======Dungeon Buttons======
        self.attackBtn = tk.Button(self.windowBattle, text='ATTACK!', command=lambda: [self.hpHandler(), self.statusLabel.destroy(), 'do_attack()'])
        self.escapeBtn = tk.Button(self.windowBattle, text='ESCAPE!', command=lambda: [self.shop(), self.statusLabel.destroy(), 'do_escape()'])
        self.statsBtn = tk.Button(self.windowBattle, text='See Stats!', command=lambda: [self.descLabel.destroy(), self.statusLabel.destroy(), self.checkStats()])
        # ======Dungeon Labels=======
        self.statusLabel = tk.Label(self.windowBattle, text='DM.DungeonMaster.print_room_status()')
        # ======Packing Buttons======
        self.attackBtn.pack()
        self.escapeBtn.pack()
        self.statsBtn.pack()
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
menu = M.Menue_loop()
chCreate = M.CharacterCreationLoop(menu.data_handler)
root.mainloop()
