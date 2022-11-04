import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s=Service('F:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#open and login
driver.get("https://qa.neapro.site/login/")
#adjust window size
#driver.set_window_size(1280, 1024)
driver.maximize_window()
#driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("madrockgod@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
time.sleep(2)

#passport form open
#driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[3]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]").click()
#over CSS
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()

#surname form
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Кутузов")
time.sleep(0.5)
#name form
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Михаил")
time.sleep(0.5)
#middle name form
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Илларионович")
time.sleep(0.5)

#date of birth form
datefield=driver.find_element(By.XPATH, "//*[@id='birthday']/div/input")
datefield.click()
datefield.clear()
datefield.send_keys("10.10.2000")
time.sleep(0.5)

#passportSeries form
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").send_keys("4815")
time.sleep(0.5)
#passportNumber form
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").send_keys("162342")
time.sleep(0.5)
#date of issue form
datefield=driver.find_element(By.XPATH, "//*[@id='dateOfIssue']/div/input")
datefield.click()
datefield.clear()
datefield.send_keys("20.10.2020")
time.sleep(1)

#unit code form
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").send_keys("123456")
time.sleep(0.5)
#cardId form
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").send_keys("42424242424")
time.sleep(0.5)

#issued form
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("УМВД России по Выборгскому району г. Санкт-Петербурга")
time.sleep(1)
#adress form????
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").clear()
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys("Простоквашино")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.XPATH, "//*[@id='address']/div/div/input").send_keys(Keys.ENTER)
time.sleep(2)
#phonenumber form
driver.find_element(By.ID, "phone").clear()
driver.find_element(By.ID, "phone").send_keys("1234567890")
time.sleep(0.5)
#privacy checkbox????
#driver.find_element(By.ID, "privacy").clear()
#time.sleep(1)

#add passport foto form
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("F:\Test\doc\pass.jpg")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)

#diplom form
driver.find_element(By.CSS_SELECTOR, "div.body.documents-tiles > div:nth-child(2)").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("F:\Test\doc\dip.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)

#contract form
driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div.body.documents-tiles > div:nth-child(1) > div.document-name").click()
time.sleep(2)
#driver.find_element(By.CSS_SELECTOR, "div.form.contract-form.document-form > div.body > div.buttons > button:nth-child(1)").click()
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("F:\Test\doc\dog.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)

#statement form
driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div.body.documents-tiles > div:nth-child(2) > div.document-name").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("F:\Test\doc\state.jpg")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(2)
#agreement form
driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div.body.documents-tiles > div:nth-child(3) > div.document-name").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".upload-widget > input").send_keys("F:\Test\doc\greement.pdf")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.fill").click()
time.sleep(1)

#logout
driver.execute_script('window.localStorage.clear();')
time.sleep(3)
driver.refresh()
time.sleep(1)

#admin login
driver.get("https://adminqa.neapro.site/login")
driver.maximize_window()
driver.find_element(By.ID, "admin_email").send_keys("moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
time.sleep(1)
#docks approve
driver.find_element(By.NAME, "commit").click()
driver.get("https://adminqa.neapro.site/documents?q%5Buser_id_eq%5D=2190&commit=%D0%A4%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C&order=id_desc")
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[1]/td[6]/div/div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[2]/td[6]/div/div[1]").click()
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[3]/td[6]/div/div[1]").click()
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[4]/td[6]/div/div[1]").click()
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div/form/div[2]/div[1]/div/div/table/tbody/tr[5]/td[6]/div/div[1]").click()
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys("Принят")
driver.find_element(By.XPATH, "/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
time.sleep(1)

#user pass change
driver.get("https://adminqa.neapro.site/users/2190/edit")