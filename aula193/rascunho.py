from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVE_EXEC = ROOT_FOLDER / "drivers" / "chromedriver.exe"

# colocar opções quando executar
chrome_options = webdriver.ChromeOptions()

# Servico utilizado o path do drive
chrome_service = Service(executable_path=CHROMEDRIVE_EXEC)

# o navegador que vai usar
params = {"service": chrome_service, "options": chrome_options}
chrome_browser = webdriver.Chrome(**params)


chrome_browser.get("https://www.google.com.br/")
time.sleep(30)
