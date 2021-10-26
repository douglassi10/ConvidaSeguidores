from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get("https://www.instagram.com")
time.sleep(5)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("douglasmaltapb")

navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("")

navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)

navegador.get("https://www.instagram.com/tvsolpatos/")
time.sleep(4)
navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').click()
time.sleep(3)

fBody  = navegador.find_element_by_xpath("//div[@class='isgrP']") #pega referencia de seguidores da janela popup

cont = 0
quant = 0
while True:
    seguidores = navegador.find_elements_by_class_name('sqdOP') #pega lista de botoes visiveis na janela
   
    for seguidor in seguidores: #itera entre lista seguidores carregados
        if(seguidor.text == 'Seguir' and cont < 40):
            seguidor.click() #clica em cima do botão seguir
            print('seguin')
            cont += 1
            print(cont)
            quant += 1
            print(quant)
            time.sleep(1)

    if(cont >= 30):
        time.sleep(1800)
        cont = 0

    i = 0
    for i in range(5): # scroll 5 times, 
        navegador.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(2)
        print('rool')

