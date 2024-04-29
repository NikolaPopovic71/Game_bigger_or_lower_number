import tkinter as tk
from random import randint


class Game:
    def __init__(self, root):
        self.root = root
        self.sn = 5
        self.c = 0

    def bigger(self, l1, l2):
        n = randint(1, 10)
        while n == self.sn:
            n = randint(1, 10)

        if n > self.sn:
            l1.configure(text=n)
            self.sn = n
            self.c += 1
        else:
            l2.configure(text="The number is lower")
            l1.configure(text=n)
            self.window_end(l1, l2)

    def lower(self, l1, l2):
        n = randint(1, 10)
        while n == self.sn:
            n = randint(1, 10)

        if n < self.sn:
            l1.configure(text=n)
            self.sn = n
            self.c += 1
        else:
            l2.configure(text="The number is bigger")
            l1.configure(text=n)
            self.window_end(l1, l2)

    def reset(self, l1, l2):
        l1.configure(text="5")
        l2.configure(text="")
        self.sn = 5
        self.c = 0

    def window_end(self, l1, l2):
        t = tk.Toplevel(self.root)
        t.title("Reset or Exit game")
        # Get the position of the main window
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        main_width = self.root.winfo_width()
        main_height = self.root.winfo_height()

        # Calculate new position for Toplevel
        toplevel_x = main_x + main_width + 10  # 10 pixels to the right of the main window
        toplevel_y = main_y + (main_height - 200) // 2  # Vertically centered

        # Set the geometry of the Toplevel window
        t.geometry(f"250x200+{toplevel_x}+{toplevel_y}")

        if self.c == 0:
            l_t = tk.Label(t, text="Ups! You had {} hits!\nYou seem to be a great lover!\nWould you like to play a new game?".format(self.c))
        else:
            l_t = tk.Label(t, text="Congratulations!\nYou had {} hits!\nWould you like to play a new game?".format(self.c))
        l_t.pack(pady=(25, 30))

        reset_and_frame = tk.Frame(t)
        reset_and_frame.pack(pady=(0, 10))
        
        button_reset = tk.Button(reset_and_frame, text="Reset", command=lambda: [self.reset(l1, l2), t.destroy()])
        button_reset.grid(row=0, column=0, padx=10)
        button_exit = tk.Button(reset_and_frame, text="Exit", command=self.root.destroy)
        button_exit.grid(row=0, column=1, padx=20)

root = tk.Tk()
root.title("Game 'Bigger or lower'")
root.geometry("250x200")
game = Game(root)

l1 = tk.Label(root, text='5')
l1.grid(row=1, column=0, pady=(0, 10))

l2 = tk.Label(root, text="")
l2.grid(row=3, column=0, pady=(10, 10))

button_bigger = tk.Button(root, text='Bigger', command=lambda: game.bigger(l1, l2))
button_bigger.grid(row=0, column=0, pady=(20, 20))

button_lower = tk.Button(root, text='Lower', command=lambda: game.lower(l1, l2))
button_lower.grid(row=2, column=0, pady=(0, 10))

root.grid_columnconfigure(0, weight=1)


root.mainloop()
