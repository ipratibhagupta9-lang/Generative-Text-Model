# ============================================================
# CODTECH Internship Task-4
# Generative Text Model using Groq API
# Part - 1
# ============================================================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from groq import Groq
import threading

# ============================================================
# GROQ API
# ============================================================

GROQ_API_KEY = "enter_groq_key"

client = Groq(
    api_key=GROQ_API_KEY
)

# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Generative Text Model - Groq AI")
root.geometry("1000x760")
root.minsize(900,650)

dark_mode = False

# ============================================================
# COLORS
# ============================================================

LIGHT_BG = "#F5F7FA"
LIGHT_FRAME = "#FFFFFF"
LIGHT_TEXT = "#222222"

DARK_BG = "#202124"
DARK_FRAME = "#2D2E30"
DARK_TEXT = "#FFFFFF"

BUTTON_GREEN = "#2E7D32"
BUTTON_BLUE = "#1565C0"
BUTTON_RED = "#C62828"
BUTTON_ORANGE = "#EF6C00"

root.configure(bg=LIGHT_BG)

# ============================================================
# VARIABLES
# ============================================================

status_var = tk.StringVar()
status_var.set("Ready")

word_var = tk.StringVar()
word_var.set("Words : 0")

char_var = tk.StringVar()
char_var.set("Characters : 0")

# ============================================================
# FUNCTIONS
# ============================================================

def update_count():

    text = output_text.get("1.0", tk.END)

    word_var.set(
        f"Words : {len(text.split())}"
    )

    char_var.set(
        f"Characters : {len(text.strip())}"
    )


def clear_text():

    prompt_text.delete("1.0", tk.END)

    output_text.delete("1.0", tk.END)

    update_count()

    status_var.set("Ready")


def copy_text():

    text = output_text.get("1.0", tk.END)

    if text.strip() == "":
        return

    root.clipboard_clear()

    root.clipboard_append(text)

    messagebox.showinfo(
        "Copied",
        "Generated text copied successfully."
    )


def save_text():

    text = output_text.get("1.0", tk.END)

    if text.strip() == "":

        messagebox.showwarning(
            "Warning",
            "Nothing to save."
        )

        return

    file = filedialog.asksaveasfilename(

        defaultextension=".txt",

        filetypes=[
            ("Text File","*.txt")
        ]

    )

    if file:

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

        messagebox.showinfo(
            "Saved",
            "Text saved successfully."
        )


def toggle_theme():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:

        bg = DARK_BG
        frame = DARK_FRAME
        fg = DARK_TEXT

        theme_btn.config(
            text="Light Mode"
        )

    else:

        bg = LIGHT_BG
        frame = LIGHT_FRAME
        fg = LIGHT_TEXT

        theme_btn.config(
            text="Dark Mode"
        )

    root.configure(bg=bg)

    main_frame.config(bg=bg)

    control_frame.config(bg=bg)

    button_frame.config(bg=bg)

    stats_frame.config(bg=bg)

    prompt_label.config(
        bg=bg,
        fg=fg
    )

    output_label.config(
        bg=bg,
        fg=fg
    )

    prompt_text.config(
        bg=frame,
        fg=fg,
        insertbackground=fg
    )

    output_text.config(
        bg=frame,
        fg=fg,
        insertbackground=fg
    )

    word_label.config(
        bg=bg,
        fg=fg
    )

    char_label.config(
        bg=bg,
        fg=fg
    )

    status_label.config(
        bg=frame,
        fg=fg
    )

# ============================================================
# GENERATE FUNCTION
# (Part-2)
# ============================================================

def generate_text():
    pass

# ============================================================
# TITLE
# ============================================================

title = tk.Label(

    root,

    text="Generative Text Model using Groq AI",

    font=("Arial",22,"bold"),

    bg=LIGHT_BG,

    fg="#0D47A1"

)

title.pack(
    pady=10
)

main_frame = tk.Frame(
    root,
    bg=LIGHT_BG
)

main_frame.pack(
    fill="both",
    expand=True,
    padx=20
)

