import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser, grid):
    """Erase objects in contact with the eraser"""
    eraser_coords = canvas.coords(eraser)
    overlapping_objects = canvas.find_overlapping(*eraser_coords)
    
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    root.title("Eraser Demo")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    grid = []

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline="black")
            grid.append(cell)

    def on_mouse_move(event):
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser, grid)

    root.bind("<Motion>", on_mouse_move)

    
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

    root.mainloop()

if __name__ == '__main__':
    main()


            
    