from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import win32clipboard
import pyautogui
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
driver = webdriver.Chrome()
driver.get("https://goo.gl/WCS3hC")
wait = WebDriverWait(driver, 600)
driver.maximize_window()
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('http://secim.parti.org.tr/')
wait = WebDriverWait(driver, 600)
kllnc = driver.find_element_by_xpath("//*[@id='txtKullaniciAdi']")
prl = driver.find_element_by_xpath("//*[@id='txtParola']")
kllnc.send_keys("kullanıcı_adı")
prl.send_keys("parola")
buton = driver.find_element_by_xpath("//*[@id='btnLogin']") 
wait = WebDriverWait(driver, 600)
buton.click()
driver.switch_to_window(driver.window_handles[0])
isim = 'parti_grup'

input('Kare Kod tanıtıldıktan sonra "enter" giriniz')
whatsapp_grup= driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
whatsapp_grup.click()
onceki_msj = "Null"
data = "okunmadı"
def parti_tc_sorgula(tc)
    driver.switch_to_window(driver.window_handles[1])
    sekme = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[1]/div/div[1]/input")
    sekme.send_keys(tc)
    buton = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div/div[3]/center/input[1]")
    buton.click()
    yanit =driver.find_element_by_xpath("//*[@id='resultStats']")
    driver.switch_to_window(driver.window_handles[0]
    return yanit
def basamak(sayi):
    sayac=0
    while sayi:
        sayac+=1       
        sayi=sayi/10
        sayi=int(sayi)
    return sayac
def tc(tc):
    
    y = [int(i) for i in tc.split() if i.isdigit()]
    
    try:
        x=y[0]
        bsmk = basamak(x)
        if (bsmk == 11):
            liste = []
            for i in str(x):
                liste.append(i)
            liste = [int(i) for i in liste]
            ksl1 = (liste[0]+liste[2]+liste[4]+liste[6]+liste[8])*7
            ksl2 = (liste[1]+liste[3]+liste[5]+liste[7])*9
            ksl3 = ksl1+ksl2
            ksl4 = ksl3 % 10
            ksl5 = (liste[0]+liste[2]+liste[4]+liste[6]+liste[8])*8
            ksl6 = ksl5 % 10
if (ksl4 == liste[9] and ksl6 == liste[10] ):
                sandik = parti_tc_sorgula(x)
                box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                box.send_keys(x," tc kimlik numaralı şahsın sandık numarası: ",sandik + Keys.ENTER)
                
            else:
                print(x," tc kimlik numarasını hatalı girdiniz..")
                box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                box.send_keys(x," tc kimlik numarasını hatalı girdiniz..\lütfen tekrar deneyin" + Keys.ENTER)
except IndexError:
        print("sayı yok")
def mesajoku():
    global onceki_msj
    global data
    pyautogui.doubleClick(742,886)
    pyautogui.click(742,886)
    pyautogui.hotkey('ctrl', 'c')
try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        
        win32clipboard.CloseClipboard()
if (data != onceki_msj):
            onceki_msj=data
            tc(data)
    
        
    except TypeError:
        pyautogui.click(1793,893)
        win32clipboard.OpenClipboard()
        win32clipboard.CloseClipboard()
x=1
while x < 3:
    
    mesajoku()
    time.sleep(10)
