import pyautogui

def MoverParaImagem(imagem):
    start = pyautogui.locateOnScreen(imagem,confidence=0.8)
    print(start)
    pyautogui.moveTo(start)

MoverParaImagem('Iniciar.png')
MoverParaImagem('py.png')
MoverParaImagem('debug.png')



