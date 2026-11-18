import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")

def new_file(window, text_edit):
    text_edit.delete(1.0, tk.END)
    window.title("Untitled")

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=300)
    window.columnconfigure(1, minsize=400)

    text_edit = tk.Text(window, font="Arial 12")
    text_edit.grid(row=0, column=1)

    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10, 'bold'), foreground='navy')

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    new_button = ttk.Button(frame, text="New", style='TButton', command=lambda: new_file(window, text_edit))
    save_button = ttk.Button(frame, text="Save As", command=lambda: save_file(window, text_edit))
    open_button = ttk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    new_button.grid(row=0, column=0, padx=5, pady=2, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    save_button.grid(row=2, column=0, padx=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-n>", lambda x: new_file(window, text_edit))
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()
