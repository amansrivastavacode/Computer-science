import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")

        # Variable to store current expression
        self.expression = ""
        self.input_text = tk.StringVar()

        # Input Screen
        input_frame = self.create_input_screen()
        input_frame.pack(side=tk.TOP)

        # Buttons
        btns_frame = self.create_buttons()
        btns_frame.pack()

    def create_input_screen(self):
        # Create a frame for the input field
        frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        frame.pack(side=tk.TOP)

        # Create the input field (Entry widget)
        input_field = tk.Entry(frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=13) # 'ipady' is internal padding to increase height
        return frame

    def create_buttons(self):
        # Create a frame for buttons
        btns_frame = tk.Frame(self.root, width=312, height=322.5, bg="grey")
        
        # Button layout configuration
        # Row 1
        self.create_button(btns_frame, "C", 1, 0, 3, lambda: self.btn_clear())
        self.create_button(btns_frame, "/", 1, 3, 1, lambda: self.btn_click("/"))
        
        # Row 2
        self.create_button(btns_frame, "7", 2, 0, 1, lambda: self.btn_click(7))
        self.create_button(btns_frame, "8", 2, 1, 1, lambda: self.btn_click(8))
        self.create_button(btns_frame, "9", 2, 2, 1, lambda: self.btn_click(9))
        self.create_button(btns_frame, "*", 2, 3, 1, lambda: self.btn_click("*"))
        
        # Row 3
        self.create_button(btns_frame, "4", 3, 0, 1, lambda: self.btn_click(4))
        self.create_button(btns_frame, "5", 3, 1, 1, lambda: self.btn_click(5))
        self.create_button(btns_frame, "6", 3, 2, 1, lambda: self.btn_click(6))
        self.create_button(btns_frame, "-", 3, 3, 1, lambda: self.btn_click("-"))
        
        # Row 4
        self.create_button(btns_frame, "1", 4, 0, 1, lambda: self.btn_click(1))
        self.create_button(btns_frame, "2", 4, 1, 1, lambda: self.btn_click(2))
        self.create_button(btns_frame, "3", 4, 2, 1, lambda: self.btn_click(3))
        self.create_button(btns_frame, "+", 4, 3, 1, lambda: self.btn_click("+"))
        
        # Row 5
        self.create_button(btns_frame, "0", 5, 0, 2, lambda: self.btn_click(0))
        self.create_button(btns_frame, ".", 5, 2, 1, lambda: self.btn_click("."))
        self.create_button(btns_frame, "=", 5, 3, 1, lambda: self.btn_equal())

        return btns_frame

    def create_button(self, frame, text, row, col, colspan, command):
        # Helper to create standardized buttons
        tk.Button(frame, text=text, fg="black", width=10 * colspan, height=3, bd=0, bg="#fff", cursor="hand2", command=command).grid(row=row, column=col, padx=1, pady=1, columnspan=colspan, sticky="nsew")

    def btn_click(self, item):
        # Update expression when a button is clicked
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def btn_clear(self):
        # Clear the input field
        self.expression = ""
        self.input_text.set("")

    def btn_equal(self):
        # Calculate result
        try:
            result = str(eval(self.expression)) # 'eval' parses the string expression
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            self.input_text.set("Error")
            self.expression = ""
        except SyntaxError:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    app = CalculatorApp(root)
    # Run the application
    root.mainloop()
