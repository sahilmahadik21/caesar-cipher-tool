import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cipher_logic import caesar_cipher, brute_force_decrypt
from themes import apply_dark_mode, apply_light_mode

def build_gui():
    root = tk.Tk()
    root.title("Advanced Caesar Cipher Tool")
    root.geometry("700x600")

    # Widgets
    ttk.Label(root, text="Input Text").pack()
    input_text = tk.Text(root, height=5, width=80)
    input_text.pack()

    ttk.Button(root, text="Load from File", command=lambda: load_from_file(input_text)).pack()

    ttk.Label(root, text="Shift (0–25)").pack()
    shift_var = tk.StringVar(value="3")
    shift_combo = ttk.Combobox(root, textvariable=shift_var, values=[str(i) for i in range(26)])
    shift_combo.pack()

    ttk.Label(root, text="Mode").pack()
    mode_var = tk.StringVar(value="encrypt")
    mode_combo = ttk.Combobox(root, textvariable=mode_var, values=["encrypt", "decrypt"])
    mode_combo.pack()

    ttk.Label(root, text="Output Text").pack()
    output_text = tk.Text(root, height=5, width=80)
    output_text.pack()

    def process():
        try:
            text = input_text.get("1.0", tk.END).strip()
            shift = int(shift_var.get())
            mode = mode_var.get()
            output = caesar_cipher(text, shift, mode)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, output)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def brute_force():
        text = input_text.get("1.0", tk.END).strip()
        result = brute_force_decrypt(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    def live_preview(event=None):
        if auto_var.get():
            process()

    def toggle_theme():
        if theme_var.get() == "Dark":
            apply_dark_mode(root)
        else:
            apply_light_mode(root)

    auto_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Auto Encrypt/Decrypt", variable=auto_var, command=process).pack()

    # Buttons
    ttk.Button(root, text="Process", command=process).pack(pady=5)
    ttk.Button(root, text="Brute Force Decrypt", command=brute_force).pack(pady=5)
    ttk.Button(root, text="Save Output", command=lambda: save_to_file(output_text.get("1.0", tk.END))).pack(pady=5)

    # Theme toggle
    theme_var = tk.StringVar(value="Light")
    ttk.Label(root, text="Theme").pack()
    ttk.Combobox(root, textvariable=theme_var, values=["Light", "Dark"], state="readonly").pack()
    ttk.Button(root, text="Apply Theme", command=toggle_theme).pack(pady=5)

    # Live update
    input_text.bind("<KeyRelease>", live_preview)

    root.mainloop()

# Helper functions
def save_to_file(content):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(content)

def load_from_file(text_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, file.read())
