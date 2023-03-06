import PySimpleGUI as sg
import requests
import re

def page_conversor():
    sg.theme_background_color("white")
    cabecalho = [sg.Image(filename="img\cabecalho.png", background_color="white", pad=(0,(0,20)),)]
    valor_equivalente = [
        [sg.Image(filename="img//Valor Moeda.png", background_color="white",pad=(0,(0,5)), k="valor_moeda")],
        [sg.Input("", background_color="white", size=(28,1),border_width=0, font="Inter 12 bold", justification="c", focus=True, k="valor")],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(0,(0,20)))],
    ]
    
    pais_equivalente = [sg.OptionMenu([
        "BRL - Real Brasileiro",
"EUR - Euro",
"USD - Dólar Americano",
"AUD - Dólar Australiano",
"ARS - Peso Argentino",
"CAD - Dólar Canadense",
"CHF - Franco Suíço",
"CLP - Peso Chileno",
"DKK - Coroa Dinamarquesa",
"HKD - Dólar de Hong Kong",
"JPY - Iene Japonês",
"MXN - Peso Mexicano",
"SGD - Dólar de Cingapura",
"AED - Dirham dos Emirados",
"BBD - Dólar de Barbados",
"BHD - Dinar do Bahrein",
"CNY - Yuan Chinês",
"CZK - Coroa Checa",
"EGP - Libra Egípcia",
"GBP - Libra Esterlina",
"HUF - Florim Húngaro",
"IDR - Rupia Indonésia",
"ILS - Novo Shekel Israelense",
"INR - Rúpia Indiana",
"ISK - Coroa Islandesa",
"JMD - Dólar Jamaicano",
"JOD - Dinar Jordaniano",
"KES - Shilling Queniano",
"KRW - Won Sul-Coreano",
"LBP - Libra Libanesa",
"LKR - Rúpia de Sri Lanka",
"MAD - Dirham Marroquino",
"MYR - Ringgit Malaio",
"NAD - Dólar Namíbio",
"NOK - Coroa Norueguesa",
"NPR - Rúpia Nepalesa",
"NZD - Dólar Neozelandês",
"OMR - Rial Omanense",
"PAB - Balboa Panamenho",
"PHP - Peso Filipino",
"PKR - Rúpia Paquistanesa",
"PLN - Zlóti Polonês",
"QAR - Rial Catarense",
"RON - Leu Romeno",
"RUB - Rublo Russo",
"SAR - Riyal Saudita",
"SEK - Coroa Sueca",
"THB - Baht Tailandês",
"TRY - Nova Lira Turca",
"VEF - Bolívar Venezuelano",
"XAF - Franco CFA Central",
"XCD - Dólar do Caribe Oriental",
"XOF - Franco CFA Ocidental",
"ZAR - Rand Sul-Africano",
"TWD - Dólar Taiuanês",],auto_size_text=True, k="equivalente",background_color="white",text_color="green",pad=(0,(0,20)))]
    pais_equivalecia = [sg.OptionMenu([
"BRL - Real Brasileiro",
"EUR - Euro",
"USD - Dólar Americano",
"AUD - Dólar Australiano",
"ARS - Peso Argentino",
"CAD - Dólar Canadense",
"CHF - Franco Suíço",
"CLP - Peso Chileno",
"DKK - Coroa Dinamarquesa",
"HKD - Dólar de Hong Kong",
"JPY - Iene Japonês",
"MXN - Peso Mexicano",
"SGD - Dólar de Cingapura",
"AED - Dirham dos Emirados",
"BBD - Dólar de Barbados",
"BHD - Dinar do Bahrein",
"CNY - Yuan Chinês",
"CZK - Coroa Checa",
"EGP - Libra Egípcia",
"GBP - Libra Esterlina",
"HUF - Florim Húngaro",
"IDR - Rupia Indonésia",
"ILS - Novo Shekel Israelense",
"INR - Rúpia Indiana",
"ISK - Coroa Islandesa",
"JMD - Dólar Jamaicano",
"JOD - Dinar Jordaniano",
"KES - Shilling Queniano",
"KRW - Won Sul-Coreano",
"LBP - Libra Libanesa",
"LKR - Rúpia de Sri Lanka",
"MAD - Dirham Marroquino",
"MYR - Ringgit Malaio",
"NAD - Dólar Namíbio",
"NOK - Coroa Norueguesa",
"NPR - Rúpia Nepalesa",
"NZD - Dólar Neozelandês",
"OMR - Rial Omanense",
"PAB - Balboa Panamenho",
"PHP - Peso Filipino",
"PKR - Rúpia Paquistanesa",
"PLN - Zlóti Polonês",
"QAR - Rial Catarense",
"RON - Leu Romeno",
"RUB - Rublo Russo",
"SAR - Riyal Saudita",
"SEK - Coroa Sueca",
"THB - Baht Tailandês",
"TRY - Nova Lira Turca",
"VEF - Bolívar Venezuelano",
"XAF - Franco CFA Central",
"XCD - Dólar do Caribe Oriental",
"XOF - Franco CFA Ocidental",
"ZAR - Rand Sul-Africano",
"TWD - Dólar Taiuanês",],auto_size_text=True, k="equivalecia",background_color="white",text_color="red",pad=(0,(0,20)))],
    
    resultado = [
        [sg.Input("", background_color="white", size=(30,1),border_width=0, font="Inter 10 bold", disabled=True,disabled_readonly_background_color="white",justification="c", focus=True, k="resultado")],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(0,(0,20)))],
    ]                
    variacao = [
        [sg.Image(filename="img\Variação.png", background_color="white",pad=(0,(0,5)))],
        [sg.Input("", background_color="white", size=(28,1),border_width=0, font="Inter 12 bold",disabled=True,disabled_readonly_background_color="white", justification="c", focus=True, k="variacao")],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(0,(0,20)))],
    ]                
    porcentagem_variacao = [
        [sg.Image(filename="img\Porcentagem Variação.png", background_color="white",pad=(0,(0,5)),)],
        [sg.Input("", background_color="white", size=(28,1),border_width=0, font="Inter 12 bold",disabled=True,disabled_readonly_background_color="white", justification="c", focus=True, k="porcentagem_var")],
        [sg.Image(filename="img\Line 1.png", background_color="white", pad=(0,(0,20)))],
    ]                
    
    layout = [cabecalho, valor_equivalente,pais_equivalente, pais_equivalecia, resultado, variacao, porcentagem_variacao]
    window = sg.Window("Conversor", layout=layout, margins=(0,0), element_justification='c', size=(310,556))
    
    while True:
        event, values = window.read(timeout=10)
        
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
                        valor_cotacao = ""
                        valor_variacao = valores[pais]["varBid"]
                        valor_porc_variacao = valores[pais]["pctChange"]
                        window["valor_moeda"].update("img\Valor Moeda.png")
                        window["resultado"].update(f"{valor_moeda} {pais_1} igual a {valor_cotacao} {pais_2}")
                        window["variacao"].update(f"{valor_variacao}")
                        window["porcentagem_var"].update(f"{valor_porc_variacao}")
                    except KeyError as erro:
                        print(erro)
            else:
                    window["valor_moeda"].update("img\Erro.png")
                    window["resultado"].update("")
                    window["variacao"].update("")
                    window["porcentagem_var"].update("")
        
        if bool(values["valor"]) == False:            
                window["valor_moeda"].update("img\Valor Moeda.png")
                window["resultado"].update("")
                window["variacao"].update("")
                window["porcentagem_var"].update("")
            
page_conversor()