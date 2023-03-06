from page import page_conversor
import re
import requests
import PySimpleGUI as sg

class Main():
    def __init__(self) -> None:
        self.window = page_conversor()
    def executar(self):
        while True:
            event, values = self.window.read(timeout=10)
            
            if event == sg.WIN_CLOSED:
                break
            
            pais_1 = str(values["equivalente"][:3])
            pais_2 = str(values["equivalecia"][:3])
            
            if bool(values["valor"]):
                valor_moeda = str(values["valor"])
                validacao = re.search(r'^[0-9]+$', valor_moeda)
                if validacao:
                    if bool(values["equivalente"]) and bool(values["equivalecia"]):
                        try:
                            requisicao = requests.get(f"http://economia.awesomeapi.com.br/json/last/{pais_1}-{pais_2}")
                            valores = requisicao.json()
                            pais = pais_1 + pais_2
                            valor_cotacao = float(float(valores[pais]["bid"]) * float(values["valor"]))
                            valor_variacao = valores[pais]["varBid"]
                            valor_porc_variacao = valores[pais]["pctChange"]
                            self.window["valor_moeda"].update("img\Valor Moeda.png")
                            self.window["resultado"].update(f"{valor_moeda} {pais_1} igual a {valor_cotacao:.2f} {pais_2}")
                            self.window["variacao"].update(f"{valor_variacao}")
                            self.window["porcentagem_var"].update(f"{valor_porc_variacao}")
                        except KeyError as erro:
                            self.window["valor_moeda"].update("img\Erro.png")
                else:
                        self.window["valor_moeda"].update("img\Erro.png")
                        self.window["resultado"].update("")
                        self.window["variacao"].update("")
                        self.window["porcentagem_var"].update("")
            
            if bool(values["valor"]) == False:            
                    self.window["valor_moeda"].update("img\Valor Moeda.png")
                    self.window["resultado"].update("")
                    self.window["variacao"].update("")
                    self.window["porcentagem_var"].update("")
                    
if __name__ == "__main__":
    t = Main()
    t.executar()