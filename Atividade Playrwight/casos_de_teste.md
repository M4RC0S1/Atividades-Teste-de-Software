# Casos de teste funcionais — Login

| ID | Plataforma | Cenário | Passos | Resultado esperado |
|----|-----------|---------|--------|---------------------|
| CT01 | SauceDemo | Login válido + logout | Acessar site → preencher standard_user/secret_sauce → login → logout | Vai para /inventory.html com "Products"; após logout volta à tela de login |
| CT02 | SauceDemo | Login inválido | Acessar site → credenciais erradas → login | Mensagem de erro exibida |
| CT03 | The Internet | Login válido + logout | Acessar /login → tomsmith/SuperSecretPassword! → login → logout | Vai para /secure com flash "You logged into a secure area!"; logout retorna ao login |
| CT04 | The Internet | Login inválido | Acessar /login → credenciais erradas → login | Flash "Your username is invalid!" |
| CT05 | Practice Test Automation | Login válido + logout | Acessar página → student/Password123 → login → logout | Vai para /logged-in-successfully/ com "Logged In Successfully"; logout retorna ao login |
| CT06 | Practice Test Automation | Login inválido | Acessar página → credenciais erradas → login | Erro "Your username is invalid!" |
| CT07 | OrangeHRM | Login válido + logout | Acessar /auth/login → Admin/admin123 → login → logout | Dashboard carregado; logout retorna ao login |
| CT08 | OrangeHRM | Login inválido | Acessar /auth/login → credenciais erradas → login | Mensagem "Invalid credentials" |

Cada CT foi implementado igual nas duas ferramentas (Playwright e Selenium), arquivos:
- `test_playwright_login.py`
- `test_selenium_login.py`
