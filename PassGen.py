import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Spin, Window

def winPass():
    sg.theme("Python")

    spin = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
            51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    layout = [
        [sg.Text(" " * 15), sg.Text("-- PASSWORD GEN --")],
        
        [sg.Text("-" * 70)],

        #[sg.Text(" " * 22), sg.Text("-- Caracters --")],
        [sg.Text(" " * 28), sg.Spin((spin), initial_value=1, key="spin", size=(3, 0))],
        [sg.Checkbox("abcd", ), sg.Checkbox("ABCD"), sg.Checkbox("1234"), sg.Checkbox("!@#$%&*")],

        [sg.Text("-" * 70)],

        [sg.Text(" " * 26), sg.Button("Gen")],
        
        [sg.Output(size=(38, 4))],
        [sg.Text(" " * 20), sg.Text("(c) NT Developer")]
    ]
    return sg.Window("PassGen", layout=layout)


window = winPass()

while True:
    event, values = window.Read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Gen":
        pass

    for x in range(1, 10):
        print(x)
