"""
Testes funcionais de login com Selenium Python
Rodar com: pytest -v test_selenium_login.py
Instalar: pip install selenium pytest
(precisa do chromedriver no PATH)
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.implicitly_wait(5)
    yield d
    d.quit()


def wait(d):
    return WebDriverWait(d, 10)


# ---------- 1. SauceDemo ----------

def test_saucedemo_login_sucesso(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait(driver).until(EC.url_contains("inventory.html"))
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    wait(driver).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    assert driver.find_element(By.ID, "login-button").is_displayed()


def test_saucedemo_login_falha(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.ID, "login-button").click()

    erro = wait(driver).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert erro.is_displayed()


# ---------- 2. The Internet (Herokuapp) ----------

def test_theinternet_login_sucesso(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait(driver).until(EC.url_contains("/secure"))
    assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text

    driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
    assert driver.find_element(By.ID, "username").is_displayed()


def test_theinternet_login_falha(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_errada")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    assert "Your username is invalid!" in driver.find_element(By.ID, "flash").text


# ---------- 3. Practice Test Automation ----------

def test_practicetest_login_sucesso(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    wait(driver).until(EC.url_contains("logged-in-successfully"))
    assert driver.find_element(By.TAG_NAME, "h1").text == "Logged In Successfully"

    driver.find_element(By.LINK_TEXT, "Log out").click()
    assert driver.find_element(By.ID, "username").is_displayed()


def test_practicetest_login_falha(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.find_element(By.ID, "username").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    erro = wait(driver).until(EC.visibility_of_element_located((By.ID, "error")))
    assert "Your username is invalid!" in erro.text


# ---------- 4. OrangeHRM Demo ----------

def test_orangehrm_login_sucesso(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    titulo = wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6"))
    )
    assert titulo.text == "Dashboard"

    driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    assert driver.find_element(By.NAME, "username").is_displayed()


def test_orangehrm_login_falha(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.NAME, "username").send_keys("usuario_invalido")
    driver.find_element(By.NAME, "password").send_keys("senha_errada")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    erro = wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-alert-content-text"))
    )
    assert "Invalid credentials" in erro.text
