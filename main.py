import tkinter as tk
import tkinter.colorchooser

# paint program cus why not, really thought this would be more time consuming rofl

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ppython")

        # creates the canvas
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack()

        # creates the brush, will add a brush size adjuster possibly?
        self.color = "black"
        self.brush_size = 2
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # this just adds the buttons and binds the buttons to keys
        self.clear_button = tk.Button(self.button_frame, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT)
        self.color_button = tk.Button(self.button_frame, text="Change Color", command=self.change_color)
        self.color_button.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.drawing = False
        self.last_x = 0
        self.last_y = 0

    # basically starts the program
    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    # self explanatory lol
    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_line((self.last_x, self.last_y, x, y), fill=self.color, width=self.brush_size)
            self.last_x = x
            self.last_y = y

    def clear_canvas(self):
        self.canvas.delete("all")

    def change_color(self):
        new_color = tk.colorchooser.askcolor()[1]
        if new_color:
            self.color = new_color


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()