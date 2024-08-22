import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyttsx3
import os

if "voices" not in os.listdir():
    os.mkdir("voices")
number_of_saved_sounds = len(os.listdir("voices"))

combo_menu = {
    "speed" : ["Very Fast", "Fast", "Normal", "Slow", "Very Slow"],
    "gender" : ["Male", "Female"],
    "volume" : ["Silent", "Low", "Medium", "High", "Very High"],
}

root = tk.Tk()
root.resizable(False, False)
root.geometry("900x500")
root.config(bg="#4E4F61")
root.title("Speak Text")

engine = pyttsx3.init()

def set_voice_gender():
    voices = engine.getProperty("voices")
    if gender.get().title() == "Male":
        id = 0
    elif gender.get().title() == "Female":
        id = 1
    else:
        messagebox.showerror(title="Error", message="ERROR!!")
        return
    engine.setProperty("voice", voices[id].id)


def set_voice_speed():
    if speed.get().title() == "Very Slow":
        rate = 70
    elif speed.get().title() == "Slow":
        rate = 100
    elif speed.get().title() == "Normal":
        rate = 150
    elif speed.get().title() == "Fast":
        rate = 200
    elif speed.get().title() == "Very Fast":
        rate = 300
    else:
        messagebox.showerror(title="Error", message="ERROR!!")
        return
    engine.setProperty("rate", rate)


def set_voice_volume():
    if volume.get().title() == "Silent":
        vol = 0
    elif volume.get().title() == "Low":
        vol = 0.25
    elif volume.get().title() == "Medium":
        vol = 0.5
    elif volume.get().title() == "High":
        vol = 0.75
    elif volume.get().title() == "Very High":
        vol = 1
    else:
        messagebox.showerror(title="Error", message="ERROR!!")
        return
    engine.setProperty("volume", vol)
    
def speak_and_download(flag):
    global number_of_saved_sounds
    text = txt_user_text.get(1.0, "end-1c")
    set_voice_gender()
    set_voice_speed()
    set_voice_volume()
    if flag == "speak":
        engine.say(text)
    else:
        with open("history.txt", "a") as writer:
            writer.write(text + "\n")
        engine.save_to_file(text, f"voices\{number_of_saved_sounds}.mp3")
        number_of_saved_sounds += 1
    engine.runAndWait()





def delete_file(history_window):
    history_window.destroy()
    os.remove("history.txt")


def history():
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as reader:
            text = reader.read()
        history_window = tk.Tk()
        history_window.resizable(False, False)
        history_window.geometry("500x800")
        history_window.title("History")

        tk.Label(
            history_window,
            text= text,
            font= "arial 15",
            bg= "#000",
            fg= "#fff",
        ).place(x=0, y=0, width=500, height=800)

        tk.Button(
            history_window,
            text= "Delete all",
            font= "arial 15",
            bg= "#E81616",
            activebackground= "#E81616",
            command= lambda: delete_file(history_window),
        ).place(x=380, y=20)
        history_window.mainloop()
    else:
        messagebox.showerror(title="ERROR", message="There is no history.")

lbl_heading = tk.Label(
    root,
    text= "SPEAK TEXT",
    font= "arial 20 bold",
    bg= "#1B1E53",
    fg= "#D8D816",
)

lbl_string = tk.Label(
    root,
    text= "Enter your text :",
    font= "arial 15",
    bg= "#4E4F61",
)

lbl_speed = tk.Label(
    root,
    text= "Speed :",
    font= "arial 15",
    bg= "#4E4F61",
)

lbl_gender = tk.Label(
    root,
    text= "Voice :",
    font= "arial 15",
    bg= "#4E4F61",
)

lbl_volume = tk.Label(
    root,
    text= "Volume :",
    font= "arial 15",
    bg= "#4E4F61",
)

speed = tk.StringVar(value="Normal")
combo_speed = Combobox(
    root,
    textvariable= speed,
    font= "arial 10 bold",
    values= combo_menu["speed"],
)

gender = tk.StringVar(value="Male")
combo_gender = Combobox(
    root,
    textvariable= gender,
    font= "arial 10 bold",
    values= combo_menu["gender"],
)

volume = tk.StringVar(value="Medium")
combo_volume = Combobox(
    root,
    textvariable= volume,
    font= "arial 10 bold",
    values= combo_menu["volume"],
)

txt_user_text = tk.Text(
    root,
    font= "arial 15",
    bd= 0,
    wrap="word",
)

btn_speak = tk.Button(
    root,
    text= "Speak",
    font= "arial 15 bold",
    bg= "#E0AB07",
    activebackground= "#E0AB07",
    command= lambda: speak_and_download("speak"),
)

btn_download = tk.Button(
    root,
    text= "Download",
    font= "arial 15 bold",
    bg= "#20CC14",
    activebackground= "#20CC14",
    command= lambda: speak_and_download("download"),
)

btn_history = tk.Button(
    root,
    text= "History",
    font= "arial 15 bold",
    bg= "#22E3E0",
    activebackground= "#22E3E0",
    command= history,
)

lbl_heading.place(x=0, y=0, width=900, height=100)
lbl_string.place(x=40, y=180)
txt_user_text.place(x=210, y=130, width=600, height=130)
lbl_speed.place(x=30, y=295)
combo_speed.place(x=120, y=300)
lbl_gender.place(x=300, y=295)
combo_gender.place(x=390, y=300)
lbl_volume.place(x=580, y=295)
combo_volume.place(x=680, y=300)
btn_speak.place(x=120, y=400, width=160, height=50)
btn_download.place(x=370, y=400, width=160, height=50)
btn_history.place(x=620, y=400, width=160, height=50)
root.mainloop()