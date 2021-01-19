from gtts import gTTS
from os import remove
from playsound import playsound as play

def speak(text):
    tts = gTTS(text=text, lang='pt-br', slow=False)
    filename ='voz.mp3'
    tts.save(filename)
    play(filename)
    remove(filename)
def buscasContas(conta, existir=False):
    arquivo = open('configs.txt', 'r')
    ler = arquivo.readlines()
    achou = False
    for linha in ler:
        if f'{conta}:::' in linha:
            achou = True
            if not existir:
                return linha.split(f'{conta}:::')[1]
            else:
                return True
    if achou == False:
        return False
    arquivo.close()
def mudarConta(conta, nova, UVA=False):
    if UVA == True:
        arquivo = open('configs.txt', 'r')
        ler = arquivo.readlines()
        existe = False
        for linha in ler:
            if conta in linha:
                existe = True
        if existe == False:
            arquivo = open('configs.txt', 'a')
            arquivo.write(f'{conta}:::{nova}\n')
            arquivo.close()
            quit()
        arquivo.close()
    lista_contas = ''
    arquivo = open('configs.txt', 'r')
    ler = arquivo.readlines()
    for linha in ler:
        if f'{conta}:::' not in linha:
            lista_contas += linha
    arquivo.close()
    lista_contas += f'{conta}:::{nova}\n'
    arquivo = open('configs.txt', 'w')
    arquivo.write(lista_contas)
    arquivo.close()