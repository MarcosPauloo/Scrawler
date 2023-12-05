from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import time



chrome_options = Options()
chrome_options.add_argument('--headless')
drive = webdriver.Chrome()
wait = WebDriverWait(drive, 10)

drive.get("https://www.jusbrasil.com.br/artigos-noticias/busca?q=seguran%C3%A7a+de+dados")

dados =[];

site_html = wait.until(lambda driver:drive.find_elements(By.XPATH,'*//h2/a'))


# for site in site_html:
#     titulo = site.find_element(by=By.XPATH, value='.//h2[@class="search-results_SearchResults-title__QeJBI"]').text
#     aux = site.find_elements(By.XPATH,'.//article')
#     dicionario = {}
#     dicionario['titulo']=titulo;

#     index = 0
#     for a in aux:
#         index=index+1

#         subtitulo = a.find_element(by=By.XPATH, value='*//a[@data-testid="search-snippet-title-link"]').text
#         texto = a.find_element(by=By.XPATH, value='.//div[@data-testid="search-snippet-base-body"]//p').text

#         dicionario['subtitulo'+str(index)]=subtitulo
#         dicionario['texto'+str(index)]=texto

#     dados.append(dicionario)
        
#     with open('dados.json', 'w', encoding='utf-8') as file:
#         json.dump(dados, file, ensure_ascii=False,indent=2)

print(site_html)

drive.close()
