import os, re, shutil
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

top = tk.Tk()
top.geometry("250x280")
top.title("Calculo=PS,PSM,PCX")

with open ('P:\Julien\Prog6 - PS\espessuras.txt',"r") as file1:
    esp=[]
    esp=file1.readlines()
file1.close()



texto=ttk.Label(top,text='espessura mesa superior')
texto.pack(side='top')
combo = ttk.Combobox(top,width=27)
combo.pack(side='top')
combo['values']=(esp)
combo.current()

texto1=ttk.Label(top,text='espessura mesa inferior')
texto1.pack(side='top')
combo1 = ttk.Combobox(top,width=27)
combo1.pack(side='top')
combo1['values']=(esp)
combo1.current()


texto2=ttk.Label(top,text='espessura alma')
texto2.pack(side='top')
combo2 = ttk.Combobox(top,width=27)
combo2.pack(side='top')
combo2['values']=(esp)
combo2.current()

texto3=ttk.Label(top,text='altura perfil')
texto3.pack(side='top')
valor= ttk.Entry()
valor.pack(side='top')

texto4=ttk.Label(top,text='mesa superior')
texto4.pack(side='top')
valor1= ttk.Entry()
valor1.pack(side='top')

texto5=ttk.Label(top,text='mesa inferior')
texto5.pack(side='top')
valor2= ttk.Entry()
valor2.pack(side='top')



def cadastre():
    esp_ms=float(combo.get())
    esp_mi=float(combo1.get())
    esp_al=float(combo2.get())
    h=float(valor.get())
    l1=float(valor1.get())
    l2=float(valor2.get())
    peso_ps=(l1*esp_ms+l2*esp_mi+esp_al*(h-esp_ms-esp_mi))*0.00785
    peso_pcx=(l1*esp_ms+l2*esp_mi+2*esp_al*(h-esp_ms-esp_mi))*0.00785
    messagebox.showinfo('Peso PS/PSM: ', peso_ps)   
    messagebox.showinfo('Peso PCX: ', peso_pcx)
    
bt = ttk.Button(top, text = 'Calcule',command=cadastre)
bt.pack(side='top')

top.mainloop()
