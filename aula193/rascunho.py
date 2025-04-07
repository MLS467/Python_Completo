from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVE_EXEC = ROOT_FOLDER / "drivers" / "chromedriver.exe"

# colocar opções quando executar
chrome_options = webdriver.ChromeOptions()

# Servico utilizado o path do drive
chrome_service = Service(executable_path=CHROMEDRIVE_EXEC)

# o navegador que vai usar
params = {"service": chrome_service, "options": chrome_options}
chrome_browser = webdriver.Chrome(**params)

if __name__ == "__main__":
    # tempo de espera antes de fechar
    TIME_TO_WAIT = 120

    # abrindo a página
    chrome_browser.get("http://localhost:8000/html/")

    # esperando até encontrar o elemento selecionado
    search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.ID, "email"))
    )

    # search_input.send_keys("Hello Word test")
    for i in range(2):
        # pegando o elemento pai para pegar as tags filhas
        classe = "main-header-form"
        element_father = chrome_browser.find_element(By.CLASS_NAME, classe)

        # pegando vários elementos por tags find_elements
        inputs = element_father.find_elements(By.TAG_NAME, "input")

        # pegando um campo com find_element
        text_area = element_father.find_element(By.TAG_NAME, "textarea")

        # escrevendo no campo send_keys
        inputs[0].send_keys("John")
        inputs[1].send_keys("Doe")
        inputs[2].send_keys("John.Doe@gmail.com")
        text_area.send_keys("aaaaaaaaaaaaaaassssssssssssssddddddddddddd")

        # se sabe se o elemento vai estar pronto é só usar o find_element
        btn_send = chrome_browser.find_element(By.ID, "send_menssage")
        time.sleep(10)
        btn_send.click()

time.sleep(TIME_TO_WAIT)
