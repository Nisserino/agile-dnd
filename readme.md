

###### _Grupp 6 eller nått (Rasmus N, Burak, Rasmus H, Joel, Olle, Jesper)_

 # __<h2> Gamedesign & Dungeon Run <h2>__
 
<br> <br> 
__<h1>Overview</h1>__
_Dungeon Run is a game where your goal is to have fun, and loot as many treasures as possible. Inside the treasures you can find gold. The gold you loot is what defines your highscore. <br> Be careful, there are enemies waiting for you along the way.<br> You can fight the enemies and kill them, or sometimes run away from them. <br> Once you have found all the treasures in a  room, you get moved to another room._

**Mechanics:**<br>
The game is object-oriented.<br>
_During the game experience there are 'hidden dices' that are being thrown in the background. This is what makes the experience of playing the game variate every time you play it. When you spawn, the exit door is randomly placed somewhere not too close to you. Spawning enemies, treasures are also random._ <br><br>
_When you are done playing the game, your character will still be saved. When you decide to play another time, your character will still be there. <br> 
Waiting for you to make a new highscore. Unless you want to create a new character and play another class._



<br><br>
_**To play the game you need:**<br>_
- 1 computer
- 1 player
- Have read the guide/manual
- Know English
<br><br>

## **_Guide - How to play_**
#
__If you are ever unsure of what you can do while in the game just type '*? or help*'.__ 
- [Create a character🧙](#Making-your-character)
- [Load your character](#Load-your-character)
- [Start the game](#Start-the-game)
- [Find treasures💰](#Treasures)
- [Combat⚔️](#Combat)
- [Enemies🧟‍♀️](#Enemies)
- [Winning conditions🏆](#Winning-conditions)
- [Game board🗺️](#Game-board)
- [Movement](#Movement)

<br><br>
## **_Making your character_**
#
_When you start the game for the first time you need to create a new character. <br> Typing **new_character** will give you the option to choose which character you want to play as. After that you get to decide your name._

<br><br>
<h2> Characters </h2> 

| Knight    | Theif | Wizard|
|:------------- |:----------------|:-------------|
| Initiative: 5 | Initiative: 7   | Initiative: 6|
| Endurance: 9  | Endurance: 5    | Endurance: 4 |
| Attack: 6     | Attack: 5       | Attack: 9    |
| Agility: 4    | Agility: 7      | Agility: 5   |

<br><br> 

***Each class have their own special ability***.
<br>
Knight: Shield block, always blocks the first attack in a battle.<br>
Wizard: Blinding light, makes monsters blind which increases your ability to escape by 80%<br>
Thief: Critical hit, has a 25% chance of doing double damage every attack_
<br><br>

<br><br>
## **_Load your character_**
#
To load your character type **load_character 'your name'**.<br> If you forget your name, you can type **see_characters** and a list of all names will be displayed.

<br><br>
## **_Start the game_**
#

To start playing a game you first need to do these steps:  
- Load_character '**your characters name**'
- Start_game  
- Pick a board size (small, medium, large)
- Choose which corner of the map to start (north_east, north_west, south_east, south_west)

<br><br>
## **_Treasures_**
#
There are 5 different types of treasures you can run into.
<br> They all have different spawn-chances. The lower procentage of them spawning, the bigger the loot.<br><br>
**_list of the treasures:_**
| Coins       | Coin bag        | Jewelry      | Gems            |Treasure Chest|        
|:-------------  |:----------------|:-------------|:-------------|:-------------|
| Chance: 40%    | Chance: 20%     | Chance: 6    | Chance: 15%  | Chance: 5%   |
| Gold: 2        | Gold: 6         | Gold: 3      | Gold: 10     | Gold: 20     |



<br><br>
## **_Combat_**
#
In some rooms you will encounter monsters.  
When in a combat scenario you have two options:
* _Attack_
* _Escape_

Your attacking and escaping success depend on your stats and luck when rolling the dice.

<br><br>
## **_Enemies_**
#
_**There are 4 different enemies that you can run into. Those are:**_
| Giantspider    |  Skeleton |        Orc |         Troll |
|:-------------  |:----------------|:-------------|:-------------|
| Initiative: 7  | Initiative: 4   | Initiative: 6| Initiative: 2|
| Endurance: 9   | Endurance: 2    | Endurance: 3 | Endurance: 4 |
| Attack: 2      | Attack: 3       | Attack: 4    | Attack: 7    |
| Agility: 3     | Agility: 3      | Agility: 4   | Agility: 2   |
| Chance: 20%    | Chance: 15%     | Chance: 10   | Chance: 5%   |


<br> </br>

## **_Winning conditions_**
#
_The objective of the game is to get as much gold as you can. To escape the dungeon
you need to find the room with an exit. When you find the exit room it will ask
if you want to leave or not.  
If you decide to leave, it will save all your gold
for that character. You can use that gold in the shop or keep it and try to get
as much as possible before dying.  
When your character dies or you give up(type give_up) it will save your name and
the amount of gold you have into the leaderboard. The leaderboard is ordered
by which character had the most gold when dying._

<br><br>
## **_Game board_**
#
**The different markers on the map are as follows:**
<br>
-   X = Unknown room
-   P = Your position
-   C = Cleared room
-   E = Room with an exit
-   R = You have escaped from this room

<h1><h1>

<br><br>
## **_Movement_**
#
**To walk around the dungeon you decide which way to go by typing:**
-   North
-   South
-   East
-   West
