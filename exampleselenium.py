from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Navega a la URL
#driver=webdriver.Edge('C:/Users/norma/PythonProjects/wasamasivo/msedgedriver.exe')

#driver.switch_to_window("http://www.facebook.com")
#driver.switch_to.window("http://www.facebook.com")
# Inserta el texto "Webdriver" y ejecuta la accion del teclado "ENTER"

#driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)
#driver.send_keys("webdriver" + Keys.ENTER)

#about = driver.find_element_by_link_text('About')
#driver.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()
#driver.switch_to.window(driver.window_handles[-1])
#driver.get("https://stackoverflow.com")
#driver.execute_script("window.open('http://www.facebook.com', 'new_window')")

driver = webdriver.Edge('C:/Users/norma/PythonProjects/wasamasivo/msedgedriver.exe')
#driver.get("http://www.google.com")
#driver.key_down(Keys.CONTROL).send_keys(Keys.CONTROL + 't') 
#driver.switch_to.new_window('tab')
time.sleep(5)
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
time.sleep(30)
