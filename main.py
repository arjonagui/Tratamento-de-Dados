#Automação de processos

#etapas:

#buscas os dados das ações
#gerar as análises de forma automática
#enviar um e-mail para um "gestor"

# etapa 1:

import yfinance

codigo = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(codigo).history("6mo")

fechamento = dados.Close


#Análise dos últimos seis meses
#Cotação máxima 
#Cotação mínima
#Cotação atual

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

#automação

import pyautogui
import pyperclip

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

pyperclip.copy("www.gmail.com")

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

pyautogui.click(x = 34, y = 216)

pyperclip.copy("gestor@nemexiste.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

mensagem = f"""
Prezado gestor,

Seguem as análises diárias dos últimos seis meses da ação {codigo}:

Cotação máxima: R${round(maxima, 2)}
Cotação mínima: R$${round(minima, 2)}
Cotação atual: R$${round(atual, 2)}

Qualquer dúvida, fico à disposição!

Att. Guilherme Goes
"""

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

#botão de enviar

pyautogui.click(x = 1308, y = 1001)

