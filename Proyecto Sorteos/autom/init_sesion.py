# codigo para iniciar session [ INCOMPLETO ]

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
time.sleep(1)
# driver.quit()

time.sleep(3)


boton_ahora_no = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
if boton_ahora_no.is_displayed() :
    print('ca esta')
    boton_ahora_no.click()

time.sleep(3)


boton_ahora_no_2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')
if boton_ahora_no_2.is_displayed() :
    print('ca esta')
    boton_ahora_no_2.click()

time.sleep(2)

# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

time.sleep(2)
driver.get('https://www.instagram.com/p/CPWxqK1jgg6/?utm_source=ig_web_copy_link')


time.sleep(1)
