from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep #chrome kapanmasın dıye
from selenium.webdriver.common.by import By

class tests:

    def __init__(self) -> None:
        pass


    def  nullnameAndPassword():
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        loginButton = driver.find_element(By.ID,"login-button")
        sleep(1)
        loginButton.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"mesaj: {errorMessage.text}")
        testResult= errorMessage.text == "Epic sadface: Username is required"
        
        print(f"Test Sonucu: {testResult}")



    def nullPassword():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
         
        inputName = driver.find_element(By.ID,"user-name")
        inputName.send_keys("salih")

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"mesaj: {errorMessage.text}")
        testResult= errorMessage.text == "Epic sadface: Password is required"

        print(f"Test Sonucu: {testResult}")

    
    def lockedUser():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
         
        inputName = driver.find_element(By.ID,"user-name")
        inputName.send_keys("locked_out_user")
        sleep(1)

        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(1)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(f"mesaj: {errorMessage.text}")
        testResult= errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

        print(f"Test Sonucu: {testResult}")


        
    def xButton():
         
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

        loginButton = driver.find_element(By.ID,"login-button")
        sleep(1)
        loginButton.click()
        sleep(1)
                        
        xbutton1=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)

        print(f"buton gorunurluğu: {xbutton1.is_displayed()}")
        xbutton1.click()
        print(f"çarpı tıklandı")
        sleep(1)
        print("Test Başarılı")
        

    
        
        

    
    def loginUser():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
         
        inputName = driver.find_element(By.ID,"user-name")
        inputName.send_keys("standard_user")
        sleep(1)

        inputPassword=driver.find_element(By.ID,"password")
        inputPassword.send_keys("secret_sauce")
        sleep(1)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        if(driver.current_url=="https://www.saucedemo.com/inventory.html"):
            print("sayfa basarılı sekilde yüklendi")

    
        list = driver.find_elements(By.CLASS_NAME, "inventory_item")
        
        if(len(list)==6):
            print("test sonucu başarılı")
        
        
   
    loginUser()
