import tkinter
from tkinter import PhotoImage
from tkinter import messagebox

import messagebox
from cryptography.fernet import Fernet

window = tkinter.Tk()
window.title("Cryptocode")
window.minsize(350, 600)
window.config(bg="aliceblue", padx=50, pady=100)

FONT = ("Arial", 10, "bold")


def button_save_crypt():




    x = entry_title.get()

    y = secret_text.get("1.0", tkinter.END)
    z = entry_key.get()
    open("cryptofile.txt",mode="a")

    ''''
    with open("cryptofile.txt") as file:
        f = file.read()
        '''



    if z == "" or y== "" or x=="":
        messagebox.showerror("showerror", "enter values")
    else:

        y = Fernet.generate_key()
        f = Fernet(y)
        tok = f.encrypt(y)

        tok = y.decode("utf-8").rstrip()
        


        with open("cryptofile.txt", mode="a") as d:
            d.write(x + ": \n")
            d.write(tok)
            d.write("\n")
            #d.write(dc)
            #d.write(dk)
            print(tok)













    entry_title.delete(first="0", last=tkinter.END)
    secret_text.delete(1.0, tkinter.END)

    entry_key.delete(first="0", last=tkinter.END)




''''
def dec_button():
    z = entry_key.get()
    y = secret_text.get()
    f = Fernet(y)
    
    dc = tok.decode("utf-8").rstrip()
    dk = f.decrypt(dc)
    


    if input(secret_text) == tok and input(entry_key) == z:
        secret_text.insert(f.decrypt())
       



    else:
        tkinter.messagebox.showerror("showerror", "wrong")
         '''



path = "C:/Users/AKİF-PC/Desktop/top_secret.png"

image = PhotoImage(file=path)
label_image = tkinter.Label(window, image=image, width=160, height=160)
label_image.pack()

entry_title_label = tkinter.Label(text="enter your title", font=FONT, pady=10)
entry_title_label.pack()

entry_title = tkinter.Entry(width=35)
entry_title.pack()

text_label = tkinter.Label(text="enter your secrets", font=FONT, pady=10)
text_label.pack()

secret_text = tkinter.Text()
secret_text.config(width=40, height=22, padx=10, pady=20)

secret_text.pack()

entry_key_label = tkinter.Label(text="enter master key", font=FONT, pady=10)
entry_key_label.pack()

entry_key = tkinter.Entry(width=35)
entry_key.pack()

crypt_button = tkinter.Button(text="Save & Encrypt", bd=3, command=button_save_crypt)

crypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt", bd=3)
decrypt_button.pack(side="bottom")



label_error = tkinter.Label()
label_error.pack()
'''
key = Fernet.generate_key()
f = Fernet(key)
token = f. encrypt(b"akif")
print("şifreli metin:\n", token)
'''

window.mainloop()
