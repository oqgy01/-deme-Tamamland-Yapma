#Doğrulama Kodu
import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/spreadsheets/d/1AP9EFAOthh5gsHjBCDHoUMhpef4MSxYg6wBN0ndTcnA/edit#gid=0"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
first_cell = soup.find("td", {"class": "s2"}).text.strip()
if first_cell != "Aktif":
    exit()
first_cell = soup.find("td", {"class": "s1"}).text.strip()
print(first_cell)


from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.chrome.service import Service
import tkinter as tk
from tkinter import simpledialog
import chromedriver_autoinstaller



print(" ")
print("Oturum Açma Başarılı Oldu")
print(" /﹋\ ")
print("(҂`_´)")
print("<,︻╦╤─ ҉ - -")
print("/﹋\\")
print("(Kod Bekçisi)")
print("Mustafa ARI")
print(" ")
print("https://docs.google.com/spreadsheets/d/1t6IMKuGjy2-VnW9VlwfGJ0i1wxOXi05BTPLKAMTQdXU/edit#gid=0")



google_sheet_url = "https://docs.google.com/spreadsheets/d/1t6IMKuGjy2-VnW9VlwfGJ0i1wxOXi05BTPLKAMTQdXU/gviz/tq?tqx=out:csv&gid=2093893541"

try:
    google_df = pd.read_csv(google_sheet_url)
    google_excel_file = "E-Tablodaki Ödeme Tamamlandılar.xlsx"
    google_df.to_excel(google_excel_file, index=False)
except Exception as e:
    print(f"Error: {e}")





#Selenium Giriş Yapma
options = webdriver.ChromeOptions()

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--log-level=1') 
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  
driver = webdriver.Chrome(options=chrome_options)

login_url = "https://task.haydigiy.com/kullanici-giris/?ReturnUrl=%2Fadmin"
driver.get(login_url)

email_input = driver.find_element("id", "EmailOrPhone")
email_input.send_keys("mustafa_kod@haydigiy.com")

password_input = driver.find_element("id", "Password")
password_input.send_keys("123456")
password_input.send_keys(Keys.RETURN)


# Google Sheets verilerini içeren Excel dosyasını okuyun
google_df = pd.read_excel("E-Tablodaki Ödeme Tamamlandılar.xlsx")


# Giriş yaptıktan sonra işlem yapmak için her bir satırdaki "Link" sütunundaki URL'leri ziyaret edin
for index, row in google_df.iterrows():
    link = row["Link"]
    driver.get(link)
    
    
    # Düzenleme butonunu bulun
    edit_button = driver.find_element(By.ID, "markreturnaspaid")

    

    # Düzenleme butonuna tıklayın
    edit_button.click()


    # Kaydetme onayı için gerekli butonu bulun
    confirmation_button = driver.find_element(By.ID, "markreturnaspaid-action-confirmation-submit-button")

    # Kaydetme onayı butonuna tıklayın
    confirmation_button.click()
    
    
    
kurgu_excel_adi = "E-Tablodaki Ödeme Tamamlandılar.xlsx"

# Dosyayı sil
if os.path.exists(kurgu_excel_adi):
    os.remove(kurgu_excel_adi)
else:
    print(f"{kurgu_excel_adi} dosyası zaten mevcut değil.")


# Tarayıcıyı kapatın
driver.quit()