prompt_label = tk.Label(

    main_frame,

    text="Enter Prompt",

    font=("Arial",13,"bold"),

    bg=LIGHT_BG

)

prompt_label.pack(
    anchor="w"
)

prompt_text = tk.Text(

    main_frame,

    height=7,

    font=("Arial",11),

    wrap="word"

)

prompt_text.pack(
    fill="x",
    pady=8
)

# ============================================================
# CONTROLS
# ============================================================

control_frame = tk.Frame(
    main_frame,
    bg=LIGHT_BG
)

control_frame.pack(
    fill="x",
    pady=10
)

tk.Label(

    control_frame,

    text="Max Tokens",

    bg=LIGHT_BG,

    font=("Arial",10,"bold")

).grid(
    row=0,
    column=0,
    padx=5
)

length_slider = tk.Scale(

    control_frame,

    from_=100,

    to=600,

    orient="horizontal",

    length=180

)

length_slider.set(250)

length_slider.grid(
    row=0,
    column=1
)

tk.Label(

    control_frame,

    text="Temperature",

    bg=LIGHT_BG,

    font=("Arial",10,"bold")

).grid(
    row=0,
    column=2,
    padx=5
)

temp_slider = tk.Scale(

    control_frame,

    from_=0.0,

    to=1.5,

    resolution=0.1,

    orient="horizontal",

    length=180

)

temp_slider.set(0.7)

temp_slider.grid(
    row=0,
    column=3
)

button_frame = tk.Frame(
    main_frame,
    bg=LIGHT_BG
)

button_frame.pack(
    pady=10
)
# ============================================================
# GENERATE FUNCTION
# ============================================================

def generate_text():

    prompt = prompt_text.get("1.0", tk.END).strip()

    if prompt == "":

        messagebox.showwarning(
            "Warning",
            "Please enter a prompt."
        )

        return

    generate_btn.config(
        state="disabled"
    )

    progress.start(10)

    status_var.set(
        "Generating..."
    )

    output_text.delete(
        "1.0",
        tk.END
    )

    def run():

        try:

            response = client.chat.completions.create(

                model="llama-3.1-8b-instant",

                messages=[

                    {
                        "role": "system",

                        "content":
                        """
You are a professional AI content writer.

Write a detailed, well-structured article.

Rules:

1. Give a proper title.

2. Write an introduction.

3. Write 3 informative paragraphs.

4. Use simple professional English.

5. Avoid repetition.

6. End with a conclusion.

7. Generate around 250-300 words.
                        """
                    },

                    {
                        "role": "user",
                        "content": prompt
                    }

                ],

                temperature=float(
                    temp_slider.get()
                ),

                max_completion_tokens=int(
                    length_slider.get()
                )

            )

            generated = response.choices[0].message.content

            def update_gui():

                output_text.insert(
                    tk.END,
                    generated
                )

                update_count()

                progress.stop()

                generate_btn.config(
                    state="normal"
                )

                status_var.set(
                    "Generation Completed"
                )

            root.after(
                0,
                update_gui
            )

        except Exception as e:

            def show_error():

                progress.stop()

                generate_btn.config(
                    state="normal"
                )

                status_var.set(
                    "Error"
                )

                messagebox.showerror(
                    "Groq Error",
                    str(e)
                )

            root.after(
                0,
                show_error
            )

    threading.Thread(
        target=run,
        daemon=True
    ).start()


# ============================================================
# BUTTONS
# ============================================================

generate_btn = tk.Button(

    button_frame,

    text="Generate",

    width=14,

    font=("Arial",11,"bold"),

    bg=BUTTON_GREEN,

    fg="white",

    command=generate_text

)

generate_btn.grid(
    row=0,
    column=0,
    padx=6
)

copy_btn = tk.Button(

    button_frame,

    text="Copy",

    width=12,

    font=("Arial",11,"bold"),

    bg=BUTTON_BLUE,

    fg="white",

    command=copy_text

)

copy_btn.grid(
    row=0,
    column=1,
    padx=6
)

