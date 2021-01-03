from gtts import gTTS
from os import remove
import os
from time import sleep
from playsound import playsound as play
import speech_recognition as sr
import keyboard as kb
import sys
from datetime import datetime as dt
from datetime import date
import urllib
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def speak(text):
    tts = gTTS(text=text, lang='pt-br', slow=False)
    filename ='voz.mp3'
    tts.save(filename)
    play(filename)
    remove(filename)
r = sr.Recognizer()
continua = False
while True:
    if kb.is_pressed('alt+b') or continua == True:
        with sr.Microphone() as source:
            print('diga algo')
            audio = r.listen(source)
        try:
            frase = str(r.recognize_google(audio, language='pt-br'))
            print(frase)
            if frase == 'Ok Bia':
                speak('Olá, como posso ajudar?')
                continua = True
            if frase == 'sair':
                speak('saindo')
                continua = False
                sys.exit()
                quit()
            if frase == 'Que horas são':
                if dt.now().hour < 12:
                    horario = 'manhã'
                elif dt.now().hour < 18:
                    horario = 'tarde'
                else:
                    horario = 'noite'
                speak(f'são {dt.now().hour} e {dt.now().minute} da {horario}')
                continua = False
            if frase == 'Que dia é hoje':
                dias = [
                    'Segunda-feira',
                    'Terça-feira',
                    'Quarta-feira',
                    'Quinta-Feira',
                    'Sexta-feira',
                    'Sábado',
                    'Domingo'
                ]
                data = date(year=dt.now().year, month=dt.now().month, day=dt.now().day)
                speak(f'Hoje é {dias[data.weekday()]}')
                continua = False
            if frase == 'Qual a data de hoje':
                mes_num = dt.now().month
                mes = ''
                if mes_num == 1:
                    mes = 'Janeiro'
                if mes_num == 2:
                    mes = 'Fevereiro'
                if mes_num == 3:
                    mes = 'Março'
                if mes_num == 4:
                    mes = 'Abril'
                if mes_num == 5:
                    mes = 'Maio'
                if mes_num == 6:
                    mes = 'Junho'
                if mes_num == 7:
                    mes = 'Julho'
                if mes_num == 8:
                    mes = 'Agosto'
                if mes_num == 9:
                    mes = 'Setembro'
                if mes_num == 10:
                    mes = 'Outubro'
                if mes_num == 11:
                    mes = 'Novembro'
                if mes_num == 12:
                    mes = 'Dezembro'
                speak(f'Hoje é dia {dt.now().day} de {mes}')
                continua = False
            if frase.split(' ')[0] == 'pesquisar':
                pesquisar = frase.replace('pesquisar', '').replace(' ', '+')
                webbrowser.open(f'https://www.google.com/search?q={pesquisar[1:]}')
            if frase.split(' ')[0] == 'YouTube':
                if frase == 'YouTube':
                    webbrowser.open('https://www.youtube.com/')
                else:
                    pesquisar = frase.replace('YouTube', '').replace(' ', '+')
                    webbrowser.open(f'https://www.youtube.com/results?search_query={pesquisar[1:]}')
            if frase == 'abrir o meu github' or frase == 'abrir o meu kit Ruby' or frase == 'abrir o meu Git Hub' or frase == 'abrir o meu kit Rubi':
                arquivo = open('configs.txt', 'a')
                arquivo.close()
                arquivo = open('configs.txt', 'r')
                ler = arquivo.readlines()
                tem = False
                for linha in ler:
                    if 'GitHub:::' in linha:
                        tem = True
                        conta = linha.replace('GitHub:::', '')
                arquivo.close()
                if tem == True:
                    speak('Abrindo o seu GitHub')
                    webbrowser.open(f'https://github.com/{conta}')
                else:
                    speak('Sua conta do GitHub não está cadastrada ainda, por favor digite o nome da sua conta')
                    conta = str(input('Digite o nome da sua conta: '))
                    speak('Obrigado pela comprensão')
                    os.system('cls')
                    arquivo = open('configs.txt', 'a')
                    arquivo.write(f'GitHub:::{conta}\n')
                    speak('Abrindo o seu GitHub')
                    webbrowser.open(f'https://github.com/{conta}')
            if len(frase.split(' ')) >= 2:
                if frase.split(' ')[0] == 'github' or str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'kit Ruby' or str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'Git Hub' or str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'kit Rubi':
                    if frase.split(' ')[0] == 'github':
                        pesquisar = frase.replace('github', '').replace(' ', '+')
                        frase_github = frase.replace('github', '')
                        speak(f'Pesquisando {frase_github} no GitHub')
                    if str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'kit Ruby':
                        pesquisar = frase.replace('kit Ruby', '').replace(' ', '+')
                        frase_github = frase.replace('kit Ruby', '')
                        speak(f'Pesquisando {frase_github} no GitHub')
                    if str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'Git Hub':
                        pesquisar = frase.replace('Git Hub', '').replace(' ', '+')
                        frase_github = frase.replace('Git Hub', '')
                        speak(f'Pesquisando {frase_github} no GitHub')
                    if str(frase.split(' ')[0]+' '+frase.split(' ')[1]) == 'kit Rubi':
                        pesquisar = frase.replace('kit Rubi', '').replace(' ', '+')
                        frase_github = frase.replace('kit Rubi', '')
                        speak(f'Pesquisando {frase_github} no GitHub')
                    webbrowser.open(f'https://github.com/search?q={pesquisar[1:]}')
            if frase == 'ver meu canal no YouTube':
                arquivo = open('configs.txt', 'a')
                arquivo.close()
                arquivo = open('configs.txt', 'r')
                ler = arquivo.readlines()
                tem = False
                for linha in ler:
                    if 'YouTube:::' in linha:
                        id_canal = linha.replace('YouTube:::', '')
                        webbrowser.open(id_canal)
                        tem = True
                if tem == False:
                    speak('Você não tem um canal cadastrado, por favor digite o nome do seu canal ou o link dele')
                    link_conta = str(input('Digite o link ou nome do seu canal: '))
                    if 'https://' in link_conta:
                        arquivo = open('configs.txt', 'a')
                        arquivo.write(f'YouTube:::{link_conta}\n')
                        arquivo.close()
                        speak('Canal cadastrado com sucesso')
                        speak('Abrindo o canal')
                        webbrowser.open(link_conta)
                    else:
                        nome = link_conta
                        speak('Conferindo link do canal')
                        driver = webdriver.Chrome(executable_path=os.getcwd()+os.sep+'chromedriver.exe')
                        str_pesquisar = nome.replace(' ', '+')
                        driver.get(f'https://www.youtube.com/results?search_query={str_pesquisar}&sp=EgIQAg%253D%253D')
                        driver.find_element_by_xpath('//*[@id="avatar-section"]/a').click()
                        url = driver.current_url
                        sleep(2)
                        driver.close()
                        arquivo = open('configs.txt', 'a')
                        arquivo.write(f'YouTube:::{url}\n')
                        arquivo.close()
                        speak('Canal cadastrado com sucesso')
                        os.system('cls')
                        speak('Abrindo o seu canal')
                        webbrowser.open(url)
            if frase == 'mudar a minha conta do YouTube':
                speak('Digite o nome ou link do seu canal')
                arquivo = open('configs.txt', 'a')
                arquivo.close()
                arquivo = open('configs.txt', 'r')
                ler = arquivo.readlines()
                for linha in ler:
                    if 'YouTube:::' in linha:
                        link_conta = str(input('Digite o nome ou link do seu canal: '))
                        arquivo.close()
                        arquivo = open('configs.txt', 'r')
                        ler = arquivo.readlines()
                        linhas = ''
                        for linha in ler:
                            if 'YouTube' not in linha:
                                linhas += linha
                        arquivo.close()
                        if 'https://' in link_conta:
                            arquivo = open('configs.txt', 'a')
                            arquivo.write(f'YouTube:::{link_conta}\n')
                            arquivo.close()
                            speak('Canal cadastrado com sucesso')
                            speak('Abrindo o canal')
                            webbrowser.open(link_conta)
                        else:
                            nome = link_conta
                            speak('Conferindo link do canal')
                            driver = webdriver.Chrome(executable_path=os.getcwd()+os.sep+'chromedriver.exe')
                            str_pesquisar = nome.replace(' ', '+')
                            driver.get(f'https://www.youtube.com/results?search_query={str_pesquisar}&sp=EgIQAg%253D%253D')
                            driver.find_element_by_xpath('//*[@id="avatar-section"]/a').click()
                            url = driver.current_url
                            sleep(2)
                            driver.close()
                            arquivo = open('configs.txt', 'a')
                            arquivo.write(f'YouTube:::{url}\n')
                            arquivo.close()
                            speak('Canal cadastrado com sucesso')
                            os.system('cls')
                            speak('Abrindo o seu canal')
                            webbrowser.open(url)
                    else:
                        speak('Você não possui uma conta do YouTube cadastrada pra mudar')
        except sr.UnknownValueError:
            print('Não Entendi')
            
        ok = False
