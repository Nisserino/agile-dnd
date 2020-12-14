# Dungeon run
You're in a dungeon and the objective of the game is to clear the rooms of potential foes and gather any treasures that
you may find. The only way for you to escape with your life and gold intact is to find the exit that is hidden somewhere
in the dungeon.

## How to play
##### If you are ever unsure of what you can do while in the game just type ? or help.  

When starting up the game for the first time you should create a new character to play as.  
Enter new_character and from there it will ask you which character you want to play.  

**three characters to choose from**
* Knight
* Wizard
* Thief  

*They all have different stats, check further down in this document to see the stats*  

Choose any name for your new character.  
## Starting a game
To start playing a game you first need to do these steps:  
1. load_character [your characters name]
2. start_game  
3. choose a board size (small, medium, large)
4. Choose which corner of the map to start (north_east, north_west, south_east, south_west)  

You have now started a new game and should see a game board

## Game board
The different markers on the map are as follows:  
* X = Unknown room
* P = Your position
* C = Cleared room
* E = Room with an exit
* R = You have escaped from this room  

## Movement
To walk around the dungeon you decide which way to go by typing:
* North
* South
* East 
* West

## Combat
In some rooms you will encounter treasures and/or monsters.  
When in a combat scenario you have two options:
* Attack
* Escape  

Your attacking and escaping success depend on your stats and luck when rolling the dice.

## Winning conditions
The objective of the game is to get as much gold as you can. To escape the dungeon
you need to find the room with an exit. When you find the exit room it will ask
if you want to leave or not.  
If you decide to leave, it will save all your gold
for that character. You can use that gold in the shop or keep it and try to get
as much as possible before dying.  
When your character dies or you give up(type give_up) it will save your name and
the amount of gold you have into the leaderboard. The leaderboard is ordered
by which character had the most gold when dying.  
  
  
## Heroes
There are 3 different heroes to pick from.  
They all have different stats and one unique special ability.

| Knight    | Thief | Wizard|
|:------------- |:----------------|:-------------|
| Initiative: 5   | Initiative: 7| Initiative: 6|
| Endurance: 9    | Endurance: 5 | Endurance: 4 |
| Attack: 6       | Attack: 5    | Attack: 9    |
| Agility: 4      | Agility: 7   | Agility: 5   |

**Special abilities**

**Knight**: Shield block, always blocks the first attack in a battle.  
**Wizard**: Blinding light, makes monsters blind which increases your ability to escape by 80%  
**Thief**: Critical hit, has a 25% chance of doing double damage every attack.
## Treasures
Some rooms contain treasures, if there's monsters in the room you have to slay them before collecting the treasures.  
Differet treasures have different values:
* Coin bag = 6 Gold
* Jewlery = 10 Gold
* Gems = 14 Gold
* Treasure chest = 20 Gold
