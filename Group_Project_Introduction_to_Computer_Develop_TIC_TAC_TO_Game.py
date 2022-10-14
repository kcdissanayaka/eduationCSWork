#!/usr/bin/env python
# coding: utf-8

# 
# # Project Team Members
# 
# 
# | Member Name | Role | Task Perfomed
# |:---|:---|:---|
# | Maduka Ramanayaka | Developer | * Code Develpment  <br> * Research  |
# | BOM Wongsakorn Sertsandee | Developer | * Code Develpment  <br> * Research|
# | Molagoda Dissanayakage Kasun Chathuranga Dissanayaka | Presenter |* Conduct Research on UI <br> * Demo the Presentation <br> * Develpment|
# 

# # Project Description  
# 
# As the final course assessment of the Introduction Computer Science subject, conducted by "Edunation Finland", it is required to develop a python application to evaluate the knowledge and the skills acquired from the course. There will be five group project topics. Out of five, one of the topics must be chosen, developed and deliver the solution within seven days.
# Further, this assignment must be delivered as a group project comprising four students.So we have choose the project topic one which is the develop a Tic Tac Toe game as our final project. 
# This document elaborates details of the poject implematation based on the instrauction given. 
# 
# 
#     
# #  Game Description Rules :  
# <br>
# The * Tic-Tac-Toe * , noughts and crosses , or **X**s and **O**s is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. It is a solved game, with a forced draw assuming best play from both players.
# 
#      
# 
# #  Approach for this Project :  
# 
#   * Schedule the first meeting 
#   * Finalized the project Topic
#   * Understand the Game
#   * First, we learn the game to understand its basics, rules and logic behind the game. 
#   
#   
# 
# First we learn the game to understand its rules and the loggic behind the game. Sencondly we finlized the stucure of the game board whether this 3x3 or more board which has more board cells. 
# then we agreed on the what will be deilivered as a final outcome. whether the ame will run on seperate UI or within Jupyter notebek IDE. Finally we all agreed our our final outcome goes with a seperate User Interface. 
# The we did resharch on the internet to find how GUI can be implement for our code. then we found out there "PyQt5","Tkinter" "Kivy","Wxpython" ect.. Out of that we desided to use Tkinter framework for develp our game
# 

# ## How to Play Tic Tac Toe Game
# * Follow the stpes
#  1. Once the Application is loaded to the screen, both the playears must enter their names to the fields.
#  2. Click on the "Start" button to start the Game.
#  3. Player one must click on a tile on the game board
#  4. Then game application will display the "X" on the selected tile.
#  5. Next, Player 2 ust select a Tile on the game board.
#  6. Then the Game board will show Player 2's selection as " O " on the tile.
#  7. Follow the *"Step 1"* and *"Step 5"* sequentially untill recevie a pop-up message as " Player Wins" or other wise "The game is Over, No One Wins"
#  8. Click QUIT button to exit or Click on the "Restart" play again.

# ### Game Code Implementation.
# 
# Since we disided to deliver the game in seperate graphysical we had to use framework that compatibile with python. for this implentation we use tkinter library  
# 
# 
# As first step installed the tkinter in anaconda enviroment and verfy.
# 
# 
# 

# **Step 2 Install Tcl/ Tk GUI toolkit!**
# 
# Import tkinter library to the enviroment

# #### Step 3 Import GUI libraries 
# **The tkinter Library    :** <br>
# *The Tkinter is apackage that can be used in python for GUI application development.
# Import Folloiwng Moduels*

# In[75]:


from tkinter import *    
from functools import partial
from tkinter import messagebox


# *Creating a Python dictionary to create a game board cell and give defined key values from 1 to 9 will use to identify the game board cells*

# In[76]:


theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


# *Define variable call 'clickType'. this variable to validate player input. This variable holds either X or O at a time. The default value is initially set to X, assuming that "the Player One" will click first.*
# 
# *Define another variable to called "count" to trace the number of user clicks. This will be limited to 9 in the program.*

