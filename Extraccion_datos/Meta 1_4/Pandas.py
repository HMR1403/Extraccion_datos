#Hector Malaga Rodriguez     951    09/09/2026

import time
from tkinter import simpledialog
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def extraer(data, page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    lista = soup.find_all('div', class_="a-section a-spacing-base desktop-grid-content-view")
    for item in lista:
        nombre = item.find("h2", class_="a-size-base-plus a-spacing-none a-color-base a-text-normal")
        precio = item.find("span", class_="a-price-whole")
        entrega = item.find("div", class_="a-row a-color-base udm-primary-delivery-message")
        data["nombre"].append(nombre.text if nombre else "No contiene nombre")
        data["precio"].append(precio.text if precio else "Precio no disponible")
        data["entrega_fecha"].append(entrega.text if entrega else "Fecha de entrega no disponible")

def navegar(prod_bus, paginas):
    data = {"nombre": [],"precio": [],"entrega_fecha": []}

    url = "https://www.amazon.com.mx"

    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1500,800")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get(url)
    time.sleep(4)

    txt_busqueda = navegador.find_element(By.ID,"twotabsearchtextbox")
    btn_busqueda = navegador.find_element(By.ID,"nav-search-submit-button")
    txt_busqueda.send_keys(prod_bus)
    time.sleep(3)
    btn_busqueda.click()
    time.sleep(3)

    for pagina in range(paginas):
        time.sleep(1)
        extraer(data, navegador.page_source)
        next_btn = navegador.find_element(By.LINK_TEXT,"Siguiente")
        if next_btn:
            next_btn.click()
        else:
            break
        time.sleep(3)

    time.sleep(2)
    navegador.quit()
    return data


if __name__ == "__main__":
    producto_buscado = simpledialog.askstring("BUSCADOR", "Ingrese el nombre del producto que busca:")
    pag = simpledialog.askinteger("BUSCADOR", "Cuantas paginas desea recorrer")
    data = navegar(producto_buscado,pag)
    print("Total de articulos: ", len(data["nombre"]))
    df = pd.DataFrame(data)
    df.to_csv("documento/data.csv", index=False)