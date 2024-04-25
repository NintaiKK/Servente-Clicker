import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

janela = tk.Tk()
janela.resizable(0,0)
janela.geometry('800x500')
janela.title('Servente Clicker')

eqpAtual = 'Colher enferrujada'

def mendigar():
    value = int(dnr["text"])
    dnr["text"] = f"{value + 1}"

frameClk = tk.Frame(
    width = 400,
    height = 250)

frameOps = tk.Frame(
    height = 500,
    width = 250)

spc = tk.Label(
    master = frameClk,
    height = 5)
spc.pack()

enxada = tk.Button(
    master = frameClk,
    command = mendigar,
    text = 'Capinar',
    width = 20,
    height = 5,
    bg = 'gray')
enxada.pack()

spc2 = tk.Label(
    master = frameClk,
    height = 2)
spc2.pack()

lblNm = tk.Label(
    master = frameClk,
    text = 'Enxadadas')
lblNm.pack()

dnr = tk.Label(
    master = frameClk,
    text = '0')
dnr.pack()

spc3 = tk.Label(
    master = frameOps,
    height = 5)
spc3.pack()

eqp = tk.Label(
    master = frameOps,
    text = f'Equipamento: {eqpAtual}')
eqp.pack(side = LEFT)

spc4 = tk.Label(
    master = frameOps,
    width = 100)
spc4.pack(side = LEFT)

frameClk.pack()
frameOps.pack()
janela = mainloop
