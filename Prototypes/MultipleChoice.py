from guizero import App, Combo
app = App()

combo = Combo(app, options=["Beef", "Chicken", "Fish", "Vegetarian"])

app.display()
