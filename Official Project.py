from guizero import App, Box, Text, TextBox, PushButton, Picture, Window
import random, time, pickle
from statistics import mean
app = App(bg = "white", width= 3456, height= 2234, title="Menu")
TimeCounter = 0
UserTimes = []
UserTimes2 = []
UserNames = []
startTime = 0

#Creating a Large Function in order to manage all the separate Windows.
def menu():
    global app
    TimeToGreen = random.randint(6000,10000)
    spacerSeparationHeight = 161
    iconNumber = 50

    #Here there is a separation of the screen in order to improve organisation.
    spacerRight = Box(app, width=600, height="fill", align="right", border=False)
    spacerLeft = Box(app, width=2856, height="fill", align="left", border=False)
    spacerOverTop = Box(spacerRight, width="fill", height=20, border=False, align="Top")
    spacerTop = Box(spacerRight, width="fill", height=100, border=False)

    spacerTopMR = Box(spacerTop, width=300, height="fill", align="right", border=False)
    spacerTopML = Box(spacerTop, width=300, height="fill", align="left", border=False)

    spacerTitleImage = Box(spacerLeft, width = 900, height=300, align="top",border=False)
    spacerButtonsBox = Box(spacerLeft, width = "fill", height=1934, align="bottom",border=False)

    spacerButtonImagesL = Box(spacerButtonsBox, width=418, height="fill", align="left", border=False)
    spacerButtonImagesR = Box(spacerButtonsBox, width=418, height="fill", align="right", border=False)

    spacerlineSeparation1 = Box(spacerButtonImagesR, width="fill",height=spacerSeparationHeight,align="top",border=False)
    spacerlineSeparation2 = Box(spacerButtonImagesR, width="fill",height=spacerSeparationHeight,border=False)
    spacerlineSeparation3 = Box(spacerButtonImagesR, width="fill",height=spacerSeparationHeight,align="bottom",border=False)

    spacerlineSeparation4 = Box(spacerButtonImagesL, width="fill",height=spacerSeparationHeight,align="top",border=False)
    spacerlineSeparation5 = Box(spacerButtonImagesL, width="fill",height=spacerSeparationHeight,border=False)
    spacerlineSeparation6 = Box(spacerButtonImagesL, width="fill",height=spacerSeparationHeight,align="bottom",border=False)

    spacerButtonImage1 = Box(spacerlineSeparation4, width=100, height=spacerSeparationHeight,align="left",border=False)
    spacerButtonImage2 = Box(spacerlineSeparation5, width=100, height=spacerSeparationHeight,align="left",border=False)
    spacerButtonImage3 = Box(spacerlineSeparation6, width=100, height=spacerSeparationHeight,align="left",border=False)

    spacerSupportButton1 = Box (spacerlineSeparation4, width="fill", height = 30,border=False)
    spacerSupportButton2 = Box (spacerlineSeparation5, width="fill", height = 30,border=False)
    spacerSupportButton3 = Box (spacerlineSeparation6, width="fill", height = 30,border=False)

    ButtonImageSpacer1 = Box(spacerlineSeparation4, width=100, height=100,border=False)
    ButtonImageSpacer2 = Box(spacerlineSeparation5, width=100, height=100,border=False)
    ButtonImageSpacer3 = Box(spacerlineSeparation6, width=100, height=100,border=False)

    titleImageSpacer = Box(spacerTitleImage, align="left", width=200, height="fill")
    titleImage = Picture(spacerTitleImage, align="right", image="Images/DD_Project/TitleF1.gif")

    PlayButton = Picture(ButtonImageSpacer1, image="Images/DD_Project/play-button.gif")
    LeaderBoardButton = Picture(ButtonImageSpacer2, image="Images/DD_Project/crown.gif")
    QuitButton = Picture(ButtonImageSpacer3, image="Images/DD_Project/delete.gif")

    spacerBeforeCharacter = Box(spacerRight, width = "fill", height=150, border = False)
    funCharacterImage = Picture(spacerRight, image="Images/DD_Project/funCharacter.gif")

    #BUTTON IMAGES
    inButtonSpacer = Box(spacerlineSeparation1, align="top", width="fill",height=35)
    buttonPlay = Picture(spacerlineSeparation1, image="Images/DD_Project/Buttons/White Play.png")

    inButtonSpacer2 = Box(spacerlineSeparation2, align="top", width="fill",height=35)
    buttonLeaderBoard = Picture(spacerlineSeparation2, image="Images/DD_Project/Buttons/White LeaderBoard.png")

    inButtonSpacer3 = Box(spacerlineSeparation3, align="top", width="fill",height=35)
    buttonQuit = Picture(spacerlineSeparation3, image="Images/DD_Project/Buttons/White Quit.png")

    musicVolumeImage = Picture(spacerTopML, image="Images/DD_Project/Buttons/MusicVolumeImage.png")
    musicBox = Box(spacerTopMR, align="top", width="fill", height = 18, border=False)

    musicVolumeWhiteSlider = Box(spacerTopMR, width=230, height=35, border=False)
    musicVolumeRedSlider = Picture(musicVolumeWhiteSlider, image = "Images/DD_Project/Buttons/Red Slider.png")
    musicVolumeRedSlider.bg = "red"

    #Here are all the functions involving a slider.

    #mousePosX = event_data.x

    def redSliderEffect():
        musicVolumeRedSlider.image = "Images/DD_Project/Buttons/Red Slider.png"
        #musicVolumeRedSlider.width = mousePosX

    musicVolumeRedSlider.when_mouse_dragged = redSliderEffect

    #Here are all the functions involving the button images.

    def hoverPlayButton():
        buttonPlay.image = "Images/DD_Project/Buttons/Red Play.png"

    def leavePlayButton():
        buttonPlay.image = "Images/DD_Project/Buttons/White Play.png"

    def hoverLeaderBoardButton():
        buttonLeaderBoard.image = "Images/DD_Project/Buttons/Red LeaderBoard.png"

    def leaveLeaderBoardButton():
        buttonLeaderBoard.image = "Images/DD_Project/Buttons/White LeaderBoard.png"

    def hoverQuitButton():
        buttonQuit.image = "Images/DD_Project/Buttons/Red Quit.png"

    def leaveQuitButton():
        buttonQuit.image = "Images/DD_Project/Buttons/White Quit.png"

    buttonPlay.when_mouse_enters = hoverPlayButton
    buttonPlay.when_mouse_leaves = leavePlayButton
    buttonLeaderBoard.when_mouse_enters = hoverLeaderBoardButton
    buttonLeaderBoard.when_mouse_leaves = leaveLeaderBoardButton
    buttonQuit.when_mouse_enters = hoverQuitButton
    buttonQuit.when_mouse_leaves = leaveQuitButton

    #This is opened after pressed play in the menu. This is before the playing the reaction game.
    def openLoading():
        loadingWindow = Window(app, bg = "white", width= 3456, height= 2234, title="PLAY")
        loadingWindow.show(wait = True) # wait stops user from using previous window
        #app.hide() # option to hide

        #This is initiated after pressing start in the loading screen.
        def openPlay():
            playWindow = Window(app, bg = "white", width= 3456, height= 2234, title="PLAY")
            playWindow.show(wait = True) # wait stops user from using previous window
            loadingWindow.hide() # option to hide

            PlaySeparation1 = Box(playWindow, width = 300, height="fill", border = False, align="right")
            PlaySeparation1.bg = "light blue"
            PlaySeparation2 = Box(playWindow, width = 300, height="fill", border = False, align="left")
            PlaySeparation2.bg = "light blue"
            PlaySeparation3 = Box(playWindow, width = 1250, height="fill", border = False)

            InsidePlayTop = Box(PlaySeparation3, width="fill", height=300, align="top", border = False)
            InsidePlayTop.bg = "light blue"
            InsidePlayBottom = Box(PlaySeparation3, width="fill", height=250, align="bottom", border = False)

            GoButtonBox = Box(PlaySeparation3, width="fill", height=1000, align="bottom", border=False)
            GoButtonBox.bg = "light blue"

            GasPedalImage = Picture(InsidePlayBottom, image = "Images/DD_Project/Buttons/GasPedalBefore.png", align = "top")
            LightImageStable = Picture(InsidePlayTop, image = "Images/DD_Project/Lights/LightGo.png")
            F1POVImage = Picture (GoButtonBox, image = "Images/DD_Project/F1POV.gif", align="bottom")

            backImage = Picture(PlaySeparation1, align="top", image = "Images/DD_Project/Buttons/White Back.png")

            def hoverBackButton():
                backImage.image = "Images/DD_Project/Buttons/Red Back.png"

            def leaveBackButton():
                backImage.image = "Images/DD_Project/Buttons/White Back.png"

            def backOptions():
                app.show
                playWindow.hide()

            backImage.when_mouse_enters = hoverBackButton
            backImage.when_mouse_leaves = leaveBackButton
            backImage.when_clicked = backOptions

            def goBefore():
                GasPedalImage.image = "Images/DD_Project/Buttons/GasPedalBefore.png"

            def goAfter():
                GasPedalImage.image = "Images/DD_Project/Buttons/GasPedalAfter.png"

            def Light1():
                LightImageStable.image = "Images/DD_Project/Lights/Light1.png"

            def Light2():
                LightImageStable.image = "Images/DD_Project/Lights/Light2.png"

            def Light3():
                LightImageStable.image = "Images/DD_Project/Lights/Light3.png"

            def Light4():
                LightImageStable.image = "Images/DD_Project/Lights/Light4.png"

            def Light5():
                LightImageStable.image = "Images/DD_Project/Lights/Light5.png"

            def Light6():
                global startTime
                startTime = time.time()
                LightImageStable.image = "Images/DD_Project/Lights/Light65.gif"

            LightImageStable.after(1000, Light1)
            LightImageStable.after(2000, Light2)
            LightImageStable.after(3000, Light3)
            LightImageStable.after(4000, Light4)
            LightImageStable.after(5000, Light5)
            LightImageStable.after(random.randint(6000,12000), Light6)

            GasPedalImage.when_mouse_enters = goAfter
            GasPedalImage.when_mouse_leaves = goBefore


            def clickingImage():
                global TimeCounter
                TimeCounter = TimeCounter + 1
                endTime = time.time()
                FinalTime = endTime - startTime
                name = playWindow.question("Good Job", "What's your name?")
                UserNames.append(name)
                UserTimes.append(float(FinalTime))

                with open("Prototypes/names.pickle", "wb") as outfile:
                    pickle.dump(UserNames, outfile)
                print(UserNames)

                with open("times.pickle", "wb") as outfile:
                    pickle.dump(UserTimes, outfile)
                print(UserTimes)

            GasPedalImage.when_clicked = clickingImage

        screenSplitTopHelp = Box(loadingWindow, width="fill",height=100, align="top", border=False)
        screenSplitTop = Box(loadingWindow, width="fill", height=390, align="top", border=False)
        screenSplitBottomHelp = Box(loadingWindow, width="fill", height=100, align="bottom",border=False)
        screenSplitBottom = Box(loadingWindow, width="fill", height=200, align="bottom", border=False)

        instructionImage = Picture(screenSplitTop, image= "Images/DD_Project/LoadingInstructions.png")
        startImage = Picture(screenSplitBottom, image= "Images/DD_Project/Buttons/White Start.png")
        backImage = Picture(screenSplitTopHelp, align="right", image = "Images/DD_Project/Buttons/White Back.png")

        def hoverStartButton():
            startImage.image = "Images/DD_Project/Buttons/Red Start.png"

        def leaveStartButton():
            startImage.image = "Images/DD_Project/Buttons/White Start.png"

        def hoverBackButton():
            backImage.image = "Images/DD_Project/Buttons/Red Back.png"

        def leaveBackButton():
            backImage.image = "Images/DD_Project/Buttons/White Back.png"

        startImage.when_mouse_enters = hoverStartButton
        startImage.when_mouse_leaves = leaveStartButton

        backImage.when_mouse_enters = hoverBackButton
        backImage.when_mouse_leaves = leaveBackButton

        age = loadingWindow.question("Age", "Enter Age")
        if int(age) >=12 and int(age) <=18:
            startImage.when_clicked = openPlay
        else:
            openLoading.hide()
            app.show()
            ageRestrictionMethod = app.info("Restriction", "You have to be 12 - 18 years old to Play this Game!")

        def backDestroyer():
            loadingWindow.destroy()
            app.shown


    buttonPlay.when_clicked = openLoading

    #This is to open the leaderboard through the menu, as well as the play.
    def open_LeaderBoard():
        global FinalTime, name
        leaderWindow = Window(app, bg = "white", width= 3456, height= 2234, title="LEADERBOARD")
        leaderWindow.show(wait = True) # wait stops user from using previous window
        app.hide() # option to hide

        spacerL = Box(leaderWindow, width=400, height="fill", align="left", border=True)
        spacerR = Box(leaderWindow, width=400, height="fill", align="right", border=True)
        spacerM = Box(leaderWindow, width=700, height="fill", border=True)

        PlaySeparation1 = Box(spacerR, width = 300, height="fill", border = True, align="right")
        backImage = Picture(PlaySeparation1, align="top", image = "Images/DD_Project/Buttons/White Back.png")

        def hoverBackButton():
            backImage.image = "Images/DD_Project/Buttons/Red Back.png"

        def leaveBackButton():
            backImage.image = "Images/DD_Project/Buttons/White Back.png"

        backImage.when_mouse_enters = hoverBackButton
        backImage.when_mouse_leaves = leaveBackButton

        horizM = Box(spacerM, width="fill", height=200, border=True, align="top")
        horiz1 = Box(spacerM, width="fill", height=150, border=True, align="top")
        horiz2 = Box(spacerM, width="fill", height=150, border=True, align="tpp")
        horiz3 = Box(spacerM, width="fill", height=150, border=True, align="top")

        splitHoriz1L = Box(horiz1, width=315, height="fill", border=True, align="left")
        splitHoriz2L = Box(horiz2, width=315, height="fill", border=True, align="left")
        splitHoriz3L = Box(horiz3, width=315, height="fill", border=True, align="left")

        splitHoriz1R = Box(horiz1, width=315, height="fill", border=True, align="right")
        splitHoriz2R = Box(horiz2, width=315, height="fill", border=True, align="right")
        splitHoriz3R = Box(horiz3, width=315, height="fill", border=True, align="right")

        UserTimes.sort()
        userAverage = mean(UserTimes)

        ScoreTop = Text(splitHoriz1R, text= UserTimes[0])
        ScoreAverage = Text(splitHoriz2R, text = userAverage)
        ScoreMax = Text(splitHoriz3R, text = UserTimes[-1])

        BestImage = Picture(splitHoriz1L, image="Images/DD_Project/best.png")
        AvrImage = Picture(splitHoriz2L, image="Images/DD_Project/Average.png")
        SlowImage = Picture(splitHoriz3L, image="Images/DD_Project/slowest.png")
        logo = Picture(horizM, image="Images/DD_Project/logo.png")


        UserNames.sort()

        def backDestroyer():
            leaderWindow.destroy()
            app.shown

        backImage.when_clicked = backDestroyer


    buttonLeaderBoard.when_clicked = open_LeaderBoard

    def open_Quit():
        quit()
        app.hide() # option to hide

    buttonQuit.when_clicked = open_Quit

menu()
app.display()
