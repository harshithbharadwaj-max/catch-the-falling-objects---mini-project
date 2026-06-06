import tkinter as tk
import random

WIDTH = 500
HEIGHT = 600

root = tk.Tk()
root.title("Catch The Falling Objects")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lightblue")
canvas.pack()

basket = canvas.create_rectangle(200, 550, 300, 580, fill="brown")

score = 0
score_text = canvas.create_text(70, 20, text="Score: 0", font=("Arial", 14))

falling = canvas.create_oval(240, 0, 270, 30, fill="red")

def move_left(event):
    canvas.move(basket, -20, 0)

def move_right(event):
    canvas.move(basket, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

def update():
    global score, falling

    canvas.move(falling, 0, 5)

    obj_pos = canvas.coords(falling)
    basket_pos = canvas.coords(basket)

    if obj_pos[3] >= basket_pos[1]:
        if basket_pos[0] <= obj_pos[0] <= basket_pos[2]:
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

            canvas.delete(falling)
            x = random.randint(50, 450)
            falling = canvas.create_oval(x, 0, x+30, 30, fill="red")

    if obj_pos[3] > HEIGHT:
        canvas.create_text(
            WIDTH//2,
            HEIGHT//2,
            text="GAME OVER",
            font=("Arial", 24),
            fill="red"
        )
        return

    root.after(30, update)

update()
root.mainloop()