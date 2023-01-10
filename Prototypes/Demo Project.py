from guizero import App, Box, Text, TextBox, PushButton, Picture, Window, Slider
app = App(bg = "white", width= 3456, height= 2234, title="Menu")

middleWidth = 1368
middleHeight = 65
mainButtonWidth = 30

def openPlay():
    playWindow = Window(app, title = "Play", width= 3456, height= 2234)
    playWindow.show(wait = True) # wait stops user from using previous window
    app.hide() # option to hide

def openSettings():
    settingsWindow = Window(app, title = "Settings", width= 3456, height= 2234)
    settingsWindow.show(wait = True) # wait stops user from using previous window
    app.hide() # option to hide

def openLeaderBoard():
    leaderWindow = Window(app, title = "Leaderboard", width= 3456, height= 2234)
    leaderWindow.show(wait = True) # wait stops user from using previous window
    app.hide() # option to hide

def quit():
    app.destroy()

#SPACERS
spacer1 = Box(app, width="fill", height=70, align="top", border=True, layout="grid")
spacer2 = Box(app, width=70, height="fill", align="right", border=True)

#Title Box Elements
topSpacer = Box(app, height=300, width="fill", align="top", border=True, layout="grid")
titleBox = Box(topSpacer, height=300, width=1225, border=True, grid=[0,0])
settingsButton = PushButton(topSpacer, grid=[10,0], width=10, height=5, align="top", text="Settings", command=openSettings)
titleImage = Picture(titleBox, image="Images/f1.gif")

#Lower Button Elements
middleSpacer = Box(app,height=525, width="fill", border=True, layout="grid")

EmptyMiddleSpacer1 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,3],border=True,layout="grid")
FilledMiddleSpacer1 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,4],border=True)

EmptyMiddleSpacer2 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,5],border=True,layout="grid")
FilledMiddleSpacer2 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,6],border=True,)

EmptyMiddleSpacer3 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,7],border=True,layout="grid")
FilledMiddleSpacer3 = Box(middleSpacer, height=middleHeight, width=middleWidth,grid=[0,8],border=True,)

#Actual Buttons

playButton = PushButton(FilledMiddleSpacer1, width=mainButtonWidth, height=3, text = "PLAY",command=openPlay)
leaderButton = PushButton(FilledMiddleSpacer2, width=mainButtonWidth, height=3, text = "LEADERBOARD",command=openLeaderBoard)
quit = PushButton(FilledMiddleSpacer3, width=mainButtonWidth, height=3, text = "QUIT",command=quit)

#Volume Slider
volumeSlider = Slider(FilledMiddleSpacer2)

app.display()
