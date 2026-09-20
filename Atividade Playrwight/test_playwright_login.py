"""
Testes funcionais de login com Playwright (Python)
Rodar com: pytest -v test_playwright_login.py
Instalar: pip install pytest-playwright && playwright install
"""
from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        pg = browser.new_page()
        yield pg
        browser.close()


# ---------- 1. SauceDemo ----------

def test_saucedemo_login_sucesso(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")
    expect(page.locator("#login-button")).to_be_visible()


def test_saucedemo_login_falha(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "usuario_invalido")
    page.fill("#password", "senha_errada")
    page.click("#login-button")
    expect(page.locator("[data-test='error']")).to_be_visible()


# ---------- 2. The Internet (Herokuapp) ----------

def test_theinternet_login_sucesso(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")

    page.click("a[href='/logout']")
    expect(page.locator("#username")).to_be_visible()


def test_theinternet_login_falha(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "usuario_invalido")
    page.fill("#password", "senha_errada")
    page.click("button[type='submit']")
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")


# ---------- 3. Practice Test Automation ----------

def test_practicetest_login_sucesso(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.locator("h1")).to_have_text("Logged In Successfully")

    page.click("text=Log out")
    expect(page.locator("#username")).to_be_visible()


def test_practicetest_login_falha(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "usuario_invalido")
    page.fill("#password", "Password123")
    page.click("#submit")
    expect(page.locator("#error")).to_contain_text("Your username is invalid!")


# ---------- 4. OrangeHRM Demo ----------

def test_orangehrm_login_sucesso(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    expect(page.locator(".oxd-topbar-header-breadcrumb h6")).to_have_text("Dashboard")

    page.click(".oxd-userdropdown-tab")
    page.click("text=Logout")
    expect(page.locator("input[name='username']")).to_be_visible()


def test_orangehrm_login_falha(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("input[name='username']", "usuario_invalido")
    page.fill("input[name='password']", "senha_errada")
    page.click("button[type='submit']")
    expect(page.locator(".oxd-alert-content-text")).to_contain_text("Invalid credentials")
