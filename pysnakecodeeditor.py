import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

class PySnakeIDLE:
    def __init__(self, root):
        self.root = root
        self.root.title("PySnake IDLE")
        self.filepath = None

        # Create a text area for the code editor
        self.text_area = tk.Text(self.root, wrap="word", font=("Consolas", 12), undo=True)
        self.text_area.pack(fill="both", expand=True)

        # Bind events for syntax highlighting and indentation
        self.text_area.bind("<KeyRelease>", self.highlight_syntax)
        self.text_area.bind("<Tab>", self.insert_tab)
        self.text_area.bind("<Return>", self.auto_indent)

        # Create a text area for the console output
        self.console_output = tk.Text(self.root, height=10, font=("Consolas", 10), bg="black", fg="white", state=tk.DISABLED)
        self.console_output.pack(fill="x")

        # Create the Run button
        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(side="bottom")

        # Set up a menu bar
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_program)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        self.root.protocol("WM_DELETE_WINDOW", self.exit_program)

    def new_file(self):
        self.filepath = None
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        self.filepath = filedialog.askopenfilename(defaultextension=".pysn", filetypes=[("PySnake Files", "*.pysn")])
        if self.filepath:
            with open(self.filepath, 'r') as file:
                code = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, code)

    def save_file(self):
        if self.filepath:
            with open(self.filepath, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filepath = filedialog.asksaveasfilename(defaultextension=".pysn", filetypes=[("PySnake Files", "*.pysn")])
        if self.filepath:
            with open(self.filepath, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def run_code(self):
        if not self.filepath:
            messagebox.showwarning("Save your file", "Please save your file before running.")
            return
        
        self.save_file()
        
        compiled_output = "compiled_output.pyc"
        process = subprocess.run(['python', 'pysncompile', self.filepath, '-t', compiled_output],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete(1.0, tk.END)
        self.console_output.insert(tk.END, process.stdout + process.stderr)
        self.console_output.config(state=tk.DISABLED)

    def clear_output(self):
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete(1.0, tk.END)
        self.console_output.config(state=tk.DISABLED)

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    # Syntax highlighting
    def highlight_syntax(self, event=None):
        self.text_area.tag_remove("keyword", "1.0", tk.END)
        keywords = ["enjoy", "main", "print", "True", "False"]
        for keyword in keywords:
            start_idx = "1.0"
            while True:
                start_idx = self.text_area.search(keyword, start_idx, stopindex=tk.END)
                if not start_idx:
                    break
                end_idx = f"{start_idx}+{len(keyword)}c"
                self.text_area.tag_add("keyword", start_idx, end_idx)
                start_idx = end_idx
        self.text_area.tag_config("keyword", foreground="blue")

    # Insert tab character
    def insert_tab(self, event):
        self.text_area.insert(tk.INSERT, "    ")  # 4 spaces for indentation
        return "break"  # Prevent default tab behavior

    # Auto-indent on new line
    def auto_indent(self, event):
        current_line = self.text_area.index("insert").split('.')[0]
        previous_line = str(int(current_line) - 1)
        previous_line_content = self.text_area.get(f"{previous_line}.0", f"{previous_line}.end")

        if previous_line_content.strip():  # Check if the previous line is not empty
            indent = len(previous_line_content) - len(previous_line_content.lstrip())
            self.text_area.insert(tk.INSERT, "\n" + " " * indent)
        else:
            self.text_area.insert(tk.INSERT, "\n")
        return "break"  # Prevent default newline behavior

if __name__ == "__main__":
    root = tk.Tk()
    app = PySnakeIDLE(root)
    root.mainloop()
