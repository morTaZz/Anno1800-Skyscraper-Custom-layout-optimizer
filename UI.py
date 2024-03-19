import tkinter as tk

class GridUI:
    def __init__(self, master,on_submit):
        self.master = master
        self.grid_size = 20
        self.cell_size = 20
        self.numbered_cells = {}  # Tracks the numbered cell with its unique number
        self.associated_cells = {}  # Tracks the surrounding cells associated with a numbered cell
        self.next_number = 1
        self.setup_ui()
        self.on_submit = on_submit

    def setup_ui(self):
        self.canvas = tk.Canvas(self.master, width=self.grid_size*self.cell_size, height=self.grid_size*self.cell_size)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

        self.erase_mode_button = tk.Button(self.master, text="Eraser", command=lambda: self.set_mode("erase"))
        self.erase_mode_button.pack(side=tk.BOTTOM, pady=10)

        self.number_mode_button = tk.Button(self.master, text="Number Mode", command=lambda: self.set_mode("number"))
        self.number_mode_button.pack(side=tk.BOTTOM, pady=10)

        self.mode = "number"  # Default mode
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_click)

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                color = "lightblue" if (i, j) in self.associated_cells else "white"
                self.canvas.create_rectangle(i*self.cell_size, j*self.cell_size, (i+1)*self.cell_size, (j+1)*self.cell_size, fill=color, outline="black")
        for (x, y), number in self.numbered_cells.items():
            self.canvas.create_text(x*self.cell_size + self.cell_size/2, y*self.cell_size + self.cell_size/2, text=str(number), font=("Arial", 9))

    def set_mode(self, mode):
        self.mode = mode

    def handle_click(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.mode == "number":
            self.mark_number_and_associates(x, y)
        elif self.mode == "erase":
            self.erase_cell_and_associates(x, y)
        self.draw_grid()

    def mark_number_and_associates(self, x, y):
        if (x, y) not in self.numbered_cells and (x, y) not in self.associated_cells:
            self.numbered_cells[(x, y)] = self.next_number
            for i in range(max(0, x-1), min(self.grid_size, x+2)):
                for j in range(max(0, y-1), min(self.grid_size, y+2)):
                    if (i, j) != (x, y):
                        self.associated_cells[(i, j)] = self.next_number
            self.next_number += 1

    def erase_cell_and_associates(self, x, y):
        if (x, y) in self.numbered_cells:
            number = self.numbered_cells.pop((x, y))
            cells_to_erase = [cell for cell, num in self.associated_cells.items() if num == number]
            for cell in cells_to_erase:
                del self.associated_cells[cell]
        elif (x, y) in self.associated_cells:
            number = self.associated_cells.pop((x, y))
            cell_to_erase = [cell for cell, num in self.numbered_cells.items() if num == number]
            for cell in cell_to_erase:
                del self.numbered_cells[cell]
            cells_to_erase = [cell for cell, num in self.associated_cells.items() if num == number]
            for cell in cells_to_erase:
                del self.associated_cells[cell]

    def submit(self):
        # Instead of printing and destroying the master, call the callback with the results
        if self.on_submit:  # Check if the callback function is provided
            self.on_submit(list(self.numbered_cells.keys()))
        self.master.destroy()

def main():
    root = tk.Tk()
    root.title("Grid UI")
    app = GridUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
