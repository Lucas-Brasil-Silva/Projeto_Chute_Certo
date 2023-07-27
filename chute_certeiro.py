import PySimpleGUI as sg
from utilities import verificar_chute, sorteando_numero

sg.theme('Topanga')

def windowGame():
    layout = [
        [sg.Text('Chute um numero de 1 à 100: ')],
        [sg.Input(key='chute',size=(4,1)), sg.Button('Chutar')],
        [sg.Output(size=(25,2))]
    ]

    return sg.Window('Acerte o Chute!', layout,finalize=True)

def windowFinalize():
    layout = [
        [sg.Text('Continuar jogando?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]

    return sg.Window('Finalize', layout,finalize=True)

def main():
    windowGame_, windowFinalize_ = windowGame(), None
    sortia = True

    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED:
            break
        
        elif window == windowGame_:
            try:
                if event == 'Chutar':
                    if sortia:
                        numero_sorteado = sorteando_numero()
                        sortia = False
                    resultado = verificar_chute(numero_sorteado,int(values['chute']))
                    window['chute'].update('')
                    if resultado == True:
                        sg.popup(f'Parabéns você acerto o chute!!\nNumero Sorteado: {values["chute"]}')
                        windowGame_.close()
                        windowFinalize_ = windowFinalize()
            
            except ValueError:
                sg.popup('Digite apenas números!')
                window['chute'].update('')
                    
        elif window == windowFinalize_:
            if event == 'Sim':
                sortia = True
                windowFinalize_.close()
                windowGame_ = windowGame()
            else:
                break


if __name__ == '__main__':
    main()