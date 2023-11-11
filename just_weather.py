import requests
from pprint import pprint
#from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Just Weather")
        self.root.configure(bg="#000000")
        self.root.geometry("360x640")

        self.label = tk.Label(self.root, text="Just Weather", font=('San Francisco', 27), foreground='white', background='black')
        self.label.pack(padx=10, pady=10)
        self.label = tk.Label(self.root, text="Check temperature\nin your town", font=('San Francisco', 20), foreground='white', background='black')
        self.label.pack(padx=5, pady=5)
        self.result_label = tk.Label(self.root, text='', font=('San Francisco', 20), foreground='white', background='black')
        self.result_label.pack(padx=5, pady=5)

        # Create labels and text boxes 
        #label1 = tk.Label(self.root, text="wpisz :3") 
        #label1.pack()
         
        self.textbox1 = tk.Entry(self.root)
        self.textbox1.pack(padx=30, pady=30)
        self.button = tk.Button(self.root, text="Check", command=self.get_user_input, foreground='white', background='black', font='Arial')
        self.button.pack()

        image = Image.open(f"C:\\Users\\miche\\Desktop\\06c4f70ec5931e2342e703e8a3f0a253.png")
        image = image.resize((200, 200))
        self.photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.image = self.photo 
        #self.image_label.place(x=10, y=10)
        self.image_label.pack(padx=100, pady=100)

        self.root.mainloop()

    def get_user_input(self):
        user_input = self.textbox1.get()
        self.func(user_input)

    def func(self, user_input):
        #city = input("Wpisz miasto: ")
        #API_Key = '1b6abf9b372a431fbcc214217230911'
        base_url = f'http://api.weatherapi.com/v1/current.json?key=1b6abf9b372a431fbcc214217230911&q={user_input}&aqi=no'
        data = requests.get(base_url).json()
        if 'current' in data and 'temp_c' in data['current']:
            temperatura = data['current']['temp_c']
            print(f"Temperatura {user_input}: {temperatura}°C")
            out = f"{user_input}: {temperatura}°C"
            #messagebox.showinfo(title="Wiadomosc", message=out)
            self.result_label.config(text=out)
        else:
            print("Nie udało się wczytać")
            '''print("Chciałbyś wpisać następne miasto? Śmiało wpisz następne jeśli chcesz, w innym wypadku nacisnij enter aby zamknąć lub obojetnie co innego aby kontynuoac")
            ui = input('Kontynuować')
            if ui == '':
                print("Zamykanie")
                time.sleep(1)
                return 0
            else:
                func(user_input)'''
Gui()