# In[77]:


clickType= 'X'
count = 0


# **The clickTile Method    :** <br>
# 
# *reate a method called "clicktype" which executes when the player clicks the tile. This method uses the global keyword to access the "clicktype" and count variable. Once the user clicks on a tile, it will check the number of user clicks in the count variable. If the count is less the 10 will check whether the user has clicked on the tile, which is empty. It will execute the rest of the code if it is empty.
# Then the program will assign the click type of the user (x or O) to the value under the particular key value in the dictionary.
# Finally, assign the  "Click type" of the next player to the click type" Variable.*
# 
# the system will increment the number of count.
# 
# then the label of the button changed to the value in the clicktype to display it on the screen. <br>
# 
# then will use the validateTile method to check the any wining pattern exist.
# 
# 
# 

# In[78]:


def clickTile(val):
    
    global clickType, count
   
    if count < 10:
        
        if theBoard[val] == ' ':
            theBoard[val] = clickType
            count += 1 #increese count by one
            if val == "9":
                nine["text"] = clickType
            elif val == "8":
                eight["text"] = clickType
            elif val == "7":
                seven["text"] = clickType
            elif val == "6":
                six["text"] = clickType
            elif val == "5":
                five["text"] = clickType
            elif val == "4":
                four["text"] = clickType
            elif val == "3":
                three["text"] = clickType
            elif val == "2":
                two["text"] = clickType
            elif val == "1":
                one["text"] = clickType
            validateTile(clickType,count)

            if clickType =='X':
                clickType = 'O'
            else:
                clickType = 'X'
        else:
            showMsg("Opps", "That place is already filled. Try an another Tile ?")
    else:
        showMsg("Game over", "No One Wins, Try Again !")
       


# **The showMsg Method    :** <br>
# 
# Next Defiend a method to display messaage as pop up.

# In[79]:


def showMsg (title,message):
    messagebox.showinfo(title,message)


# **The validateTile Method    :** <br>
# 
# *The "validateTiel" is used to check the winner. It checks eight winning combinations in the game rule. If the tile combinations are equal, the "showMsg" method to display the winning player name at the end will validate that the count equals nine and show the message Game Over No one wins.

# In[80]:


def validateTile(clickType,count):
    
    winner = ""
    if clickType == "X":
        winner = player_one.get()
    else:
        winner = player_two.get()
        
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
        showMsg("Game over", winner + " won!")
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        showMsg("Game over", winner + " won!")
    elif count == 9:
        showMsg("Game over",  "No One Winns!")


# #### The restart Method :
# 
# Use this method to initialize all the varibles and restart the game application again.
# further it also disable the all tiles and the restart button untile the Start button is pressed.
# and also clear the Player names from the game application.
# 

# In[81]:


def restart():
    global clickType, count, theBoard
    nine["text"] = ""
    eight["text"] = ""
    seven["text"] = ""
    six["text"] = ""
    five["text"] = ""
    four["text"] = ""
    three["text"] = ""
    two["text"] = ""
    one["text"] = ""
    
    nine["state"] = "disabled"
    eight["state"] = "disabled"
    seven["state"] = "disabled"
    six["state"] = "disabled"
    five["state"] = "disabled"
    four["state"] = "disabled"
    three["state"] = "disabled"
    two["state"] = "disabled"
    one["state"] = "disabled"
    restart["state"] = "disabled"
    
    player_one.delete(0, END)
    player_two.delete(0, END)
    
    clickType = "X"
    count = 0
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


# #### The StartGame method :
# This will be the method user to start the game. 
# this will first check the both players names are empty if not then enable the tile state property to normal so that the player can click on the tiles on the board.

# In[82]:


