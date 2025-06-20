https://github.com/Hexlet/ru-test-assignments/blob/main/QA%2FEffective%20Mobile%2FREADME.md

E2E UI

Цель:
Создать автоматический e2e тест для проверки сценария покупки товара на сайте saucedemo.com с использованием Python + Selenium или Playwright. Тест должен проверять процесс от авторизации до завершения покупки, с возможностью легко воспроизвести его на любом компьютере.

Требования:
1. Сценарий теста:
Тест должен выполнять следующие действия на сайте saucedemo.com:

Авторизация: Использовать тестовый аккаунт:
Логин: standard_user
Пароль: secret_sauce
Выбор товара: Выбрать один товар (например, "Sauce Labs Backpack") и добавить его в корзину.
Оформление покупки:
Перейти в корзину и убедиться, что товар добавлен.
Оформить покупку, заполнив поля
Завершить покупку.
Проверка: Убедиться, что покупка завершена успешно.

(ChatGPT generated)

# 🧪 Saucedemo E2E UI Automation Test

This project automates an end-to-end (E2E) UI test of the product purchase flow on [saucedemo.com](https://www.saucedemo.com/) using **Python** and **Selenium WebDriver**.

## 🚀 Features

- Logs in with test credentials
- Adds a product to the shopping cart
- Proceeds through checkout
- Verifies successful order completion
- Cleanly closes the browser

## 🛠 Tech Stack

- Python 3
- Selenium
- WebDriver Manager
- Fake UserAgent

## 🧰 Installation

```bash
git clone https://github.com/your-username/saucedemo-com.git
cd saucedemo-com

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
