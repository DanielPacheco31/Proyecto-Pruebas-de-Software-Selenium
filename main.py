from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    return webdriver.Chrome(options=options)

def registrar_usuario(driver):
    print("Registrando usuario...")
    
    driver.get("http://127.0.0.1:8000/usuarios/registro/")
    time.sleep(3)
    
    datos_usuario = {
        "nombre_usuario": "Sebastian1",
        "nombre": "Sebastian",
        "apellido": "Martinez", 
        "cedula": "2223222233",
        "telefono": "3232034565",
        "correo_electronico": "Test1@gmail.com",
        "direccion": "calle Test 127",
        "fecha_nacimiento": "03011989",
        "contraseña1": "MiPassword12345#",
        "contraseña2": "MiPassword12345#",
    }
    
    for campo, valor in datos_usuario.items():
        try:
            element = driver.find_element(By.NAME, campo)
            element.clear()
            element.send_keys(valor)
            time.sleep(0.5)
        except:
            try:
                element = driver.find_element(By.ID, campo)
                element.clear()
                element.send_keys(valor)
                time.sleep(0.5)
            except:
                pass
    
    try:
        submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
        submit_btn.click()
    except:
        try:
            submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_btn.click()
        except:
            pass
    
    time.sleep(3)

def iniciar_sesion(driver):
    print("Iniciando sesion...")
    
    driver.get("http://127.0.0.1:8000/usuarios/login/")
    time.sleep(3)
    
    try:
        campo_usuario = driver.find_element(By.NAME, "username")
        campo_usuario.send_keys("Sebastian1")
    except:
        try:
            campo_usuario = driver.find_element(By.ID, "username")
            campo_usuario.send_keys("Sebastian1")
        except:
            pass
    
    try:
        campo_password = driver.find_element(By.NAME, "password")
        campo_password.send_keys("MiPassword12345#")
    except:
        try:
            campo_password = driver.find_element(By.ID, "password")
            campo_password.send_keys("MiPassword12345#")
        except:
            pass
    
    try:
        login_btn = driver.find_element(By.XPATH, "//input[@type='submit']")
        login_btn.click()
    except:
        try:
            login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_btn.click()
        except:
            pass
    
    time.sleep(3)

def tomar_captura(driver, nombre):
    driver.save_screenshot(f"{nombre}.png")
    print(f"Captura guardada: {nombre}.png")

def main():
    driver = get_driver()
    
    # Registro
    registrar_usuario(driver)
    tomar_captura(driver, "01_registro")
    
    # Login
    iniciar_sesion(driver)
    tomar_captura(driver, "02_login")
    
    print("Proceso completado")
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    main()