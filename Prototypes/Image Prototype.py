from guizero import App, Box, Picture

app = App(bg = "white", width= 3456, height= 2234, title="Menu")

topSpacer = Box(app, height=300, width="fill", align="top", border=True, layout="grid")
titleBox = Box(topSpacer, height=300, width=1225, border=True, grid=[0,0])
titleImage = Picture(titleBox, image="Images/f1.gif")

app.display()
