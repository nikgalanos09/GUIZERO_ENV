from guizero import App, Window, PushButton

def open_window():
    window = Window(app, title = "Second Window")
    window.show(wait = True) # wait stops user from using previous window
    #app.hide() # option to hide

app = App(title = "Main Window")
open_button = PushButton(app, text="Open", command = open_window)
app.display()