save_btn = tk.Button(

    button_frame,

    text="Save",

    width=12,

    font=("Arial",11,"bold"),

    bg=BUTTON_ORANGE,

    fg="white",

    command=save_text

)

save_btn.grid(
    row=0,
    column=2,
    padx=6
)

clear_btn = tk.Button(

    button_frame,

    text="Clear",

    width=12,

    font=("Arial",11,"bold"),

    bg=BUTTON_RED,

    fg="white",

    command=clear_text

)

clear_btn.grid(
    row=0,
    column=3,
    padx=6
)

theme_btn = tk.Button(

    button_frame,

    text="Dark Mode",

    width=12,

    font=("Arial",11,"bold"),

    bg="#616161",

    fg="white",

    command=toggle_theme

)

theme_btn.grid(
    row=0,
    column=4,
    padx=6
)

# ============================================================
# PROGRESS BAR
# ============================================================

progress = ttk.Progressbar(

    main_frame,

    orient="horizontal",

    mode="indeterminate",

    length=900

)

progress.pack(

    fill="x",

    pady=10

)
# ============================================================
# OUTPUT LABEL
# ============================================================

output_label = tk.Label(

    main_frame,

    text="Generated Text",

    font=("Arial",13,"bold"),

    bg=LIGHT_BG

)

output_label.pack(

    anchor="w",

    pady=(10,5)

)

# ============================================================
# OUTPUT TEXT BOX
# ============================================================

output_text = tk.Text(

    main_frame,

    height=16,

    font=("Arial",11),

    wrap="word"

)

output_text.pack(

    fill="both",

    expand=True

)

# ============================================================
# WORD & CHARACTER COUNTER
# ============================================================

stats_frame = tk.Frame(

    main_frame,

    bg=LIGHT_BG

)

stats_frame.pack(

    fill="x",

    pady=8

)

word_label = tk.Label(

    stats_frame,

    textvariable=word_var,

    font=("Arial",10,"bold"),

    bg=LIGHT_BG

)

word_label.pack(

    side="left",

    padx=10

)

char_label = tk.Label(

    stats_frame,

    textvariable=char_var,

    font=("Arial",10,"bold"),

    bg=LIGHT_BG

)

char_label.pack(

    side="left",

    padx=20

)

# ============================================================
# UPDATE COUNTER
# ============================================================

output_text.bind(

    "<KeyRelease>",

    lambda event: update_count()

)

# ============================================================
# STATUS BAR
# ============================================================

status_label = tk.Label(

    root,

    textvariable=status_var,

    relief="sunken",

    bd=1,

    anchor="w",

    font=("Arial",10),

    bg="white"

)

status_label.pack(

    side="bottom",

    fill="x"

)

# ============================================================
# MENU BAR
# ============================================================

menu_bar = tk.Menu(root)

file_menu = tk.Menu(

    menu_bar,

    tearoff=0

)

file_menu.add_command(

    label="Save",

    command=save_text

)

file_menu.add_separator()

file_menu.add_command(

    label="Exit",

    command=root.destroy

)

menu_bar.add_cascade(

    label="File",

    menu=file_menu

)

edit_menu = tk.Menu(

    menu_bar,

    tearoff=0

)

edit_menu.add_command(

    label="Copy",

    command=copy_text

)

edit_menu.add_command(

    label="Clear",

    command=clear_text

)

menu_bar.add_cascade(

    label="Edit",

    menu=edit_menu

)

theme_menu = tk.Menu(

    menu_bar,

    tearoff=0

)

theme_menu.add_command(

    label="Toggle Theme",

    command=toggle_theme

)

menu_bar.add_cascade(

    label="Theme",

    menu=theme_menu

)

root.config(

    menu=menu_bar

)

# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(

    root,

    text="CODTECH Internship Task-4 | Generative Text Model using Groq AI",

    font=("Arial",9),

    bg=LIGHT_BG,

    fg="gray"

)

footer.pack(

    pady=4

)

# ============================================================
# INITIALIZE
# ============================================================

update_count()

status_var.set("Ready")

# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()