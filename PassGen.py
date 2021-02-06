# Libs
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Print, Spin, Window


def winPass():
    sg.theme("Python")

    spin = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
            51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    layout = [
        [sg.Text(" " * 15), sg.Text("-- PASSWORD GEN --")],
        
        [sg.Text("-" * 70)],

        [sg.Text(" " * 28), sg.Spin((spin), initial_value=1, key="spin", size=(3, 0))],
        [sg.Checkbox("abcd", key="char1"), sg.Checkbox("ABCD", key="char2"), sg.Checkbox("1234", key="char3"), sg.Checkbox("!@#$%&*", key="char4")],

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

    # Info Password
    password = ""
    lenpassword = int(values["spin"])

    char1 = str(values["char1"])
    char1_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    char2 = str(values["char2"])
    char2_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    char3 = str(values["char3"])
    char3_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    char4 = str(values["char4"])
    char4_list = ["!", "@", "#", "$", "%", "&", "*"]

    contador_caracteres = 0
    if char1 == "True":
        contador_caracteres+=1
    if char2 == "True":
        contador_caracteres+=1
    if char3 == "True":
        contador_caracteres+=1
    if char4 == "True":
        contador_caracteres+=1

    passlen = lenpassword / contador_caracteres

    def GenPass(password, list1, list2, list3, list4):
        from time import sleep
        from random import choice


        for x in range(0, int(passlen)):
            if char1 == "True":
                password += choice(list1)
            if char2 == "True":
                password += choice(list2)
            if char3 == "True":
                password += choice(list3)
            if char4 == "True":
                password += choice(list4)

        lenpass = len(password)


        def PrintPass():
            sleep(0.5)
            print("__ GENERATING __".center(52))
            sleep(2)
            
            print(f"Password: → {password} ←")
            print("")

        
        return PrintPass()
    

    if event == "Gen":
        GenPass(password, char1_list, char2_list, char3_list, char4_list)
