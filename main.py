import PySimpleGUI as sg
from calc import add, sub, mul, div

calc_dict = {
    "-ADD-": "+ (Add)",
    "-SUB-": "- (Sub)",
    "-MUL-": "* (Mul)",
    "-DIV-": "/ (Div)",
}

CLOSE_APP = "Close"

calc_frame = [
 [sg.Text("Number 1: "), sg.InputText(key="-NUM1-")],
 [sg.Radio(item[1], key=item[0], group_id='calc') for item in calc_dict.items()],
 [sg.Text("Number 2: "), sg.InputText(key="-NUM2-")],
 [sg.Submit(tooltip="Calculate", key="-CALC-")],
 [sg.Output(size=(30, 10))]
]

layout = [
    [sg.Frame("Calc", calc_frame)],
    [sg.Button(CLOSE_APP)]
]

window = sg.Window("Calc Sample", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == CLOSE_APP:
        sg.popup('Bye', title="Close")
        break

    elif event == "-CALC-":
        num1 = values["-NUM1-"]
        num2 = values["-NUM2-"]

        if values["-ADD-"]:
            add_result = add(int(num1), int(num2))
            result = num1 + " + " + num2 + " = " + str(add_result)
            print(result)
        elif values["-SUB-"]:
            add_result = sub(int(num1), int(num2))
            result = num1 + " - " + num2 + " = " + str(add_result)
            print(result)
        elif values["-MUL-"]:
            add_result = mul(int(num1), int(num2))
            result = num1 + " * " + num2 + " = " + str(add_result)
            print(result)
        elif values["-DIV-"]:
            add_result = div(int(num1), int(num2))
            result = num1 + " / " + num2 + " = " + str(add_result)
            print(result)


window.close()