def startGame():    
    if  player_one.get() and len(player_one.get()) != 0 and player_one.get().strip():
        if  player_two.get() and len(player_two.get()) != 0 and player_two.get().strip():
            nine["state"] = "normal"
            eight["state"] = "normal"
            seven["state"] = "normal"
            six["state"] = "normal"
            five["state"] = "normal"
            four["state"] = "normal"
            three["state"] = "normal"
            two["state"] = "normal"
            one["state"] = "normal"
            restart["state"] = "normal"
        else:
            showMsg("Oops",  "P2 name required!")
    else:
        showMsg("Oops",  "P1 name required!")


# #### Create GUI For TIC TAC TO GAME
# 
# Define game window size and the title of the window 

# In[83]:


root = Tk()
root.geometry("230x360")
root.title('Tic Tac Toe ')


# *Deine Input fields in the UI to get Player names*

# In[84]:


label_one = Label( root, text="P1 name (X)" )
label_one.grid(row=0, column=0,padx=5, pady=5)

player_one =Entry(root)
player_one.grid(row=0, column=1, columnspan= 2)

label_two = Label( root, text="P2 name (O)")
label_two.grid(row=1, column=0,padx=5, pady=5)

player_two = Entry(root)
player_two.grid(row=1, column=1, columnspan= 2)


# ### Creating Play Board Area
# 
# In the code cell deinfe the Main command button in the game. 
# 

# In[85]:


restart = Button(root, text="RESTART", height=2,width=8, command=restart, state= DISABLED, bg = "yellow",fg='white')
restart.grid(row=2, column=0,padx=5, pady=5)

start = Button(root, text="START", height=2,width=8, command=startGame,  bg = "green",fg='white')
start.grid(row=2, column=1,padx=5, pady=5)

quit = Button(root, text="QUIT", height=2,width=8, command=root.destroy,  bg = "red",fg='white')
quit.grid(row=2, column=2,padx=5, pady=5)


# ### Define Game board tiles 
# when the progame starts all the tile are in disable state.

# In[86]:


seven = Button(root, height=4,width=8, command=partial(clickTile, "7"), state= DISABLED)
seven.grid(row=3, column=0,padx=5, pady=5)    

eight = Button(root, height=4,width=8, command=partial(clickTile, "8"), state= DISABLED)
eight.grid(row=3, column=1,padx=5, pady=5)

nine = Button(root, height=4,width=8, command=partial(clickTile, "9"), state= DISABLED)
nine.grid(row=3, column=2,padx=5, pady=5)


# In[87]:


four = Button(root, height=4,width=8, command=partial(clickTile, "4"), state= DISABLED)
four.grid(row=4, column=0,padx=5, pady=5)    

five = Button(root, height=4,width=8, command=partial(clickTile, "5"), state= DISABLED)
five.grid(row=4, column=1,padx=5, pady=5)

six = Button(root, height=4,width=8, command=partial(clickTile, "6"), state= DISABLED)
six.grid(row=4, column=2,padx=5, pady=5)


# In[88]:


one = Button(root, height=4,width=8, command=partial(clickTile, "1"), state= DISABLED)
one.grid(row=5, column=0,padx=5, pady=5)    

two = Button(root, height=4,width=8, command=partial(clickTile, "2"), state= DISABLED)
two.grid(row=5, column=1,padx=5, pady=5)

three = Button(root,height=4,width=8, command=partial(clickTile, "3"), state= DISABLED)
three.grid(row=5, column=2,padx=5, pady=5)



# This will open the game window 

# In[89]:


root.mainloop()


# ## Learning Outcome 
# * How tkinter in python
# * How to handle Tkinter widgets and attributes when designing UIs
# * How to use python dictionary
# * Handling global Variable within a method
# * How to use the strip() method to remove white spaces in the text.
# * Enhance the knowledge of the usage of anaconda and Jupiter notebook.
# * HTeam Work and Project Planning

# In[90]:


"""class tctactoGame(tikto.Frame):
    def __init__(self,master=None):
        tikto.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.quiteButton = tikto.Button(self, text= 'Quite', command=self.quit)
        self.quiteButton.grid()
        
app = tctactoGame()
app.master.title("PLAY TIC TAC TO GAME")
app.mainloop() """






        
        


# In[ ]:




