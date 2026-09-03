#Hector Malaga Rodriguez     951    03/09/2026
from tkinter import simpledialog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def navegar(paginas_navegar):
    url = "https://www.amazon.com.mx"

    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1500,800")

    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get(url)
    time.sleep(3)

    txt_busqueda = navegador.find_element(By.ID, "twotabsearchtextbox")
    btn_busqueda = navegador.find_element(By.ID, "nav-search-submit-button")
    txt_busqueda.send_keys("RAM DDR5")
    time.sleep(3)
    btn_busqueda.click()
    time.sleep(3)
    navegador.save_screenshot("1.png")

    for pagina in range(paginas_navegar):
        if pagina < paginas_navegar - 1:
            next_btn = navegador.find_element(By.LINK_TEXT,"Siguiente")
            next_btn.click()
            time.sleep(3)
            navegador.save_screenshot(f"{pagina}.png")


    navegador.quit()

if __name__ == '__main__':
    numero = simpledialog.askinteger("SELECCIÓN PÁGINAS", "Cuantas páginas quiere navegar (escriba un número)?")
    navegar(numero)