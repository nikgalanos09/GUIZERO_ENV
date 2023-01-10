from guizero import App, Text

app = App(title="Reaction Time", width = 900, height = 400, bg="white")

# Methods
title = Text(app, text="Welcome to the reaction test!", size = 30, align = "top", font = "Helvetica")

# Adding text to different parts of the Interface
bottomText = Text(app, text="End of Page", size = 20, align = "bottom")
rightText = Text(app, text="Right Side Text", size = 20, align = "right")
leftText = Text(app, text="Left Side Text", size = 20, align = "left")

# Properties
title.size = 40

app.display()
