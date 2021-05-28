from selenium import webdriver
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extencions')

driver_path = 'chromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)

#iniciar en segunda pantalla y pequeño a la esquina (opcional amiguero)
driver.set_window_position(0, 0)
driver.set_window_size(height=800, width=800)




# Inicializar el navegador
url_posteo = 'https://www.instagram.com/p/CPadUOdg8B4/?utm_source=ig_web_copy_link'
url_init = 'https://www.instagram.com'

driver.get(url_init)

time.sleep(2)


input_user = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
input_user.click()
input_user.send_keys("lapcdefran@gmail.com")
time.sleep(1)

password = ''
input_pass = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
input_pass.click()
input_pass.send_keys(password)
time.sleep(1)


boton_entrar = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
boton_entrar.click()

# driver.quit()

time.sleep(3)


boton_ahora_no = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
if boton_ahora_no.is_displayed() :
    print('ahora no 1')
    boton_ahora_no.click()

time.sleep(2)


boton_ahora_no_2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')
if boton_ahora_no_2.is_displayed() :
    print('ahora no 2')
    boton_ahora_no_2.click()

time.sleep(2)

# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))


driver.get(url_posteo)




filePath = r"emilylucius.txt"
# with open(filePath, 'r', encoding='utf-8') as f:
# 	[_.rstrip('\n') for _ in f.readlines()]

with open(filePath, "r") as fichero:
    for linea in fichero:
        # Procesar línea a linea

        icon_coment = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button/div')
        if icon_coment.is_displayed() :
            icon_coment.click()
            print('click en icono globo: OK')
            time.sleep(1)
        

        text_area_coment = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        text_area_coment.click()
        text_area_coment.send_keys('@'+linea)
        print('click en text area y comentado: OK')
        time.sleep(2)

        boton_publicar = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')
        if boton_publicar.is_displayed() :
            print('esta el boton!')
            boton_publicar.click()
            print('click en publicar: OK')
            time.sleep(6)
        
        







