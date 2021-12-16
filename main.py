import PySimpleGUI as sg
from calc import add, sub, mul, div

NUM1 = "NUM1"
NUM2 = "NUM2"
ADD = "+"
SUB = "-"
MUL = "*"
DIV = "/"
CLOSE_APP = "Close"

calc_frame = [
 [sg.InputText(key=NUM1)],
 [sg.Button(ADD),sg.Button(SUB), sg.Button(MUL), sg.Button(DIV)],
 [sg.InputText(key=NUM2)]
]

layout = [
    [sg.Frame("Calc", calc_frame)],
    [sg.Button(CLOSE_APP)]
]

window = sg.Window("Calc Sample", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == CLOSE_APP:
        break
    elif event == ADD:
        add_result = add(int(values[NUM1]),int(values[NUM2]))
        result = values[NUM1] + " + " + values[NUM2] + " = " + str(add_result)
        sg.popup(result)
    elif event == SUB:
        sub_result = sub(int(values[NUM1]), int(values[NUM2]))
        result = values[NUM1] + " - " + values[NUM2] + " = " + str(sub_result)
        sg.popup(result)
    elif event == MUL:
        mul_result = mul(int(values[NUM1]), int(values[NUM2]))
        result = values[NUM1] + " * " + values[NUM2] + " = " + str(mul_result)
        sg.popup(result)
    elif event == DIV:
        div_result = div(int(values[NUM1]), int(values[NUM2]))
        result = values[NUM1] + " / " + values[NUM2] + " = " + str(div_result)
        sg.popup(result)


window.close()