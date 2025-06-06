import tkinter as tk
from tkinter import ttk
from password_generator import generate_password

class PasswordGeneratorApp:
    def __init__(self, root):
        """
        Initialize the GUI application and set up all widgets and variables.
        """
        self.root = root
        self.root.title("Strong Random Password Generator")
        # Bring window to front on launch for better UX
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after(500, lambda: self.root.lift())
        self.root.after(1000, lambda: self.root.attributes('-topmost', False))

        # Tkinter variables for user options and state
        self.length_var = tk.StringVar(value="16")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.StringVar(value="!#$%&*+-?@',./:;=^_~`|<>[](){}")
        self.no_similar_var = tk.BooleanVar()
        self.no_duplicate_var = tk.BooleanVar()
        self.add_word_var = tk.BooleanVar()
        self.word_var = tk.StringVar()
        self.begins_with_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Layout configuration for all widgets
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w")
        ttk.Entry(root, textvariable=self.length_var, width=5).grid(row=0, column=1, sticky="w")

        ttk.Checkbutton(root, text="Include uppercase (A-Z)", variable=self.upper_var).grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(root, text="Include lowercase (a-z)", variable=self.lower_var).grid(row=2, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(root, text="Include digits (0-9)", variable=self.digit_var).grid(row=3, column=0, columnspan=2, sticky="w")

        # Symbols row with entry field for custom symbols
        symbol_frame = ttk.Frame(root)
        symbol_frame.grid(row=4, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(symbol_frame, text="Include symbols", variable=self.symbol_var).grid(row=0, column=0, sticky="w")
        self.symbols_entry = ttk.Entry(symbol_frame, textvariable=self.symbols_var, width=30)
        self.symbols_entry.grid(row=0, column=1, padx=5)

        ttk.Checkbutton(root, text="Exclude similar characters (il1Lo0O)", variable=self.no_similar_var).grid(row=5, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(root, text="Exclude duplicate characters", variable=self.no_duplicate_var).grid(row=6, column=0, columnspan=2, sticky="w")

        # Option to add a custom word to the password
        ttk.Checkbutton(root, text="Add a word", variable=self.add_word_var).grid(row=7, column=0, sticky="w")
        ttk.Entry(root, textvariable=self.word_var, width=20).grid(row=7, column=1)

        # Option to specify a prefix for the password
        ttk.Label(root, text="Begins with:").grid(row=8, column=0, sticky="w")
        ttk.Entry(root, textvariable=self.begins_with_var, width=5).grid(row=8, column=1, sticky="w")

        # Generate password button and result display
        ttk.Button(root, text="Generate Password", command=self.generate_password).grid(row=9, column=0, columnspan=2, pady=10)
        ttk.Entry(root, textvariable=self.result_var, width=40).grid(row=10, column=0, columnspan=2)

        # Copy to clipboard button and notification label
        copy_frame = ttk.Frame(root)
        copy_frame.grid(row=11, column=0, columnspan=2)
        ttk.Button(copy_frame, text="Copy to clipboard", command=self.copy_to_clipboard).grid(row=0, column=0)
        self.copy_label = ttk.Label(copy_frame, text="", foreground="green")
        self.copy_label.grid(row=0, column=1, padx=10)

    def generate_password(self):
        """
        Collect user options from the UI, generate a password, and display it.
        """
        try:
            length = int(self.length_var.get())
        except ValueError:
            self.result_var.set("Invalid length")
            return

        try:
            # Delegate password generation to the core logic module
            password = generate_password(
                length=length,
                use_upper=self.upper_var.get(),
                use_lower=self.lower_var.get(),
                use_digits=self.digit_var.get(),
                use_symbols=self.symbol_var.get(),
                symbols=self.symbols_entry.get(),
                no_similar=self.no_similar_var.get(),
                no_duplicate=self.no_duplicate_var.get(),
                add_word=self.word_var.get() if self.add_word_var.get() else None,
                begins_with=self.begins_with_var.get() or None
            )
            self.result_var.set(password)
        except Exception as e:
            # Show error message in the result field
            self.result_var.set(str(e))

    def copy_to_clipboard(self):
        """
        Copy the generated password to the system clipboard and show a notification.
        """
        password = self.result_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            self.copy_label.config(text="✅ Copied!")
            self.root.after(2000, lambda: self.copy_label.config(text=""))

def main():
    """
    Entry point for the Tkinter GUI application.
    """
    root = tk.Tk()
    PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
