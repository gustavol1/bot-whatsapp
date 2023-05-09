from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
import tkinter
from tkinter import ttk
from tkinter import filedialog


# Declarando variáveis
contatos = []
mensagens = []
midia = []

# Funções
def iniciarBot():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://web.whatsapp.com/')
    time.sleep(30)

    def cade_contato(contato):
        achar_contato = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text")]')
        time.sleep(2)
        achar_contato.click()
        achar_contato.send_keys(contato)
        achar_contato.send_keys(Keys.ENTER)
        
    def enviar_mensagem(mensagens):
        for mensagem in mensagens:
            enviar_mensagem = driver.find_element(By.XPATH, '//p[contains(@class, "selectable-text copyable-text")]')
            enviar_mensagem.click()
            time.sleep(3)
            enviar_mensagem.send_keys(mensagem)
            enviar_mensagem.send_keys(Keys.ENTER)
            time.sleep(2)

    def enviar_midia(midia):
        enviar_midia = driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
        attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
        attach.send_keys(midia)
        time.sleep(3)
        send = driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
        send.click()

    for contato in contatos:
        cade_contato(contato)
        enviar_mensagem(mensagens)
        enviar_midia(midia) 
        time.sleep(1)

def addContato():
    contatos.append(contatosInput.get())
    
def addImg():
    img = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Image files", ["*jpg*", "*png*", "*jpeg*"]), ("all files", ("*-*"))))
    midia.append(img)
    
def addMsg():
    mensagens.append(mensagem_text.get("1.0", "end-1c"))
    
window = tkinter.Tk()
window.geometry('900x500')
window.resizable(width=False, height=False)
window.title("Bot de Mensagens para Whatsapp")

frame = tkinter.Frame(window)
frame.pack()

# Input para adcionar contatos
contatosFrame = tkinter.LabelFrame(frame, text="Contatos")
contatosFrame.grid(row=0, column=0, padx=25, pady=25)

contatosAdd = tkinter.Label(contatosFrame, text="Insira seus contatos")
contatosAdd.grid(row=0, column=1)

contatosInput = tkinter.Entry(contatosFrame)
contatosInput.grid(row= 1, column=1, padx=15, pady=15)

contatosBtn = tkinter.Button(contatosFrame, text="Adcionar Contato", command= addContato)
contatosBtn.grid(row=2, column=1, sticky="news", padx=20, pady=20)

#Criando input para a mensagem
mensagem_frame = tkinter.LabelFrame(frame, text="Mensagem")
mensagem_frame.grid(row= 0, column= 1, padx=25, pady=25)

mensagem = tkinter.Label(mensagem_frame, text="Insira sua mensagem")
mensagem_text = tkinter.Text(mensagem_frame, height=10, width=20)
mensagem.grid(row= 0, column= 1)
mensagem_text.grid(row=1, column=1)

mensagemButton = tkinter.Button(mensagem_frame, text="adcionar mensagem", command= addMsg)
mensagemButton.grid(row=2, column=1, sticky="news", padx=20, pady=20)

# Criando input para a imagem
imagemInput = tkinter.Button(mensagem_frame, text="Adcionar imagem", command= addImg)
imagemInput.grid(row=3, column=1, sticky="news", padx=20, pady=20)

# Iniciar o Bot
button = tkinter.Button(frame, text="Enviar mensagem", command=iniciarBot)
button.grid(row=2, column=0, sticky="news", padx=20, pady=20)

window.mainloop()
