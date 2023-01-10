from guizero import App, PushButton, Text

app = App(title="Reaction Time", width = 900, height = 400, bg="white")
number = 0

def do_nothing():
    global number
    print ("Button Pressed!")
    app.bg = "green"
    number += 1
    Text.value = number

Text = Text(app, text = number, size = 20, align = "bottom")


button = PushButton(app, command=do_nothing)
app.display()
