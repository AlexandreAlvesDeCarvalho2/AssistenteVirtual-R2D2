import time
import speech_recognition as sr # biblioteca para reconhecer 
from playsound import playsound
import os 
import pyautogui
import spotipy 
from spotipy.oauth2 import SpotifyOAuth


#Função para ouvir e reconhecer a fala
def ouvir_microfone():  
    while True:
        microfone = sr.Recognizer() #Habilita o microfone do usuário        
        with sr.Microphone() as source: #usando o microfone        
            print("Diga alguma coisa: ")
            
            audio = microfone.listen(source, timeout= None) #Armazena o que foi dito em uma variavel
            
            try:
                frase = microfone.recognize_google(audio,language='pt-BR') #Passa a variável para o algoritmo reconhecedor de padroes
            
                if 'R2 D2' in frase:
                        print(frase)
                        playsound("sounds/3.mp3")  
                        break        
                else:
                    print(frase)
                    break
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
    return frase

os.environ['SPOTIPY_CLIENT_ID'] = 'x'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'x'
os.environ['SPOTIPY_REDIRECT_URI'] = 'https://example.com/callback'

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

while True:
    comando = "R2 D2"
    if "R2 D2" in comando:
        print("Comando R2D2 OK")
        comando = "commitar projeto Python Assistente Virtual"
        # comandos
        if "tocar playlist" in comando:
            os.system("taskkill /f /im spotify.exe")
            os.system("start spotify")
            os.system("exit")
            time.sleep(5)
            comando = comando.replace('tocar playlist','')

            for e in range(8):
                pyautogui.press('tab')

            for e in range(int(comando)):
                pyautogui.press('down')
            
            pyautogui.press('enter')
            pyautogui.hotkey('alt','tab')

        elif "luz da sala de jantar" in comando:    
            pyautogui.hotkey('ctrl','shift','F12')
            playsound("sounds/15.mp3")
            print(comando + ": Concluido!")
        

        elif 'tocar música' in comando.lower():
            os.system("taskkill /f /im spotify.exe")

            os.system("start spotify")
            time.sleep(3)

            pyautogui.hotkey('ctrl', 'l')
            consulta = comando.lower().replace('tocar música','').strip()
        
            pyautogui.write(consulta)
            pyautogui.press('enter')

            time.sleep(2)
            pyautogui.click(379,472)

            print('Tocando ' + consulta)
            time.sleep(20)
   
        elif 'pausar musica' in comando.lower():
            sp.pause_playback()
        
        elif 'continuar musica' in comando.lower():
            sp.start_playback()
        
        elif 'mudar volume para' in comando.lower():
            volume = int(comando.lower().replace('mudar volume para','').strip())
            sp.volume(volume)
        
        elif 'commitar projeto' in comando.lower():
            # exemplo: comitar projeto Python Assistente Virtual
            comando = comando.lower().replace('commitar projeto','') # remover o texto comitar projeto da variavel 
            linguagem = comando.split()[0] # pegar a primeira palavra da variável
            projeto = comando.lower().replace(linguagem,'').strip() # remover a primeira palavra 
            os.system('start cmd')
            time.sleep(1)
            pyautogui.write("cd C:/Users/alexa/Desktop/DevApps/Repositorios/"+linguagem+"/"+projeto)
            pyautogui.press('enter')
            pyautogui.write("git add .")
            pyautogui.press('enter')
            pyautogui.write("git status")
            pyautogui.press('enter')
            pyautogui.write('git commit -m " "')

            #print(projeto)
            #print("cd C:/Users/alexa/Desktop/DevApps/Repositórios/"+linguagem+"/"+projeto)
            time.sleep(20)


