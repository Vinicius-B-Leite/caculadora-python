import PySimpleGUI as sg

#Layout da tela 
def tela():
    layout = [
        [sg.Canvas(size=(0, 2))],
        [sg.Text("", justification="center", font=10, size=(25, 2), background_color="white", text_color="black", key="cursor")],
        [sg.Canvas(size=(0, 2))],
        [sg.Button("1", font=1, size=(5, 3)), sg.Button("2", font=1, size=(5, 3)), sg.Button("3", font=1, size=(5, 3)), sg.Button("+", font=1, size=(5, 3), button_color='#606060')],
        [sg.Button("4", font=1, size=(5, 3)), sg.Button("5", font=1, size=(5, 3)), sg.Button("6", font=1, size=(5, 3)), sg.Button("-", font=1, size=(5, 3), button_color='#606060')],
        [sg.Button("7", font=1, size=(5, 3)), sg.Button("8", font=1, size=(5, 3)), sg.Button("9", font=1, size=(5, 3)), sg.Button("*", font=1, size=(5, 3), button_color='#606060')],
        [sg.Button("C", font=1, size=(5, 3), button_color='#606060'),sg.Button("0", font=1, size=(5, 3)), sg.Button("=", font=1, size=(5, 3), button_color='#606060'), sg.Button("/", font=1, size=(5, 3), button_color='#606060')],
        [sg.Canvas(size=(0, 2))]
    ]

    tela = sg.Window("Calc", layout, finalize=True)
    return tela



conta = "" #variável que vai ser usada para fazer o cálculo 
tela = tela() #criando a tela
while True:
    ev, val = tela.read()
    
    if ev == sg.WINDOW_CLOSED: #se o usuário fechar a tela
        break
    
    if ev == "C": #evento de limpar o cursor(C)
        conta = "" #zera a variável
        tela['cursor'].update("") #limpa o cursor

    elif ev == "=": #se o usuário querer a resposta da conta
        if conta[-1] not in ("+", "-", "/", "*"): #verificando se a última coisa digitada não foi um operador
            tela['cursor'].update(value=eval(conta)) #faz a conta e atualiza o cursor
            conta = str(eval(conta)) #atualiza a variável 
        else: # se a última coisas digitada foi um operador pega o penúltima coisa digitada
            conta += conta[-2]
            tela['cursor'].update(value=eval(conta))
            conta = str(eval(conta))

    else:#se o usuário digitou números ou operadores
        conta += ev
        tela['cursor'].update(value=conta)
    
