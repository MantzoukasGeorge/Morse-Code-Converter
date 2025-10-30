# src/morse/gui.py
"""
Tkinter GUI for the Morse Code Converter.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from encoder import encode
from decoder import decode


class MorseApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("720x560")
        self.root.minsize(600, 500)
        self.root.configure(bg="#f0f0f0")

        # Style
        style = ttk.Style()
        style.theme_use("clam")  # modern look
        style.configure("TButton", padding=6, font=("Helvetica", 10, "bold"))
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))

        self.create_widgets()

    def create_widgets(self):
        # === Header ===
        header = ttk.Label(
            self.root,
            text="Morse Code Converter",
            style="Header.TLabel"
        )
        header.pack(pady=(15, 5))

        # === Input Frame ===
        input_frame = ttk.LabelFrame(self.root, text=" Input (Text or Morse) ", padding=10)
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=8,
            font=("Courier", 12),
            wrap=tk.WORD,
            relief="sunken",
            bd=2
        )
        self.input_text.pack(fill="both", expand=True)

        # === Button Frame ===
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=12)

        self.encode_btn = ttk.Button(
            btn_frame,
            text="Text → Morse",
            command=self.on_encode
        )
        self.encode_btn.pack(side="left", padx=8)

        self.decode_btn = ttk.Button(
            btn_frame,
            text="Morse → Text",
            command=self.on_decode
        )
        self.decode_btn.pack(side="left", padx=8)

        self.clear_btn = ttk.Button(
            btn_frame,
            text="Clear All",
            command=self.clear_all
        )
        self.clear_btn.pack(side="left", padx=8)

        # === Output Frame ===
        output_frame = ttk.LabelFrame(self.root, text=" Output ", padding=10)
        output_frame.pack(fill="both", expand=True, padx=20, pady=(5, 15))

        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=8,
            font=("Courier", 12),
            wrap=tk.WORD,
            bg="#fffde7",
            relief="sunken",
            bd=2,
            state="disabled"
        )
        self.output_text.pack(fill="both", expand=True)

        # === Footer ===
        footer = ttk.Label(
            self.root,
            text="• Use '/' or triple space for word separation in Morse • Copy with Ctrl+C",
            font=("Helvetica", 9),
            foreground="gray"
        )
        footer.pack(pady=(0, 10))

    def on_encode(self):
        text = self.input_text.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Input", "Please enter text to encode.")
            return
        try:
            result = encode(text)
            self.show_result(result)
        except Exception as e:
            messagebox.showerror("Encoding Error", str(e))

    def on_decode(self):
        morse = self.input_text.get(1.0, tk.END).strip()
        if not morse:
            messagebox.showwarning("Empty Input", "Please enter Morse code to decode.")
            return
        try:
            result = decode(morse)
            self.show_result(result)
        except Exception as e:
            messagebox.showerror("Decoding Error", str(e))

    def show_result(self, result: str):
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, result)
        self.output_text.config(state="disabled")

    def clear_all(self):
        self.input_text.delete(1.0, tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state="disabled")


def create_gui():
    root = tk.Tk()
    app = MorseApp(root)
    root.mainloop()


if __name__ == "__main__":
    create_gui()